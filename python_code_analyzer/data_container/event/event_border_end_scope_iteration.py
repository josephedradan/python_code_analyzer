"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 7/25/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Dict, Any, Union

from python_code_analyzer.data_container.event.event_border_end import EventBorderEnd


class EventBorderEndScopeIteration(EventBorderEnd):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, python_frame_index, dict_recorded_var)
