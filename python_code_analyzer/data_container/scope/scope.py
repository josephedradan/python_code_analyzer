"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/12/2021

Purpose:
    Scope of something that can have a scope like a function or a loop's iteration

Details:

Description:

Notes:

IMPORTANT NOTES:
    Scopes are just containers of events, they should not contain anything else but events and data about the
    scope.

Explanation:

Reference:

"""
from __future__ import annotations

from abc import ABC
from typing import Union, List, TYPE_CHECKING

from python_code_analyzer.data_container.data_container import DataContainer

if TYPE_CHECKING:
    from python_code_analyzer.data_container.event.event import Event
    from python_code_analyzer.data_container.event.event_border_end import EventBorderEnd
    from python_code_analyzer.data_container.event.event_border_start import EventBorderStart


class Scope(DataContainer, ABC):
    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None
                 ):
        """

        :param name: Name of the data
        :param str_id:
        """
        super(Scope, self).__init__(name, str_id)
        ######

        """Variables that must be assigned via method calls"""

        # TODO: Event and Scope require a parent Scope, no code optimizations known at this time to reduce commonality
        # Scope's parent scope
        self._scope_parent: Union[Scope, None] = None

        # Scope's Border Start
        self._event_border_start: Union[EventBorderStart, None] = None

        # Scope's Border End
        self._event_border_end: Union[EventBorderEnd, None] = None

        ######

        # Order of recorded events called in this scope
        self._list_event: List[Event] = []

    ######

    def get_str_pseudo_like(self):
        str_temp = "{}".format(self.get_name())
        #
        # if self._dict_recorded_var:
        #     str_temp = "{} |{}|".format(str_temp, get_dict_as_str(self._dict_recorded_var))

        return str_temp

    ######
    def get_scope_parent(self) -> Union[Scope, None]:
        return self._scope_parent

    def auto_set_scope_parent(self, scope: Scope) -> None:
        """
        Should be assigned by recorder

        :param scope:
        :return:
        """
        self._scope_parent = scope

    def get_event_border_start(self) -> Union[EventBorderStart, None]:
        return self._event_border_start

    def auto_set_event_border_start(self, event_border_start: EventBorderStart) -> None:
        """
        Should be assigned by recorder

        :param event_border_start:
        :return:
        """
        self._event_border_start = event_border_start

    def get_event_border_end(self) -> Union[EventBorderEnd, None]:
        return self._event_border_end

    def auto_set_event_border_end(self, event_border_end: EventBorderEnd) -> None:
        """
        Should be assigned by recorder

        :param event_border_end:
        :return:
        """
        self._event_border_end = event_border_end

    ######

    def add_event_to_list_event(self, scope_given: Event):
        self._list_event.append(scope_given)
