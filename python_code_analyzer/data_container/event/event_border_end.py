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
from abc import ABC
from typing import Union, Dict, Any

from python_code_analyzer.data_container.event.event_border import EventBorder


class EventBorderEnd(EventBorder, ABC):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, python_frame_index, dict_recorded_var)

    # def set_scope_part_of(self, scope_related: Scope):
    #     super(EventBorderEnd, self).set_scope_part_of(scope_related)
    #
    #     """
    #     If this object has no name because it's an EventBorderEnd to a EventBorderStart,
    #     then this object will have the same name as its EventBorderStart counterpart.
    #     """
    #     if self._name is None:
    #         self._name = self.get_scope_part_of().get_event_border_start().get_name()

    def get_str_pseudo_like(self):
        return "}"
        # return ""
