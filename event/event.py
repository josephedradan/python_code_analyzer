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

from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Union, Dict, Any, List


class Event(ABC):
    def __init__(self,
                 event_parent: Union[Event, None],
                 event_previous: Union[Event, None],
                 index_stack_frame_event_recorder: int,
                 index_stack_frame_callable: int,
                 ):
        # Event's parent
        self._event_parent: Union[Event, None] = event_parent

        # Event's following
        self._event_following: Union[Event, None] = None

        # Event's previous
        self._event_previous: Union[Event, None] = event_previous

        # Index of the Stack frame relative to the event_recorder
        self._index_stack_frame_event_recorder: int = index_stack_frame_event_recorder

        # Index of the Stack frame relative to how many times the callable this event is in is called
        self._index_stack_frame_callable: int = index_stack_frame_callable

        # Instance variables recorded in this scope
        self._dict_k_varaible_name_v_variable_value = defaultdict(list)

        # Index of the event in order
        self._index_event_order: Union[int, None] = None

        # Index of the event in the stack
        self._index_stack: Union[int, None] = None

        #####################

    def get_event_following(self) -> Event:
        """
        Get the following event

        :return:
        """
        return self._event_following

    def set_event_following(self, event_following: Event) -> None:
        """
        Set the following event object after self

        """
        self._event_following = event_following

    def get_index_stack_frame_event_recorder(self) -> int:
        """
        Get the index of this scope. The index is based on the creation of all of the other scopes
        :return: the index of the scope
        """
        return self._index_stack_frame_event_recorder

    def get_index_stack_frame_callable(self) -> int:
        """
        Get the index of the scope based on the event_recorder's stack of scopes

        :return: the index of the scope based on the stack
        """
        return self._index_stack_frame_callable

    def set_index_event_order(self, index: int) -> None:
        """
        Set the index of self from the event_recorder

        """
        self._index_event_order = index

    def set_index_stack(self, index: int) -> None:
        """
        Set the index in the stack of self from the event_recorder

        """
        self._index_stack = index

    def get_index_event_order(self) -> int:
        """
        Return the index of self from the event_recorder

        :return:
        """
        return self._index_event_order

    def get_index_stack(self) -> int:
        """
        Return the index in the stack of self from the event_recorder

        :return:
        """
        return self._index_stack

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_str_simple(self) -> str:
        pass

    def record_variable(self, variable_name, variable_value) -> None:
        """
        Add variables and their values into the a storage for recording in the beginning of the scope

        Notes:
            If an object was passed then a reference is passed...

        """
        self._dict_k_varaible_name_v_variable_value[variable_name].append(variable_value)

    def get_dict_k_variable_name_v_variable_value(self) -> Dict[str, List[Any]]:
        """
        Get recorded variables dict

        """
        return self._dict_k_varaible_name_v_variable_value

    @abstractmethod
    def __str__(self):
        return self._str_helper(Event, self)

    def _str_helper(self, class_current, self_current):
        return "{}: {}".format(class_current.__name__,
                               "{0}{1:0{2}X}".format("0x", id(self_current), 16),
                               )
