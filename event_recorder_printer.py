"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/13/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import List

from algorithm_analyzer.event.event import Event
from algorithm_analyzer.event_recorder import EventRecorder


class EventRecorderPrinter:

    def __init__(self, event_recorder: EventRecorder):
        self.event_recorder = event_recorder

        # Stack of events
        self._stack_event: List[Event] = self.event_recorder.get_stack_event()

        # List of events called in order with event start and event end (start and end are not explicitly stated)
        self._list_call_order_event_complete: List[Event] = self.event_recorder.get_list_call_order_event_complete()

    def print_call_order_event_complete(self, spacing_multiple=10) -> None:
        """
        Print the list self._list_call_order_event_complete with formatting based on if your inside the event or not.

        self._list_call_order_event_complete contains the complete call order of events that you have decided to record
        from the when a event is entered to when a event has exited.

        Example:
            CallableEvent: 0x00000149C677E040: func
                      IterationEvent: 0x00000149C677E0A0 i: 1
                                IterationEvent: 0x00000149C67C9D30 j: 2
                                          IterationEvent: 0x00000149C67D4250 k: 3
                                          IterationEvent: 0x00000149C67D4250 k: 3
                                          IterationEvent: 0x00000149C67D42E0 k: 4
                                          IterationEvent: 0x00000149C67D42E0 k: 4
                                IterationEvent: 0x00000149C67C9D30 j: 2
                                IterationEvent: 0x00000149C67D4370 j: 3
                                          IterationEvent: 0x00000149C67D4400 k: 4
                                          IterationEvent: 0x00000149C67D4400 k: 4
                                IterationEvent: 0x00000149C67D4370 j: 3
                      IterationEvent: 0x00000149C677E0A0 i: 1
                      IterationEvent: 0x00000149C67D4490 i: 2
                                IterationEvent: 0x00000149C67D4520 j: 3
                                          IterationEvent: 0x00000149C67D45B0 k: 4
                                          IterationEvent: 0x00000149C67D45B0 k: 4
                                IterationEvent: 0x00000149C67D4520 j: 3
                      IterationEvent: 0x00000149C67D4490 i: 2
            CallableEvent: 0x00000149C677E040: func

        :param spacing_multiple:
        :return:
        """

        # Old Way
        # # Current spacing location
        # location = -1
        #
        # # Set of events
        # set_temp = set()
        #
        # # Loop through events in self._list_call_order_event_complete
        # for event in self._list_call_order_event_complete:
        #
        #     # Temp string created
        #     str_temp = None
        #
        #     # If the event is not in the set print format
        #     if event not in set_temp:
        #         set_temp.add(event)
        #         location += 1
        #         str_temp = "{}{}".format(" " * location * spacing_multiple, event)
        #
        #     # If the event is in th set print format
        #     elif event in set_temp:
        #         set_temp.remove(event)
        #         str_temp = "{}{}".format(" " * location * spacing_multiple, event)
        #         location -= 1
        #
        #     print(str_temp)

        # Loop through events in self._list_call_order_event_complete
        for event in self._list_call_order_event_complete:
            str_temp = "{}{}".format(" " * event.get_index_stack() * spacing_multiple, event)
            print(str_temp)

    def print_call_order_event(self, spacing_multiplier=10) -> None:
        """
        Prints all the events with indenting to signify the callable stack

        Example:
            CallableEvent: 0x00000267484BDBE0: func
                      IterationEvent: 0x00000267484BDB20 i: 1
                                IterationEvent: 0x00000267CACA9EB0 j: 2
                                          IterationEvent: 0x00000267CACA9F70 k: 3
                                          IterationEvent: 0x00000267CACA9EE0 k: 4
                                IterationEvent: 0x00000267CACB60A0 j: 3
                                          IterationEvent: 0x00000267CACB6130 k: 4
                      IterationEvent: 0x00000267CACB61C0 i: 2
                                IterationEvent: 0x00000267CACB6280 j: 3
                                          IterationEvent: 0x00000267CACB62E0 k: 4

        :param spacing_multiplier:
        :return: None
        """
        # Alternative
        # event_current: Event = self.event_recorder.get_event_first()
        #
        # counter = 0
        # while event_current is not None:
        #     str_temp = "{}{}".format(" " * event_current.get_index_stack() * spacing_multiplier, event_current)
        #     print(str_temp)
        #
        #     event_current = event_current.get_event_following()
        #
        #     counter += 1

        for event_current in self.event_recorder.get_list_call_order_event():
            str_temp = "{}{}".format(" " * event_current.get_index_stack() * spacing_multiplier, event_current)
            print(str_temp)

        # print("Amount of events created", self.get_index_event_order())
        # print("Amount of events created via linked list", counter)

    def print_call_order_event_simple(self, spacing_multiplier=10, len_name_args_kwargs=None):
        """

        :param spacing_multiplier:
        :return:
        """

        # for k, v in self.event_recorder.get_dict_k_name_event_v_events().items():

        for event_current in self.event_recorder.get_list_call_order_event():
            str_temp = "{}{}".format(" " * event_current.get_index_stack() * spacing_multiplier,
                                     event_current.get_str_simple())
            print(str_temp)

    def print_dict_k_name_event_v_events(self, spacing: int = 20, spacing_multiplier: int = 5) -> None:
        """
        Print the dict containing the event's name with the amount of events per event name
        and the events with those names

        Example:
            Event name: func                 Amount of events: 1
                 CallableEvent: 0x000001CFCF22EBE0: func
            Event name: i                    Amount of events: 4
                 IterationEvent: 0x000001CFCF22EB20 i: 1
                 IterationEvent: 0x000001D0499F5760 i: 2
                 IterationEvent: 0x000001D0499F5D00 i: 3
                 IterationEvent: 0x000001D0499F7070 i: 4


        :param spacing:
        :param spacing_multiplier:
        :return:
        """

        for key, value in self.event_recorder.get_dict_k_name_event_v_events().items():
            print("Event name: {0:<{1}} Amount of events: {2}".format(key, spacing if len(key) < spacing else len(
                key) // 5 * 6, len(value)))
            for event in value:
                print("{}{}".format(" " * spacing_multiplier, event))

    def print_amount_events_per_event_name(self, spacing: int = 20):
        """
        Print the dict containing the event's name with the amount of events per event name

        Example:
            Event name: func                 Amount of events: 1
            Event name: i                    Amount of events: 4
            Event name: j                    Amount of events: 10
            Event name: k                    Amount of events: 20

        :param spacing:
        :return: None
        """
        for key, value in self.event_recorder.get_dict_k_name_event_v_events().items():
            print("Event name: {0:<{1}} Amount of events: {2}".format(key, spacing if len(key) < spacing else len(
                key) // 5 * 6, len(value)))
