"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 7/22/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Union, Callable, Any, Dict, Sequence

from python_code_analyzer.functions_common import get_sequence_as_str, get_dict_as_str
from python_code_analyzer.interpretable.event.event_border_callable import EventBorderCallable
from python_code_analyzer.interpretable.event.event_border_start import EventBorderStart


class EventBorderStartScopeCallable(EventBorderStart, EventBorderCallable):

    def __init__(self,
                 callable_object: Callable,
                 callable_args: Sequence[Any] = None,
                 callable_kwargs: Dict[str, Any] = None,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        ######

        """Variables that must be assigned via method calls"""

        # Callable object
        self._callable_object: Union[Callable] = callable_object

        # Callable's args (Note that this does not copy args)
        self._callable_args: Union[Any, None] = callable_args

        # Callable's kwargs (Note that this does not copy kwargs)
        self._callable_kwargs: Union[Any, None] = callable_kwargs

        super().__init__(name, str_id, python_frame_index, dict_recorded_var)

    def get_str_callable_call(self) -> str:
        """
        Mimic the callable's call and arguments in string form

        Notes:
            .strip(", ") is for empty args and kwargs (removes at the beginning and at the end)

        :return:
        """

        return "{}({})".format(self._callable_object.__name__ if self._callable_object is not None else "",
                               ", ".join(
                                   [get_sequence_as_str(self._callable_args),
                                    get_dict_as_str(self._callable_kwargs)
                                    ]).strip(", ")
                               )

    def get_str_pseudo_like(self) -> str:

        str_temp = "{}".format(self.get_str_callable_call())

        if self._dict_recorded_var:
            if str_temp is None or str_temp == "":
                str_temp = "|{}|".format(self.get_str_recorded_var())
            else:
                str_temp = "{} |{}|".format(str_temp, self.get_str_recorded_var())

        str_temp = "{}{}".format(str_temp, super(EventBorderStartScopeCallable, self).get_str_pseudo_like())
        # str_temp = "{}{}".format(str_temp, super(EventBorderStartScopeCallable, self).get_str_pseudo_like())

        return str_temp

    def get_str_formal(self) -> str:
        """

        return string: "{str_base}: {self.get_str_callable_call()}"

        :return:
        """
        str_base = super(EventBorderStartScopeCallable, self).get_str_formal()

        str_formal = "{} {}".format(str_base, self.get_str_callable_call())

        return str_formal
