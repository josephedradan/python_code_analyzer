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
from collections import defaultdict
from typing import List, Union, Dict

from algorithm_analyzer.event.event import Event


class EventRecorder:
    """
    Records the events in which a callable event or a loop's event has happened in the order in in which they have
    happened.

    Purpose of recording the events and their data is up to you


    """

    def __init__(self):

        # Stack of events
        self._stack_event: List[Event] = []

        # List of events called in order with event start and event end (start and end are not explicitly stated)
        self._list_call_order_event_complete: List[Event] = []

        # List of events called in order using only the event start
        self._list_call_order_event: List[Event] = []

        # First event recorded
        self._event_first: Union[Event, None] = None

        # Most recently stack popped event
        self._event_stack_popped_recent: Union[Event, None] = None

        # Most recently stack pushed event
        self._event_stack_pushed_recent: Union[Event, None] = None

        # Event Index counter (It's a generic counter for how many things are in the stack)
        self._index_event: int = 0

        # Name of the event with list of Events
        self._dict_k_name_event_v_events: Dict[str, List[Event]] = defaultdict(list)

    def get_event_stack_top_parent(self) -> Union[Event, None]:
        """
        From the top event in the event stack, get that event's parent.

        The stack of events should mimic the actual event's position within and around other events.

        :return: Event or None
        """
        return self._stack_event[-2] if len(self._stack_event) > 1 else None

    def get_event_stack_top(self) -> Union[Event, None]:
        """
        Get the event from the top of the event stack

        :return: Event or None
        """
        return self._stack_event[-1] if self._stack_event else None

    def get_event_first(self) -> Union[Event, None]:
        """
        Get the first event given to self

        :return: Event or None
        """
        return self._event_first

    def get_call_order_top(self) -> Event:
        """
        From the call order list, get the most recently added event

        :return: Event or None
        """
        return self._list_call_order_event_complete[-1] if self._list_call_order_event_complete else None

    def push_event(self, event_given: Event) -> None:
        """
        Push the given event into the stack of events,
        add the given event into the list of call order events,
        and assign the event for self._event_stack_pushed_recent.

        :param event_given: Event given
        :return: None
        """

        # Assign a event index number for ordering the event
        event_given.set_index_event_order(self._index_event)

        # Assign a stack index number
        event_given.set_index_stack(len(self._stack_event))

        # Increment the event index number
        self._index_event += 1

        # Assign the first event in the chain of events (Ran once)
        # if not self._stack_event and not self._list_call_order_event_complete:
        if self._event_first is None:
            self._event_first = event_given

        # If there are events in the stack of events then set the top event's following event as event_given
        # if self._list_call_order_event_complete:  # Old way
        if self._event_stack_pushed_recent is not None:
            # Set the top event's following event as event_given  # Old way
            # self.get_call_order_top().set_event_following(event_given)  # Improper way
            self._event_stack_pushed_recent.set_event_following(event_given)  # Proper way

        # Add event_given to the stack of events
        self._stack_event.append(event_given)

        # Add event_given as the most recently added event
        self._event_stack_pushed_recent = event_given

        # Add event_given to the call order complete
        self._list_call_order_event_complete.append(event_given)

        # Add event_given to the call order
        self._list_call_order_event.append(event_given)

        # Add event_given to dict of event name and the events with those names
        self._dict_k_name_event_v_events[event_given.get_name()].append(event_given)

    def pop_event(self) -> Union[Event, None]:
        """
        Pop the top event from the stack of events.
        Track the popped event.
        Add the popped event into the list of call order events for properly execution order

        :return: Event or None
        """
        if not self._stack_event:
            print("Stack is empty")
            return None

        # Decrement the event index number (DO NOT DO OR YOU WILL MATCH THE STACK INDEX)
        # self._index_event -= 1

        # Get the popped event
        stack_popped = self._stack_event.pop()

        # Assign what is the most recently popped event
        self._event_stack_popped_recent = stack_popped

        # Add the popped back to self._list_call_order_event_complete to indicate that it's been completed
        self._list_call_order_event_complete.append(stack_popped)
        return stack_popped

    def get_index_event(self) -> int:
        """
        Get the index of the event that was pushed to the event.
        Basically a counter for everytime the self.push_event() was called.

        *** It should match the amount of event objects created which is can be found by looping through the linked
        list based on a events's following of previous event***

        :return: index of the event that w as added from self.push_event() call
        """
        return self._index_event

    def get_stack_event(self) -> List[Event]:
        return self._stack_event

    def get_list_call_order_event_complete(self) -> List[Event]:
        return self._list_call_order_event_complete

    def get_list_call_order_event(self):
        """

        :return:
        :rtype:
        """
        return self._list_call_order_event

    def get_dict_k_name_event_v_events(self) -> Dict[str, List[Event]]:
        return self._dict_k_name_event_v_events
