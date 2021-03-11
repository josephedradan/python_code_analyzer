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
from typing import List, Union

from algorithm_analyzer.scope import Scope


class ScopeRecorder:
    """
    Records the scopes in which a callable scope or a loop's scope has happened in the order in in which they have
    happened.

    Purpose of recording the scopes and their data is up to you


    """

    def __init__(self):

        # Stack of scopes
        self._stack_scope: List[Scope] = []

        # List of scopes called in order with scope start and scope end (start and end are not explicitly stated)
        self._list_call_order_scope_complete: List[Scope] = []

        # First scope recorded
        self._scope_first: Union[Scope, None] = None

        # Most recently stack popped scope
        self._scope_stack_popped_recent: Union[Scope, None] = None

        # Most recently stack pushed scope
        self._scope_stack_pushed_recent: Union[Scope, None] = None

        # Scope Index counter
        self._index_scope: int = 0

        self._dict_k_name_scope_v_scopes = defaultdict(list)

    def get_scope_stack_top_parent(self) -> Union[Scope, None]:
        """
        From the top scope in the scope stack, get that scope's parent.

        The stack of scopes should mimic the actual scope's position within and around other scopes.

        :return: Scope or None
        """
        return self._stack_scope[-2] if len(self._stack_scope) > 1 else None

    def get_scope_first(self) -> Union[Scope, None]:
        """
        Get the first scope given to self

        :return: Scope or None
        """
        return self._scope_first

    def get_stack_top(self) -> Union[Scope, None]:
        """
        Get the scope from the top of the scope stack

        :return: Scope or None
        """
        return self._stack_scope[-1] if self._stack_scope else None

    def get_call_order_top(self) -> Scope:
        """
        From the call order list, get the most recently added scope

        :return: Scope or None
        """
        return self._list_call_order_scope_complete[-1] if self._list_call_order_scope_complete else None

    def push_scope(self, scope_given: Scope) -> None:
        """
        Push the given scope into the stack of scopes,
        add the given scope into the list of call order scopes,
        and assign the scope for self._scope_stack_pushed_recent.

        :param scope_given: Scope given
        :return: None
        """

        # Assign a scope index number for ordering the scope
        scope_given.set_index_scope(self._index_scope)

        # Assign a stack index number
        scope_given.set_index_stack(len(self._stack_scope))

        # Increment the scope index number
        self._index_scope += 1

        # Assign the first scope in the chain of scopes (Ran once)
        # if not self._stack_scope and not self._list_call_order_scope_complete:
        if self._scope_first is None:
            self._scope_first = scope_given

        # If there are scopes in the stack of scopes then set the top scope's following scope as scope_given
        # if self._list_call_order_scope_complete:  # Old way
        if self._scope_stack_pushed_recent is not None:
            # Set the top scope's following scope as scope_given  # Old way
            # self.get_call_order_top().set_scope_following(scope_given)  # Improper way
            self._scope_stack_pushed_recent.set_scope_following(scope_given)  # Proper way

        # Add scope_given to the stack of scopes
        self._stack_scope.append(scope_given)

        # Add scope_given as the most recently added scope
        self._scope_stack_pushed_recent = scope_given

        # Add scope_given to the call order
        self._list_call_order_scope_complete.append(scope_given)

        # Add scope_given to dict of scope name and the scopes with those names
        self._dict_k_name_scope_v_scopes[scope_given.get_name()].append(scope_given)

    def pop_scope(self) -> Union[Scope, None]:
        """
        Pop the top scope from the stack of scopes.
        Track the popped scope.
        Add the popped scope into the list of call order scopes for properly execution order

        :return: Scope or None
        """
        if not self._stack_scope:
            print("Stack is empty")
            return None

        # Get the popped scope
        stack_popped = self._stack_scope.pop()

        # Assign what is the most recently popped scope
        self._scope_stack_popped_recent = stack_popped

        # Add the popped back to self._list_call_order_scope_complete to indicate that it's been completed
        self._list_call_order_scope_complete.append(stack_popped)
        return stack_popped

    def get_index_scope(self) -> int:
        """
        Get the index of the scope that was pushed to the scope.
        Basically a counter for everytime the self.push_scope() was called.

        *** It should match the amount of scope objects created which is can be found by looping through the linked
        list based on a scopes's following of previous scope***

        :return: index of the scope that w as added from self.push_scope() call
        """
        return self._index_scope

    def print_call_order_scope_complete(self, spacing_multiple=10) -> None:
        """
        Print the list self._list_call_order_scope_complete with formatting based on if your inside the scope or not.

        self._list_call_order_scope_complete contains the complete call order of scopes that you have decided to record
        from the when a scope is entered to when a scope has exited.

        :param spacing_multiple:
        :return:
        """

        # Old Way
        # # Current spacing location
        # location = -1
        #
        # # Set of scopes
        # set_temp = set()
        #
        # # Loop through scopes in self._list_call_order_scope_complete
        # for scope in self._list_call_order_scope_complete:
        #
        #     # Temp string created
        #     str_temp = None
        #
        #     # If the scope is not in the set print format
        #     if scope not in set_temp:
        #         set_temp.add(scope)
        #         location += 1
        #         str_temp = "{}{}".format(" " * location * spacing_multiple, scope)
        #
        #     # If the scope is in th set print format
        #     elif scope in set_temp:
        #         set_temp.remove(scope)
        #         str_temp = "{}{}".format(" " * location * spacing_multiple, scope)
        #         location -= 1
        #
        #     print(str_temp)

        # Loop through scopes in self._list_call_order_scope_complete
        for scope in self._list_call_order_scope_complete:
            str_temp = "{}{}".format(" " * scope.get_index_stack() * spacing_multiple, scope)
            print(str_temp)

    def print_call_order_scope(self, spacing_multiple=10) -> None:
        """
        Print the scopes based on
        TODO: DOCUMENT
        :return:
        """
        scope_current: Scope = self.get_scope_first()

        counter = 0
        while scope_current is not None:
            str_temp = "{}{}".format(" " * scope_current.get_index_stack() * spacing_multiple, scope_current)
            print(str_temp)

            scope_current = scope_current.get_scope_following()

            counter += 1

        # print("Amount of scopes created", self.get_index_scope())
        # print("Amount of scopes created via linked list", counter)

    def print_dict_k_name_scope_v_scopes(self, spacing_multiplier: int = 5) -> None:
        """
        Print the dict containing the scope's name with the amount of scopes per scope name
        and the scopes with those names
        TODO: DOCUMENT
        :return: None
        """

        for key, value in self._dict_k_name_scope_v_scopes.items():
            print("Scope name: {:<20} Amount: {}".format(key, len(value)))
            for scope in value:
                print("{}{}".format(" " * spacing_multiplier, scope))

    def print_amount_scopes_per_scope_name(self):
        """
        Print the dict containing the scope's name with the amount of scopes per scope name
        TODO: DOCUMENT
        :return: None
        """
        for key, value in self._dict_k_name_scope_v_scopes.items():
            print("Scope name: {0:<{1}} Amount: {2}".format(key, 20 if len(key) < 20 else len(key) // 5 * 6,
                                                            len(value)))
