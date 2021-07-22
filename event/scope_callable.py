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
from typing import Union, Any

from python_code_recorder.event.scope import Scope


class ScopeCallable(Scope):

    def __init__(self,
                 event_parent: Union[Scope, None],
                 event_previous: Union[Scope, None],
                 index_callable_stack_frame_scope_recorder,
                 index_callable_stack_frame_callable,
                 callable_object_current,
                 callable_args,
                 callable_kwargs
                 ):
        super().__init__(event_parent,
                         event_previous,
                         index_callable_stack_frame_scope_recorder,
                         index_callable_stack_frame_callable)

        # For name purposes
        self._callable_object_current = callable_object_current
        self._callable_args: Any = callable_args
        self._callable_kwargs: Any = callable_kwargs

        self._callable_result: Any = None

    def set_result(self, result):
        self._callable_result = result

    def get_result(self):
        return self._callable_result

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

    def __str__(self):
        """
        Type, Address (Cpython), callable name

        :return:
        """
        address_hex = "{0}{1:0{2}X}".format("0x", id(self), 16)

        return "{}: {}: {}".format(ScopeCallable.__name__,
                                   address_hex,
                                   self._callable_object_current.__name__)

    def get_str_simple(self):
        """
        Mimic the callable's call and arguments

        Notes:
            .strip(", ") is for empty args and kwargs (removes at the beginning and at the end)

        :return:
        """
        return "{}({})".format(self._callable_object_current.__name__,
                               ", ".join([", ".join([f"\"{i}\"" if isinstance(i, str) else str(i) for i in
                                                     self._callable_args]) if self._callable_args else "", ", ".join(
                                   [f"{i[0]}=\"{i[1]}\"" if isinstance(i[1], str) else f"{i[0]}={i[1]}" for i in
                                    self._callable_kwargs.items()]) if self._callable_kwargs else ""]).strip(", ")
                               )
