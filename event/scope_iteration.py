"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 4/2/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Union

from python_code_recorder.event.scope import ScopeEnd, Scope


class ScopeIteration(Scope):

    def __init__(self,
                 event_parent: Union[Scope, None],
                 event_previous: Union[Scope, None],
                 index_callable_stack_frame_scope_recorder,
                 index_callable_stack_frame_callable,
                 name_iterable,
                 index_iteration_explicit
                 ):
        super().__init__(event_parent,
                         event_previous,
                         index_callable_stack_frame_scope_recorder,
                         index_callable_stack_frame_callable)

        self.name_iterable = name_iterable
        self.index_iteration_explicit = index_iteration_explicit

    def get_data(self):
        """
        TODO ADD DOC

        :return:
        """

        list_temp = super().get_data()
        list_temp.extend([self.name_iterable, self.index_iteration_explicit])
        return list_temp

    def get_name(self):
        """
        Get the name of the scope, names of the scope differ from its hash

        :return:
        """
        return self.name_iterable

    def get_end(self) -> Union[ScopeEnd, None]:
        """
        Get the end call enum of the scope

        :return:
        """
        return self._end

    def set_end(self, end_given: ScopeEnd) -> None:
        """
        Get the end call enum of the scope

        :param end_given:
        :return: ScopeEnd
        """
        self._end = end_given

    def __str__(self):
        return "{} {}: {}".format(self._str_helper(ScopeIteration, self),
                                  self.name_iterable,
                                  self.index_iteration_explicit)

    def get_str_simple(self) -> str:
        return "{}: {}".format(self.name_iterable, self.index_iteration_explicit)
