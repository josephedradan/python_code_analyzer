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

from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, List, Any


class ScopeEnd(Enum):
    pass


class IterationEnd(ScopeEnd):
    NONE = None
    BREAK = "Break"
    CONTINUE = "Continue"


class CallableEnd(ScopeEnd):
    NONE = None
    RETURN = "Return"


class ScopeContainer:
    def __int__(self):
        self.dict_variables = {}


class Scope(ABC):
    def __init__(self,
                 scope_parent: Union[Scope, None],
                 scope_previous: Union[Scope, None],
                 index_callable_stack_frame_relative: int,
                 index_callable_stack_frame_callable: int,
                 ):
        # Scope's parent
        self._scope_scope_parent: Union[Scope, None] = scope_parent

        # Scope's following
        self._scope_following: Union[Scope, None] = None

        # Scope's previous
        self._scope_previous: Union[Scope, None] = scope_previous

        # Stack frame relative to the scope_recorder
        self._index_callable_stack_frame_relative: int = index_callable_stack_frame_relative

        # Stack frame relative to how many times the callable this scope is in is called
        self._index_callable_stack_frame_callable: int = index_callable_stack_frame_callable

        # Instance variables recorded in this scope in the beginning of the scope
        self._scope_container_start = ScopeContainer()

        # TODO: Instance variables recorded in this scope in the end of the scope (Not used, find a better solution)
        self._scope_container_end = ScopeContainer()

        # Scope set_end type
        self._end: Union[ScopeEnd, None] = None

        # Jump scope order
        self._list_scope_jump_order: List[Scope] = []

        # index of this scope based on the
        self._index_scope: Union[int, None] = None

        self._index_stack_scope: Union[int, None] = None

    def store_variable_start(self, variable_name, variable_value) -> None:
        """
        Add variables and their values into the a storage for recording in the beginning of the scope
        """
        self._scope_container_start.dict_variables[variable_name] = variable_value

    def store_variable_end(self, variable_name, variable_value) -> None:
        """
        Add variables and their values into the a storage for recording in the end of the scope
        """
        self._scope_container_end.dict_variables[variable_name] = variable_value

    def get_index_scope(self) -> int:
        """
        Get the index of this scope. The index is based on the creation of all of the other scopes
        :return: the index of the scope
        """
        return self._index_scope

    def set_index_scope(self, index_given: int) -> None:
        """
        Set the index of this scope. The index is based on teh creation of all of the other scopes

        :param index_given:
        :return:
        """
        self._index_scope = index_given

    def set_index_stack(self, index_given: int) -> None:
        """
        Set the index of the scope based on the scope_recorder's stack of scopes

        :param index_given:
        :return: None
        """
        self._index_stack_scope = index_given

    def get_index_stack(self) -> int:
        """
        Get the index of the scope based on the scope_recorder's stack of scopes

        :return: the index of the scope based on the stack
        """
        return self._index_stack_scope

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

    def get_data(self) -> List[Any]:
        """
        Get base data associated with this scope

        :return:
        """
        return [self._index_callable_stack_frame_relative,
                self._index_callable_stack_frame_callable]

    def get_scope_following(self):
        """


        :return:
        """
        return self._scope_following

    def set_scope_following(self, scope_following: Scope):
        # print("self", self)
        # print("follow", scope_following)
        # print()
        self._scope_following = scope_following

    def add_to_list_scope_jump_order(self, scope_given: Scope):
        self._list_scope_jump_order.append(scope_given)

    def get_list_scope_jump_order(self) -> List[Scope]:
        return self._list_scope_jump_order

    # def __str__(self):
    #     return "Scope: Self: {} Callable: {}".format(self._index_callable_stack_frame_relative,
    #                                                  self._index_callable_stack_frame_callable)

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def __repr__(self):
        return "{}: {}".format(Scope.__name__,
                               "{0}{1:0{2}X}".format("0x", id(self), 16),
                               )


class CallableScope(Scope):

    def __init__(self,
                 scope_parent: Union[Scope, None],
                 scope_previous: Union[Scope, None],
                 index_callable_stack_frame_relative,
                 index_callable_stack_frame_callable,
                 callable_object_current
                 ):
        super().__init__(scope_parent,
                         scope_previous,
                         index_callable_stack_frame_relative,
                         index_callable_stack_frame_callable)

        # For name purposes
        self._callable_object_current = callable_object_current

    def get_data(self):
        list_temp = super().get_data()
        list_temp.extend([self._callable_object_current])
        return list_temp

    def get_name(self):
        """
        Get the name of the scope, names of the scope differ from its hash

        :return:
        """
        return self._callable_object_current.__qualname__

    # def __str__(self):
    #     # return "{}\n{}".format(str(super()), *self.get_data())
    #     return super()

    def __repr__(self):
        return "{}: {}: {}".format(CallableScope.__name__,
                                  "{0}{1:0{2}X}".format("0x", id(self), 16),
                                  self._callable_object_current.__name__)


class IterationScope(Scope):
    def __init__(self,
                 scope_parent: Union[Scope, None],
                 scope_previous: Union[Scope, None],
                 index_callable_stack_frame_relative,
                 index_callable_stack_frame_callable,
                 name_iterable,
                 index_iteration_explicit
                 ):
        super().__init__(scope_parent,
                         scope_previous,
                         index_callable_stack_frame_relative,
                         index_callable_stack_frame_callable)

        self.name_iterable = name_iterable
        self.index_iteration_explicit = index_iteration_explicit

    def get_data(self):
        list_temp = super().get_data()
        list_temp.extend([self.name_iterable, self.index_iteration_explicit])
        return list_temp

    def get_name(self):
        """
        Get the name of the scope, names of the scope differ from its hash

        :return:
        """
        return self.name_iterable

    # def __str__(self):
    #     return "{} IterationScope iter_name: {} index_iter: {}".format(super().__str__(),
    #                                                                    self.name_iterable,
    #                                                                    self.index_iteration_explicit)

    def __repr__(self):
        return "{}: {} {}: {}".format(IterationScope.__name__,
                                     "{0}{1:0{2}X}".format("0x", id(self), 16),
                                     self.name_iterable,
                                     self.index_iteration_explicit)
