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

Explanation:

Reference:

"""
from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import Union, List, Any

from python_code_recorder.event.event import Event


class ScopeEnd(Enum):
    pass


class IterationEnd(ScopeEnd):
    NONE = None
    BREAK = "Break"
    CONTINUE = "Continue"


class Scope(Event, ABC):
    def __init__(self,
                 event_parent: Union[Event, None],
                 event_previous: Union[Event, None],
                 index_callable_stack_frame_scope_recorder: int,
                 index_callable_stack_frame_callable: int,
                 ):
        super().__init__(
            event_parent,
            event_previous,
            index_callable_stack_frame_scope_recorder,
            index_callable_stack_frame_callable)

        # Scope set_end type
        self._end: Union[ScopeEnd, None] = None

        # Jump scope order
        self._list_scope_jump_order: List[Scope] = []

        # index of this scope in the order it was called
        self._index_scope_order: Union[int, None] = None

        # index of the scope stack
        self._index_stack_scope: Union[int, None] = None

    def get_data(self) -> List[Any]:
        """
        Get base data associated with this scope
        TODO FIX ME NOT SPECIFIC
        :return:
        """
        return [self._list_scope_jump_order,
                self._index_stack_frame_callable]

    def add_to_list_scope_jump_order(self, scope_given: Scope):
        self._list_scope_jump_order.append(scope_given)

    def get_list_scope_jump_order(self) -> List[Scope]:
        return self._list_scope_jump_order
