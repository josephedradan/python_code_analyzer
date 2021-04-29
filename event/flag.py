"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/19/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Union

from algorithm_analyzer.event.event import Event


class Flag(Event):

    def __init__(self,
                 event_parent: Union[Event, None],
                 event_previous: Union[Event, None],
                 index_stack_frame_event_recorder: int,
                 index_stack_frame_callable: int,
                 flag_name: str,
                 ):
        super().__init__(event_parent,
                         event_previous,
                         index_stack_frame_event_recorder,
                         index_stack_frame_callable)

        self.flag_name = flag_name

    def get_name(self) -> str:
        return "{}".format(self.flag_name)

    def get_str_simple(self) -> str:
        return "{}: {}".format(Flag.__name__, self.flag_name)

    def __str__(self):
        return "{}: {}".format(self._str_helper(Flag, self),
                               self.flag_name)
