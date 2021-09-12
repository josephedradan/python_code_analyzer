"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/12/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from python_code_analyzer.interpretable.event.event import Event
from python_code_analyzer.interpretable.event.event_border_end import EventBorderEnd
from python_code_analyzer.interpretable.event.event_border_end_scope_callable import EventBorderEndScopeCallable
from python_code_analyzer.interpretable.event.event_border_end_scope_outer import EventBorderEndScopeOuter
from python_code_analyzer.interpretable.event.event_border_start import EventBorderStart
from python_code_analyzer.interpretable.event.event_border_start_scope_callable import EventBorderStartScopeCallable
from python_code_analyzer.interpretable.event.event_border_start_scope_iteration import EventBorderStartScopeIteration
from python_code_analyzer.interpretable.scope.scope import Scope
from python_code_analyzer.interpretable.scope.scope_callable import ScopeCallable
from python_code_analyzer.interpretable.scope.scope_iteration import ScopeIteration
from python_code_analyzer.interpretable.scope.scope_outer import ScopeOuter
from typing import List, Union


class InterpretableRecorder:
    """
    Records Interpretable objects in which a Interpretable object has happened in the order in in which they have
    happened.

    Purpose of recording the events and their data is up to you

    Notes:
        This should not be accessible to the user

    """

    def __init__(self):
        """
        Initialize the InterpretableRecorder

        """

        """Scope Stack"""

        # Stack of scopes (This should mimic the call stack frames)
        self._stack_scope: List[Scope] = []

        """Event List"""

        # List of events called in order with event start and event end (start and end are not explicitly stated)
        self._list_event_order: List[Event] = []

        """Scope List"""

        self._list_scope_order: List[Scope] = []

        """Scope Stack Recent Push/Pop"""

        self._scope_stack_scope_popped_recent: Union[Scope, None] = None

        # self._scope_stack_scope_pushed_recent: Union[Scope, None] = None

        """Scope Callable"""

        self._stack_frame_number: int = 1

        """
        Initialize starting
        """
        scope_outer = ScopeOuter()

        self._stack_scope.append(scope_outer)

        self._scope_stack_scope_pushed_recent = scope_outer

    """Event"""

    def get_event_first(self) -> Union[Event, None]:
        """
        Get the first event given to self

        :return: Event or None
        """
        return self._list_event_order[0] if self._list_event_order else None

    def get_event_list_event_order_top(self) -> Union[Event, None]:
        """
        From the call order list, get the most recently added event

        :return: Event or None
        """
        return self._list_event_order[-1] if self._list_event_order else None

    """Scope Stack"""

    def get_scope_stack_scope_top_parent(self) -> Union[Scope, None]:
        """
        Get the Parent Event of the most recent Event

        :return: Event or None
        """
        return self._stack_scope[-2] if len(self._stack_scope) > 1 else None

    def get_scope_stack_scope_top(self) -> Union[Scope, None]:
        return self._stack_scope[-1] if self._stack_scope else None

    def get_scope_first(self) -> Union[Scope, None]:
        """
        Get the first event given to self

        :return: Event or None
        """
        return self._list_scope_order[0] if self._list_scope_order else None

    def get_scope_list_event_order_top(self) -> Union[Scope, None]:
        """
        From the call order list, get the most recently added event

        :return: Event or None
        """
        return self._list_scope_order[-1] if self._list_scope_order else None

    def get_stack_frame_number(self) -> int:
        return self._stack_frame_number

    def get_scope_number(self) -> int:
        return len(self._stack_scope)

    """Scope Stack Push/Pop"""

    def _push_scope(self, event_border_start_given: EventBorderStart) -> None:
        """

        1. Set Scope to most recent push
        2. Add Scope to Scope Stack

        :return:
        """

        # scope_new: Union[Scope, None] = None

        if isinstance(event_border_start_given, EventBorderStartScopeIteration):
            scope_new = ScopeIteration("{} {}".format(event_border_start_given.get_name(), "(Iteration Scope)"))
        elif isinstance(event_border_start_given, EventBorderStartScopeCallable):
            scope_new = ScopeCallable("{} {}".format(event_border_start_given.get_name(), "(Callable Scope)"))
            self._stack_frame_number += 1
        elif isinstance(event_border_start_given, EventBorderEndScopeOuter):
            scope_new = ScopeOuter("{} {}".format(event_border_start_given.get_name(), "(Outer Scope)"))
        else:
            raise Exception(
                "No appropriate scope created for given EventBorderStart: {}".format(event_border_start_given))

        ######

        event_border_start_given.set_scope_part_of(scope_new)

        ######

        # Assign scope_new's Stack frame number
        scope_new.auto_set_stack_frame_number(self.get_stack_frame_number())

        # Assign scope_new's parent scope
        scope_new.auto_set_scope_parent(self._scope_stack_scope_pushed_recent)

        # Assign scope_new's event border start
        scope_new.auto_set_event_border_start(event_border_start_given)

        ######

        self._list_scope_order.append(scope_new)

        self._stack_scope.append(scope_new)

    def _pop_scope(self, event_border_end_given: EventBorderEnd):
        """

        1. Pop the current stack scope and assign it the most recent scope popped
        (self._scope_stack_scope_popped_recent)

        :return:
        """
        scope_popped = self._stack_scope.pop()

        """
        Special case that if you exited a scope created from an EventBorderStartScopeIteration via return,
        then you need to properly pop from self._stack_scope to get the scope 
        """
        if isinstance(event_border_end_given, EventBorderEndScopeCallable):
            while True:
                if isinstance(scope_popped, ScopeCallable):
                    self._stack_frame_number -= 1
                    break

                scope_popped = self._stack_scope.pop()

        ######

        event_border_end_given.set_scope_part_of(scope_popped)

        ######

        scope_popped.auto_set_event_border_end(event_border_end_given)

        ######

        self._scope_stack_scope_popped_recent = scope_popped

        # FIXME: Not necessary
        return self._scope_stack_scope_popped_recent

    """Stack Event (Add event)"""

    def add_event(self, event_given: Event) -> None:
        """
        1. Push the given event into the stack of events,
        2. Add the given event into self._list_order_event and self._list_event_order_complete,
        and set the event as self._event_stack_pushed_recent.

        :param event_given: Event given
        :return: None
        """

        ######

        if isinstance(event_given, EventBorderEnd):
            self._pop_scope(event_given)

        ######

        # Assign event_given's stack index number
        event_given.auto_set_stack_frame_number(self.get_stack_frame_number())

        # Assign event_given's scope index
        event_given.auto_set_scope_number(self.get_scope_number())

        # Assign event_given's parent Scope
        event_given.auto_set_scope_parent(self._scope_stack_scope_pushed_recent)

        # Assign event_given's previous Scope
        event_given.auto_set_event_previous(self.get_event_list_event_order_top())

        # Assign event_previous' event's next event
        if self.get_event_list_event_order_top() is not None:
            self.get_event_list_event_order_top().auto_set_event_next(event_given)

        ######

        # Push event_given to the list of events in order
        self._list_event_order.append(event_given)

        ######

        if isinstance(event_given, EventBorderStart):
            self._push_scope(event_given)

    def get_list_event(self) -> List[Event]:
        """
        List of events with the proper exit event
        :return:
        """
        return self._list_event_order
