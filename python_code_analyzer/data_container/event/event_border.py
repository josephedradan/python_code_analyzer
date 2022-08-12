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

from python_code_analyzer.data_container.event.event import Event
from python_code_analyzer.data_container.scope.scope import Scope


class EventBorder(Event, ABC):
    """
    Abstract EventBoarder class

    """

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):
        super().__init__(name, str_id,python_frame_index,  dict_recorded_var)

        ######

        """Variables that must be assigned via method calls"""

        # The Scope that this EventBoarder represents
        self._scope_related: Union[Scope, None] = None

    def set_scope_part_of(self, scope_related: Scope):
        self._scope_related = scope_related

    def get_scope_part_of(self) -> Scope:
        return self._scope_related


