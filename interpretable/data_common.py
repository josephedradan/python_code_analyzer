"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 8/8/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from abc import ABC, abstractmethod
from typing import Union


class DataCommon(ABC):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None):
        # Name of this object
        self._name: Union[str, None] = name

        # String ID of this object used for counting purposes (This should be given by the user)
        self._str_id: Union[str, None] = str_id

        """Variables that must be assigned via method calls"""

        # Stack frame index relative to the creation of interpretable recorder
        self._stack_frame_index: Union[int, None] = None

        # Indent Index (Level of the indent)
        self._scope_number: Union[int, None] = None

        ######

    def get_name(self) -> Union[str, None]:
        """
        Name of this object that the user gave it

        Notes:
            user assigns this.

        :return:
        """
        return self.__str__()

    def get_str_formal(self) -> str:
        """
        return string: "{address_hex}: {type(self).__qualname__}: {self.get_name()}"

        :return:
        """
        address_hex = "{0}{1:0{2}X}".format("0x", id(self), 16)

        str_formal = "{} {} {}".format(address_hex,
                                       type(self).__qualname__,
                                       '"{}"'.format(self.get_name())
                                       )
        return str_formal

    @abstractmethod
    def get_str_pseudo_like(self) -> str:
        """
        Get a string that looks more like pseudo code of this Interpretable

        :return:
        """
        pass

    def __str__(self) -> str:
        """
        Name of this object

        :return:
        """
        return "" if self._name is None else str(self._name)

    def get_str_id(self) -> str:
        """
        Get string ID

        Notes:
            The user Assigns this

            * If the string ID is None then an empty string will be returned instead because it looks nice.

        :return:
        """

        # If the string ID is None then print nothing because it looks nice.
        return "" if self._str_id is None else str(self._str_id)

    ######

    def get_stack_frame_number(self) -> Union[int, None]:
        """
        Get the stack frame index

        :return:
        """
        return self._stack_frame_index

    def auto_set_stack_frame_number(self, index) -> None:
        """
        Set the stack frame index

        Notes:
            User should not assign this, a recorder must assign this

        :param index:
        :return:
        """
        self._stack_frame_index = index

    def get_scope_number(self) -> Union[int, None]:
        """
        Get the scope number

        :return:
        """
        return self._scope_number

    def auto_set_scope_number(self, index) -> None:
        """
        Set the scope number

        Notes:
            User should not assign this, a recorder must assign this

        :param index:
        :return:
        """
        self._scope_number = index
