"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/10/2021

Purpose:

Details:

Description:

Notes:
    Not thread safe

IMPORTANT NOTES:

Explanation:

Reference:
    Decorating Hex function to pad zeros
        Notes:
            "{0:#0{1}x}".format(42,6) -> '0x002a'
            "{0:#0{1}X}".format(2983096886560,18) -> '0X000002B68E6E2520'
            So
            "{0}{1:0{2}X}".format("0x",2983096886560,16) -> '0x000002B68E6E2520'

        Reference:
            https://stackoverflow.com/questions/12638408/decorating-hex-function-to-pad-zeros

"""
from __future__ import annotations

from collections import defaultdict
from functools import wraps
from typing import Any, Callable, Dict, Union, Sequence

from python_code_analyzer.interpretable.event.event import Event
from python_code_analyzer.interpretable.event.event_border_end_scope_callable import EventBorderEndScopeCallable
from python_code_analyzer.interpretable.event.event_border_end_scope_iteration import EventBorderEndScopeIteration
from python_code_analyzer.interpretable.event.event_border_start_scope_callable import EventBorderStartScopeCallable
from python_code_analyzer.interpretable.event.event_border_start_scope_iteration import EventBorderStartScopeIteration
from python_code_analyzer.interpretable_recorder.interpretable_recorder import InterpretableRecorder
from python_code_analyzer.interpretable_recorder.interpretable_recorder_printer import EventRecorderPrinter

"""
Python frame index for the line number when an event is created

Notes:
    The assumption is -3, it may change if whatever makes events change.
    -3 will probably give you the line number of the event call put in by the user in their code
