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

from python_code_analyzer.interpretable.event.event_border import EventBorder


class EventBorderStart(EventBorder, ABC):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, python_frame_index, dict_recorded_var)

    def get_str_pseudo_like(self) -> str:
        return "{} {{".format(super(EventBorderStart, self).get_str_pseudo_like())
        # return "{}:".format(super(EventBorderStart, self).get_str_pseudo_like())
