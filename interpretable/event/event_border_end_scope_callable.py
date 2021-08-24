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
from typing import Any, Union, Dict

from python_code_analyzer.functions_common import get_str_limited
from python_code_analyzer.interpretable.event.event_border_callable import EventBorderCallable
from python_code_analyzer.interpretable.event.event_border_end import EventBorderEnd


class EventBorderEndScopeCallable(EventBorderEnd, EventBorderCallable):

    def __init__(self,
                 callable_return: Union[Any, None] = None,
                 str_id: Union[str, None] = None,
                 name: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, python_frame_index, dict_recorded_var)

        ######

        """Variables that must be assigned via method calls"""

        # Callable's result
        self._callable_return: Union[Any, None] = callable_return

        ######

    def get_callable_return(self) -> Any:
        return self._callable_return

    def get_str_pseudo_like(self):
        return "{} return {}".format(super(EventBorderEndScopeCallable, self).get_str_pseudo_like(),
                                     get_str_limited(self._callable_return))
        # return "{}return {}".format(
        #     super(EventBorderEndScopeCallable, self).get_str_pseudo_like(),
        #     get_str_limited(self._callable_return)
        # )
