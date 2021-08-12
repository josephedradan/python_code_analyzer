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

from python_code_analyzer.interpretable.event.event_border_callable import EventBorderCallable
from python_code_analyzer.interpretable.event.event_border_end import EventBorderEnd


class EventBorderEndScopeCallable(EventBorderEnd, EventBorderCallable):

    def __init__(self,
                 callable_return: Union[Any, None] = None,
                 str_id: Union[str, None] = None,
                 name: Union[str, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, dict_recorded_var)

        ######

        """Variables that must be assigned via method calls"""

        # Callable's result
        self._callable_return: Union[Any, None] = callable_return

        ######

    def get_callable_return(self) -> Any:
        return self._callable_return