"""
PYTHON_FRAME_INDEX_DEFAULT = -3


def _decorator_internal_checker(callable_given=None):
    """
    This decorator is uniquely used by the CodeRecoder

    IDK what this should do

    :return:
    """

    # TODO: DO SOMETHING HERE IDK WHAT TO DO WITH THIS, REGULATOR, CHECKER, ETC...

    def decorator(callable_given):
        @wraps(callable_given)
        def wrapper(*args, **kwargs) -> Any:
            # print("HEEEH:", args[0]._scope_recorder._index_scope_order)
            # if args[0]._scope_recorder._index_scope_order != 0:
            #     # TODO: CLEAN UP
            #     warnings.warn(
            #         "index_frame_stack_recorder is {}, it should be 0!".format(args[0]._scope_recorder._index_scope_order),
            #         stacklevel=2)
            #
            #     print("SDFSDF 3")
            #
            # print("SDFSDF 4")
            return callable_given(*args, **kwargs)

        # return the wrapped callable
        return wrapper

    # return the wrapped wrapped callable
    return decorator(callable_given) if callable_given else decorator


class PythonCodeAnalyzer:
    """
    Records the execution of code

    """

    def __init__(self, python_frame_index=PYTHON_FRAME_INDEX_DEFAULT):
        # Make a dictionary to store the callable and its stack frame relative to it being called
        self._dict_k_callable_name_v_index_stack_frame_callable = defaultdict(int)

        #####
        """
        Private vars
        """

        # Frame to find the
        self._python_frame_index = python_frame_index

        # Make a Event recorder object to record the scopes being created and being entered
        self._interpretable_recorder = InterpretableRecorder()

        #####

        self.event_recorder_printer = EventRecorderPrinter(self._interpretable_recorder)

    def decorator_wrapper_callable(self,
                                   callable_given=None,
                                   name_start: Union[str, None] = None,
                                   str_id_start: Union[str, None] = None,
                                   dict_recorded_var_start: Union[Dict[str, Any], None] = None,
                                   name_end: Union[str, None] = None,
                                   str_id_end: Union[str, None] = None,
                                   dict_recorded_var_end: Union[Dict[str, Any], None] = None
                                   ) -> Any:
        """
        Higher order decorator only accessible by this object that you put on top of a callable header to allow that
        callable to be recorded

        1.  Increment and decrement a callable_given's stack frame index.
        2.  Increment and decrement the algorithm recorder's stack frame index (The stack frame relative to the creation
            of the algorithm recorder).
        3.  Makes a event object when the callable is called.
        4.  Keep track of the current callable being called.

        This wrapper wraps the given callable so when the callable is called a new scope is created and
        the stack frame for the self and for the callable is incremented.

        Both the index for the recorder's stack frame and the callable's stack frame are incremented when the callable
        of the same name is called again. Though when a another callable is called the index for that corresponding
        callable is incremented and the recorder's index is incremented.

        Basically, when a callable is called, an event object is created with its corresponding stack frame
        index being incremented and the scope recorder's index being incremented.
        Both the recorder's stack frame index and the corresponding callable scope stack frame
        index is decremented when the callable scope is completed (the function has completed its execution).

        The purpose for the stack frame indices are for recording information about what happens in a scope.

        Notes:
            PyCharm does not notice self within the following 2 functions

        :param callable_given: Callable
        :param name_start:
        :param str_id_start:
        :param dict_recorded_var_start:
        :param name_end:
        :param str_id_end:
        :param dict_recorded_var_end:
        :return: The result from the callable
        """

        def decorator(callable_given_inner: Callable):
            """
            Actual decorator

            :param callable_given_inner:
            :return: wrapped callable_given
            """

            @wraps(callable_given_inner)
            def wrapper(*args, **kwargs) -> Any:
                """
                wrapper than runs the given callable and does the index increment/decrement and scope creation

                :param args: args for callable_given
                :param kwargs: kwargs for callable_given
                :return: Result of the callable
                """

                # Create the scope for the callable_given
                self._event_callable_start(callable_given_inner, args, kwargs, name_start, str_id_start,
                                           dict_recorded_var_start)

                # Execute and return the result's of callable_given
                result = callable_given_inner(*args, **kwargs)

                # State that the scope's callable returned not None
                self._event_callable_end(result, name_end, str_id_end, dict_recorded_var_end)

                # Return the callable's result
                return result

            # return the wrapped callable
            return wrapper

        # return the wrapped wrapped callable
        return decorator(callable_given) if callable_given else decorator

    def event(self,
              name: Union[str, None] = None,
              dict_recorded_vars: Dict[str, Any] = None,
              str_id: Union[str, None] = None
              ) -> None:
        """
        Add a variable's name and a variable's value into the current scope's dictionary of variables and their
        corresponding values

        """

        event_new = Event(name,
                          str_id,
                          self._python_frame_index,
                          dict_recorded_vars)

        self._interpretable_recorder.add_event(event_new)

    def event_iteration_start(self,
                              name: Union[str, None] = None,
                              dict_recorded_vars: Dict[str, Any] = None,
                              str_id: Union[str, None] = None
                              ) -> None:
        """
        State that an iteration scope has been created and push that scope into the scope recorder
        """

        event_new = EventBorderStartScopeIteration(name,
                                                   str_id,
                                                   self._python_frame_index,
                                                   dict_recorded_vars)

        self._interpretable_recorder.add_event(event_new)

    def event_iteration_end(self,
                            name: Union[str, None] = None,
                            dict_recorded_vars: Dict[str, Any] = None,
                            str_id: Union[str, None] = None
                            ) -> None:
        """
        State that an iteration scope has ended normally and pop it from the scope recorder

        :return: None
        """

        event_new = EventBorderEndScopeIteration(name,
                                                 str_id,
                                                 self._python_frame_index,
                                                 dict_recorded_vars)

        self._interpretable_recorder.add_event(event_new)

    def _event_callable_start(self,
                              callable_given: Callable,
                              callable_args: Sequence[Any] = None,
                              callable_kwargs: Dict[str, Any] = None,
                              name: Union[str, None] = None,
                              str_id: Union[str, None] = None,
                              dict_recorded_vars: Dict[str, Any] = None
                              ) -> None:
        """
        Create a ScopeCallable and push it to interpretable recorder

        :return: None
        """

        event_new = EventBorderStartScopeCallable(callable_given,
                                                  callable_args,
                                                  callable_kwargs,
                                                  name,
                                                  str_id,
                                                  self._python_frame_index,
                                                  dict_recorded_vars)

        self._interpretable_recorder.add_event(event_new)

    def _event_callable_end(self,
                            callable_return,
                            name: Union[str, None] = None,
                            str_id: Union[str, None] = None,
                            dict_recorded_vars: Dict[str, Any] = None
                            ) -> None:
        """
        State that an callable's scope has returned with something.
        Pop it from the scope recorder.

        IMPORTANT NOTE:
            THIS SHOULD BE HANDLED AUTOMATICALLY WITH THE DECORATOR

        :return: None
        """

        event_new = EventBorderEndScopeCallable(callable_return,
                                                name,
                                                str_id,
                                                self._python_frame_index,
                                                dict_recorded_vars)

        self._interpretable_recorder.add_event(event_new)

    def get_scope_recorder(self) -> InterpretableRecorder:
        """
        Return the scope recorder object of this algorithm recorder object

        :return: the scope recorder for this object
        """
        return self._interpretable_recorder

    @_decorator_internal_checker
    def print_all(self) -> None:
        """
        Easy print all because I don't know what to show the user

        :return: None
        """

        amount = 100
        border_symbol = "#"

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order Simple")
        print()
        self.event_recorder_printer.print_event_call_order_simple()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order Detailed")
        print()
        self.event_recorder_printer.print_event_call_order_detailed()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order Debug")
        print()
        self.event_recorder_printer.print_event_call_order_debug()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order by String ID")
        print()
        self.event_recorder_printer.print_dict_k_str_id_v_list_interpretable()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order by name")
        print()
        self.event_recorder_printer.print_dict_k_name_v_list_interpretable()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order by __qualname__")
        print()
        self.event_recorder_printer.print_dict_k_qualname_v_list_interpretable()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order by Tuple Line Number")
        print()
        self.event_recorder_printer.print_dict_k_tuple_line_number_v_list_interpretable()
        print()
        print()

        print(border_symbol * amount)
        print(border_symbol * amount)
        print("Event Call Order by Line Number")
        print()
        self.event_recorder_printer.print_dict_k_line_number_v_list_interpretable()
        print()
        print()
