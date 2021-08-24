"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/16/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from __future__ import annotations

from abc import ABC
from typing import Union, Dict, Any, List

from python_code_analyzer.functions_common import get_dict_as_str
from python_code_analyzer.interpretable.interpretable import Interpretable
from python_code_analyzer.interpretable.scope.scope import Scope


class Event(Interpretable, ABC):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None,
                 python_frame_index: Union[int, None] = None,
                 dict_recorded_var: Union[Dict[str, Any], None] = None
                 ):

        super().__init__(name, str_id, python_frame_index)
        ######

        """Variables set by the recorder"""

        # Event's parent scope
        self._scope_parent: Union[Scope, None] = None

        # Event's previous event
        self._event_previous: Union[Event, None] = None

        # Event's next event
        self._event_next: Union[Event, None] = None

        ######

        # Dict of recorded variables
        self._dict_recorded_var = dict_recorded_var

        ######

    def get_str_formal(self) -> str:
        """

        return string "{str_base}: {kwargs}"

        :return:
        """
        str_base = super(Event, self).get_str_formal()

        str_kwargs_recorded = get_dict_as_str(self._dict_recorded_var)

        str_kwargs_formal = "kwargs:{{{}}}".format(str_kwargs_recorded)

        str_formal = "{} {}".format(str_base, str_kwargs_formal)

        return str_formal

    def get_str_recorded_var(self) -> str:
        """
        Get recorded vars as a string

        :return:
        """
        return get_dict_as_str(self._dict_recorded_var)

    def get_str_pseudo_like(self) -> str:
        """
        Get string representation that looks like pseudocode

        :return:
        """
        str_temp = "{}".format(self.get_name())

        if self._dict_recorded_var:
            if str_temp is None or str_temp == "":
                str_temp = "|{}|".format(self.get_str_recorded_var())
            else:
                str_temp = "{} |{}|".format(str_temp, self.get_str_recorded_var())

        return str_temp

    #####

    def get_scope_parent(self) -> Union[Scope, None]:
        return self._scope_parent

    def auto_set_scope_parent(self, scope: Scope):
        self._scope_parent = scope

    def get_event_previous(self) -> Event:
        return self._event_previous

    def auto_set_event_previous(self, event: Event):
        self._event_previous = event

    def get_event_next(self) -> Event:
        return self._event_next

    def auto_set_event_next(self, event_following: Event) -> None:
        self._event_next = event_following

    # def get_index_stack_frame_callable(self) -> int:
    #     """
    #     Get the index of the scope based on the event_recorder's stack of scopes
    #
    #     :return: the index of the scope based on the stack
    #     """
    #     return self._index_stack_frame_callable
    #
    # def set_index_event_number(self, index: int) -> None:
    #     """
    #     Set the index of self from the event_recorder
    #
    #     """
    #     self._index_event_number = index
    #
    # def set_index_stack(self, index: int) -> None:
    #     """
    #     Set the index in the stack of self from the event_recorder
    #
    #     """
    #     self._index_stack = index
    #
    # def get_index_event_order(self) -> int:
    #     """
    #     Return the index of self from the event_recorder
    #
    #     :return:
    #     """
    #     return self._index_event_number
    #
    # def get_index_stack(self) -> int:
    #     """
    #     Return the index in the stack of self from the event_recorder
    #
    #     :return:
    #     """
    #     return self._index_stack

    def get_kwargs_recorded(self) -> Dict[str, List[Any]]:
        return self._dict_recorded_var
