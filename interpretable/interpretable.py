"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 7/22/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from __future__ import annotations

import inspect
from abc import ABC
from collections import defaultdict
from typing import List, Union, Sequence, Dict

from python_code_analyzer.interpretable.data_common import DataCommon


class Interpretable(DataCommon, ABC):
    # Dict Key of the name of the Interpretable type that has a value of a list of those specific types of objects
    _dict_k_type_qualname_v_list_type_self: Dict[str, List[Interpretable]] = defaultdict(list)

    # List of objects of the type Interpretable
    _list_object_of_type_interpretable: List[Interpretable] = []

    """
    Tuple ID based on all the python frames associated with the creation of the interpretable using the frame's source 
    code's line number in a tuple

    Notes:
        This tuple ID allows you identify objects created on the same line number in source code.

    """
    _dict_k_tuple_id_line_number_v_list_interpretable: Dict[Sequence[int], List[Interpretable]] = defaultdict(list)

    # Dict where the key is the object's string id and the value is the list of objects that have that same string id
    _dict_k_str_id_v_list_interpretable: Dict[str, List[Interpretable]] = defaultdict(list)

    # Dict where the key is the object's name and the value is the list of objects that have that same name
    _dict_k_name_v_list_interpretable: Dict[str, List[Interpretable]] = defaultdict(list)

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None
                 ):
        super(Interpretable, self).__init__(name, str_id)

        ######

        """Variables are automatically assigned abd are meta programming related"""

        # Assign the type call number as the int instantiated number (Unique based on class)
        self._call_number_type: Union[int, None] = None

        # Assign self._interpretable_number as the int instantiated number (Any object that inherits from Interpretable)
        self._call_number_interpretable: Union[int, None] = None

        # Assign Tuple id based on the python frame source code line numbers
        self._tuple_id_line_number: Union[Sequence[int], None] = None

        """
        Call number is based on how many objects are in the appropriate tuple id's list of interpretables in 
        _dict_k_tuple_id_line_number_v_list_interpretable
        """
        self._call_number_tuple_id_line_number: Union[int, None] = None

        # Call number based on name
        self._call_number_name: Union[int, None] = None

        # Call number based on str id
        self._call_number_str_id: Union[int, None] = None

        ######

        """Initializing variable"""

        # Add self to appropriate class' _list_object_of_type_self (Unique based on class)
        Interpretable._handle_self_to_dict_k_type_qualname_v_list_type_self(self)

        # Add self to _list_object_of_type_interpretable (Any object that inherits from Interpretable)
        Interpretable._add_self_to_list_object_of_type_interpretable(self)

        # Handle self's id_tuple_line_number
        Interpretable._handle_tuple_id_line_number(self)

        # Handle self's name
        Interpretable._handle_dict_k_name_v_list_interpretable(self)

        # Handle self's string id
        Interpretable._handle_dict_k_str_id_v_list_interpretable(self)

        ######

    """The below are methods associated with meta programming"""

    @classmethod
    def _handle_self_to_dict_k_type_qualname_v_list_type_self(cls, self: Interpretable) -> None:
        """
        1. Add self to cls._dict_k_type_qualname_v_list_type_self where the key is the __qualname__ of class of self
        and the value is a list of objects of type(self)
        2. Assign self._call_number_type based on the length of the list for type(self).__qualname__ from the dict

        :return:
        """

        cls._dict_k_type_qualname_v_list_type_self[type(self).__qualname__].append(self)

        self._call_number_type = len(cls._dict_k_type_qualname_v_list_type_self[type(self).__qualname__])

    @classmethod
    def _add_self_to_list_object_of_type_interpretable(cls, self: Interpretable) -> None:
        """
        1. Add the self object to list of objects of the subclass of Interpretable
        2. Assign self._interpretable_number based on the current length of the list

        :param self:
        :return:
        """
        cls._list_object_of_type_interpretable.append(self)

        self._call_number_interpretable = len(self._list_object_of_type_interpretable)

    @classmethod
    def _handle_tuple_id_line_number(cls, self: Interpretable) -> None:
        """
        Handle the creation and setup for the tuple ID

        1. Setup the tuple ID
        2. Add self to the dict where key is the tuple id and the value is the list of interpretables of type(self)
        3. Setup self's call number (Recall that this number is based on the amount of times the source code on the same
        line has been executed)

        :param self:
        :return:
        """

        # Setup tuple ID
        self._set_tuple_id_line_number()

        # Ease of use for a tuple ID
        tuple_id = self.get_tuple_id_line_number()

        # Add self to _dict_k_tuple_id_line_number_v_list_interpretable
        cls._dict_k_tuple_id_line_number_v_list_interpretable[tuple_id].append(self)

        # Setup self's tuple ID call number
        self._call_number_tuple_id_line_number = len(
            cls._dict_k_tuple_id_line_number_v_list_interpretable[self.get_tuple_id_line_number()])

    def _set_tuple_id_line_number(self) -> None:
        """
        Set up a tuple of numbers

        1. Call inspect.currentframe() to get the current python frame
        1a. Get current frame's source code line number and put it into a list
        1b. Replace the current frame with the next frame via .f_back member
        1c. Repeat 1a, 1b and 1c until their are more frames
        2. use those frames to get their line number in code
        3. Put those line numbers in a tuple

        :return:
        """
        frame_current = inspect.currentframe()

        list_id_temp = []

        while frame_current is not None:
            list_id_temp.append(frame_current.f_lineno)
            frame_current = frame_current.f_back

        self._tuple_id_line_number = tuple(list_id_temp)

    @classmethod
    def _handle_dict_k_str_id_v_list_interpretable(cls, self: Interpretable):
        """
        1. Add self to dict where the key is based on the string id and the value is a list of type interpretable
        2. Assign the call number for self's string id

        :param self:
        :return:
        """
        cls._dict_k_str_id_v_list_interpretable[self.get_str_id()].append(self)

        self._call_number_str_id = len(cls._dict_k_str_id_v_list_interpretable[self.get_str_id()])

    @classmethod
    def _handle_dict_k_name_v_list_interpretable(cls, self: Interpretable):
        """
        1. Add self to dict where the key is based on the name and the value is a list of type interpretable
        2. Assign the call number for self's name

        :param self:
        :return:
        """
        cls._dict_k_name_v_list_interpretable[self.get_name()].append(self)

        self._call_number_name = len(cls._dict_k_name_v_list_interpretable[self.get_name()])

    ###

    def get_tuple_id_line_number(self) -> Sequence[int]:
        """
        Return a tuple of ints. The ints are based on python frame source code line numbers
        that came from a inspect.currentframe() call.

        Notes:
            This tuple is useful for identifying instances of an objects of type(self) created on the same source
            code line.

                Example:
                    Executing code that calls a function that creates an object of the Interpretable type on the same
                    source code line will have the same tuple ID.

        AKA: Source Code Line Tuple ID

        :return:
        """
        return self._tuple_id_line_number

    def get_call_number_interpretable(self) -> int:
        """
        Get the call number based on the amount of interpretable type made.

        Notes:
            Interpretable number is based on the amount of objects that are instances of Interpretable.
            So if there are 23 objects that are instances of Interpretable then the 23rd object will have the
            Interpretable number of 23.

            This number correlates to the number of objects of the type Interpretable made, so this is not generally
            that helpful to use since it's more on the level of being meta meta programming rather than just
            meta programming.

        AKA: Interpretable Call Number

        :return:
        """

        return self._call_number_interpretable

    def get_call_number_type(self) -> int:
        """
        Get the call number of type(self)

        Notes:
            Type number is based on the amount of object's of type(self) that are created.
            So if there are 23 objects of type(self) then the 23rd object will have the Instantiated number of 23.

            This number is correlated to the amount of type(self) made so it's helpful as a call number for
            the uniquely identifying a specific self.

        AKA: type(self) Call Number

        :return:
        """
        return self._call_number_type

    def get_call_number_str_id(self) -> int:
        """
        Get the call number based on self's string id

        :return:
        """
        return self._call_number_str_id

    def get_call_number_name(self) -> int:
        """
        Get the call number based on self's name

        :return:
        """

        return self._call_number_name

    def get_call_number_tuple_id_line_number(self) -> int:
        """
        Get the call number based on self's Tuple ID

        Notes:
            Call number is based on how many objects are in the appropriate tuple id's list of interpretables in
            _dict_k_tuple_id_line_number_v_list_interpretable

            This number is useful for identifying a unique instance of an object created on the same source code line.
                Example:
                    Executing code that calls a function that creates an object of the Interpretable type on the same
                    source code line will have the same tuple ID, but now we use the call number of that code executed
                    which is basically the call count of that execution.

            *This number can be especially useful for counting the amount of times a source code line has been executed.

        AKA: Source Code Count

        :return:
        """
        return self._call_number_tuple_id_line_number

    def get_line_number_by_python_frame_object_index(self, index: int) -> int:
        """
        Get line number of python frame via index from the tuple id line number

        IMPORTANT NOTES:
            *THE LINE NUMBER FOR DECORATORS CANNOT BE DETERMINED

        :param index:
        :return:
        """
        return self.get_tuple_id_line_number()[index]

    @classmethod
    def get_dict_k_type_qualname_v_list_type_self(cls) -> Dict[str, List[Interpretable]]:
        """
        Get a dict where the key is a __qualname__ of the class and the key is a list of objects of the type
        Interpretable

        Notes:
            The key is the __qualname__ of an object that the use has no control of, so you can think of this as
            something that maybe useful to the person who maintains this code.

            The length of a list within the dict can be useful for counting the amount of times an object of type(self)
            has been made.

        :return:
        """
        return cls._dict_k_type_qualname_v_list_type_self

    @classmethod
    def get_list_object_of_type_interpretable(cls) -> List[Interpretable]:
        """
        Get a List of objects that are of type Interpretable. This list is the same regardless of subclass

        Notes:
            This list is useful for seeing all objects of type interpretable.

        :return:
        """
        return cls._list_object_of_type_interpretable

    @classmethod
    def get_dict_k_tuple_id_line_number_v_list_interpretable(cls) -> Dict[Sequence[int], List[Interpretable]]:
        """
        Get a dict where the key is a tuple id with objects that are of type Interpretable.

        Notes:
            The length of a list within the dict can be useful for counting the amount of times source code on the same
            line has been executed.

        :return:
        """
        return cls._dict_k_tuple_id_line_number_v_list_interpretable

    @classmethod
    def get_dict_k_name_v_list_interpretable(cls) -> Dict[str, List[Interpretable]]:
        """
        Get a dict where the key is an Interpretable object's name and the value is a list of Interpretable objects
        that have the same name.
        :return:
        """
        return cls._dict_k_name_v_list_interpretable

    @classmethod
    def get_dict_k_str_id_v_list_interpretable(cls) -> Dict[str, List[Interpretable]]:
        """
        Get a dict where the key is an Interpretable object's string id and the value is a list of Interpretable objects
        that have the same string id.
        :return:
        """
        return cls._dict_k_str_id_v_list_interpretable
