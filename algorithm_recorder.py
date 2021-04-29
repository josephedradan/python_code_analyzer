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

import traceback
from collections import defaultdict
from functools import wraps
from typing import Any

from algorithm_analyzer.event.scope import IterationEnd
from algorithm_analyzer.event.scope_callable import ScopeCallable
from algorithm_analyzer.event.scope_iteration import ScopeIteration
from algorithm_analyzer.event_recorder import EventRecorder
from algorithm_analyzer.event_recorder_printer import EventRecorderPrinter


def _decorator_internal_checker(callable_given=None):
    """
    Checks if a particular method can be called after AlgorithmRecorder has ran

    :return:
    """

    # TODO: DO SOMETHING HERE IDK WHAT TO DO WITH THIS, REGULATOR, CHECKER, ETC...
    # print("SDFSDF")

    def decorator(callable_given):
        # print("SDFSDF 2")

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


class AlgorithmRecorder:

    def __init__(self):

        # Make a dictionary to store the callable and its stack frame relative to it being called
        self._dict_k_callable_v_index_frame_stack_callable = defaultdict(int)

        # Record the stack frame index relative to where this object was created
        self._index_frame_scope_recorder = 0

        # Track the current callable being called
        self._callable_current = None

        # Make a scope recorder object to record the scopes being created and being entered
        self._scope_recorder = EventRecorder()

        self.scope_recorder_printer = EventRecorderPrinter(self._scope_recorder)

    def decorator_wrapper_callable(self, callable_given=None) -> Any:
        """
        Higher order decorator

        1.  Increment and decrement a callable_given's stack frame index.
        2.  Increment and decrement the algorithm recorder's stack frame index (The stack frame relative to the creation
            of the algorithm recorder).
        3.  Makes an a scope object when the callable is called.
        4.  Keep track of the current callable being called.

        This wrapper wraps the given callable so when the callable is called a new scope is created and
        the stack frame for the self and for the callable is incremented.

        Both the index for the recorder's stack frame and the callable's stack frame are incremented when the callable
        of the same name is called again. Though when a another callable is called the index for that corresponding
        callable is incremented and the recorder's index is incremented.

        Basically, when a callable is called, a scope object is created with its corresponding stack frame
        index being incremented and the scope recorder's index being incremented.
        Both the recorder's stack frame index and the corresponding callable scope stack frame
        index is decremented when the callable scope is completed (the function has completed its execution).

        The purpose for the stack frame indices are for recording information about what happens in a scope.

        Notes:
            PyCharm does not notice self within the following 2 functions

        :param callable_given: Callable
        :return: The result from the callable
        """

        def decorator(callable_given):
            """
            Actual decorator

            :param callable_given:
            :return: wrapped callable_given
            """

            @wraps(callable_given)
            def wrapper(*args, **kwargs) -> Any:
                """
                wrapper than runs the given callable and does the index increment/decrement and scope creation

                :param args: args for callable_given
                :param kwargs: kwargs for callable_given
                :return: Result of the callable
                """

                # Track the callable that will be executed
                self._callable_current = callable_given

                # Increment the corresponding callable's stack frame index
                self._dict_k_callable_v_index_frame_stack_callable[callable_given] += 1

                # Increment the recorder's stack frame index
                self._index_frame_scope_recorder += 1

                # Create the scope for the callable_given
                self._callable_scope_start(*args, **kwargs)

                # Execute and return the result's of callable_given
                result = callable_given(*args, **kwargs)

                # State that the scope's callable returned not None
                self._callable_scope_end(result)

                # Decrement the corresponding callable's stack frame index
                self._dict_k_callable_v_index_frame_stack_callable[callable_given] -= 1

                # Decrement the recorder's stack frame index
                self._index_frame_scope_recorder -= 1

                # Return the callable's result
                return result

            # return the wrapped callable
            return wrapper

        # return the wrapped wrapped callable
        return decorator(callable_given) if callable_given else decorator

    def record_variable(self, variable_name: str, variable_value: Any) -> Any:
        """
        Add a variable's name and a variable's value into the current scope's dictionary of variables and their
        corresponding values

        TODO: Should I include the storing of the ending of a scope's variables

        :param variable_name: variable name
        :param variable_value: variable value
        :return:
        """
        stack_top = self._scope_recorder.get_event_stack_top()

        stack_top.record_variable(variable_name, variable_value)

        return variable_value

    def iteration_scope_start(self, name_iterable: str, index_iteration: int) -> None:
        """
        State that an iteration scope has been created and push that scope into the scope recorder

        :rtype: object
        :return: None
        """

        # Get the index of the callable's stack frame
        index_frame_stack_callable = self._dict_k_callable_v_index_frame_stack_callable[self._callable_current]

        # Create a ScopeIteration object
        scope_new = ScopeIteration(
            self._scope_recorder.get_event_stack_top_parent(),
            self._scope_recorder.get_event_stack_top(),
            self._index_frame_scope_recorder,
            index_frame_stack_callable,
            name_iterable,
            index_iteration
        )

        # Push the scope into the scope recorder
        self._scope_recorder.push_event(scope_new)

    def iteration_scope_end_none(self) -> None:
        """
        State that an iteration scope has ended normally and pop it from the scope recorder

        :return: None
        """
        self._scope_recorder.get_event_stack_top().set_end = IterationEnd.NONE
        self._scope_recorder.pop_event()

    def iteration_scope_end_break(self) -> None:
        """
        State that an iteration scope has ended with a break and pop it from the scope recorder

        :return: None
        """
        self._scope_recorder.get_event_stack_top().set_end = IterationEnd.BREAK
        self._scope_recorder.pop_event()

    def iteration_scope_end_continue(self) -> None:
        """
        State that an iteration scope has ended with a continue and pop it from the scope recorder

        :return: None
        """
        self._scope_recorder.get_event_stack_top().set_end = IterationEnd.CONTINUE
        self._scope_recorder.pop_event()

    def _callable_scope_start(self, *args, **kwargs) -> None:
        """
        State that an callable scope has been created and push that scope into the scope recorder

        :return: None
        """

        # Get the index of the callable's stack frame
        index_frame_stack_callable = self._dict_k_callable_v_index_frame_stack_callable[self._callable_current]

        # Create a ScopeCallable object
        scope_new = ScopeCallable(
            self._scope_recorder.get_event_stack_top_parent(),
            self._scope_recorder.get_event_stack_top(),
            self._index_frame_scope_recorder,
            index_frame_stack_callable,
            self._callable_current,
            args,
            kwargs
        )

        # Push the scope into the scope recorder
        self._scope_recorder.push_event(scope_new)

    def _callable_scope_end(self, result) -> None:
        """
        State that an callable's scope has returned with something.
        Pop it from the scope recorder.

        IMPORTANT NOTE:
            THIS SHOULD BE HANDLED AUTOMATICALLY WITH THE DECORATOR

        :return: None
        """

        top_stack = self._scope_recorder.get_event_stack_top()
        if isinstance(top_stack, ScopeCallable):
            try:
                top_stack.set_result(result)
            except AttributeError as e:
                traceback.print_exc()
                print(e)
                exit(1)

        self._scope_recorder.pop_event()

    def get_scope_recorder(self) -> EventRecorder:
        """
        Return the scope recorder object of this algorithm recorder object

        :return: the scope recorder for this object
        """
        return self._scope_recorder

    @_decorator_internal_checker
    def print(self):
        """
        Easy printing because I don't know what to show the user

        :return: None
        """

        # TODO: THIS IS SOME UNIT TESTING SHIT TO SEE IF THE LINKED LIST MATCHES _scope_recorder.get_index_scope_order()
        # current_scope = self._scope_recorder.get_scope_first()
        # counter = 0
        # while current_scope is not None:
        #     print("START")
        #     print(current_scope)
        #     print("END")
        #     print()
        #
        #     current_scope = current_scope.get_scope_following()
        #     # print(current_scope)
        #     counter += 1
        #
        # pprint(self._scope_recorder._list_call_order_scope_complete)
        # print("_list_call_order_scope_complete", len(self._scope_recorder._list_call_order_scope_complete))
        # print("Counter", counter)
        # print("self._scope_recorder.get_index_scope_order()", self._scope_recorder.get_index_scope_order())

        BORDER_AMOUNT = 100
        BORDER_SYMBOL = "#"

        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print("Call order scope Complete")
        print()
        self.scope_recorder_printer.print_call_order_event_complete()
        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print()
        print()

        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print("Call order scope")
        print()
        self.scope_recorder_printer.print_call_order_event()
        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print()
        print()

        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print("Call order scope Simple")
        print()
        self.scope_recorder_printer.print_call_order_event_simple()
        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print()
        print()

        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print("Amount of scopes per scope name")
        print()
        self.scope_recorder_printer.print_amount_events_per_event_name()
        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print()
        print()

        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print("Amount of scopes per scope name + actual scopes used")
        print()
        self.scope_recorder_printer.print_dict_k_name_event_v_events()
        print(BORDER_SYMBOL * BORDER_AMOUNT)
        print()
        print()


if __name__ == '__main__':
    pass
