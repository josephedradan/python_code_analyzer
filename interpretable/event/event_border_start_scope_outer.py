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
from typing import Union, Dict, Any

from python_code_analyzer.interpretable.event.event_border_start import EventBorderStart


class EventBorderStartScopeOuter(EventBorderStart):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id, dict_recorded_var)
