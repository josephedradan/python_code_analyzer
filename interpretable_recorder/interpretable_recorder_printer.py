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
from typing import Sequence, Dict, Any

from python_code_analyzer.functions_common import (get_list_length_from_list_str, get_str_from_list_str_and_length)
from python_code_analyzer.interpretable.event.event import Event
from python_code_analyzer.interpretable.interpretable import Interpretable
from python_code_analyzer.interpretable_recorder.interpretable_recorder import InterpretableRecorder

AMOUNT_SPACING_MULTIPLE = 4  # Amount of space for the pseudo code look a like code
AMOUNT_SPACING_HEADER = 2  # Amount of spacing between headers

"""
Dictionary of Interpretable Header and the method to get that header information given a interpretable
Notes:
    Interp. C.# = Interpretable Count Number
    type C.# = Type Count Number
    Line# = Assumed Python code Line Number
    P.F.T. ID Line# C.# = Python Frame Tuple ID Line Number Count Number
    Line# C.# = Line Number Count Number
    str_id = String ID
    str_id C.# = String ID Count Number
    name = Name
    name C.# = Name Count Number
    Stack Frame # = Stack Frame number

"""
DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD = {
    "Interp. C.#": lambda interpretable: interpretable.get_call_number_interpretable(),
    "type C.#": lambda interpretable: interpretable.get_call_number_type(),
    "Line#": lambda interpretable: interpretable.get_line_number(),
    "P.F.T. ID Line# C.#": lambda interpretable: interpretable.get_call_number_tuple_id_python_frame_line_number(),
    "Line# C.#": lambda interpretable: interpretable.get_call_number_line_number(),
    "str_id": lambda interpretable: interpretable.get_str_id(),
    "str_id C.#": lambda interpretable: interpretable.get_call_number_str_id(),
    "name": lambda interpretable: interpretable.get_name(),
    "name C.#": lambda interpretable: interpretable.get_call_number_name(),
    "Stack Frame #": lambda interpretable: interpretable.get_stack_frame_index()
}


class EventRecorderPrinter:

    def __init__(self, interpretable_recorder: InterpretableRecorder):
        self._interpretable_recorder = interpretable_recorder

    def print_event_call_order_simple(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """

        Example:
            test_loop_double("Hello", 2) {
                W1 |i=1| {
                    W2 |i=1, j=1| {
                        W2V |j=2, _count=1|
                    }
                    W2 |i=2, j=1| {
                        W2V |j=2, _count=2|
                        W2V |j=4, _count=3|
                    }
                }
            }

        :param amount_spacing_multiple:
        :return:
        """

        for event_current in self._interpretable_recorder.get_list_event():
            """
            str_space_for_code = Space * (Stack frame - 1) * Spacing
            
            Notes:
                - 1 to subtract from the outer scope, if there is not outer scope then expect some breaking 
            """
            str_space_for_code = self._get_str_space_for_code(event_current, amount_spacing_multiple)

            str_temp = "{}{}".format(str_space_for_code, event_current.get_str_pseudo_like())
            print(str_temp)

    def print_event_call_order_detailed(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Prints all the features of the basic example and a lot more

        Notes:
            In the example below, the table is included along with the with is printed with the print_event_call_order_simple

        Example:
            Line#  Interp. C.#  Tup. Line# C.#  type C.#  str_id  str_id C.#  name  name C.#
            N/A    1            1               1                 1                 1
            33     2            1               1         test    1           W1    1
            39     3            1               2         test    2           W2    1
            48     4            1               1                 2           W2V   1
            50     5            1               1                 3           W2    2
            39     6            2               3         test    3           W2    2
            48     7            2               2                 4           W2V   2
            48     8            3               3                 5           W2V   3
            50     9            2               2                 6           W2    3
            53     10           1               3                 7           W1    4
            N/A    11           1               1                 8                 5

        :param amount_spacing_multiple:
        :return: None
        """

        # Header names
        list_header = DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD

        # List of lengths for each cell in the row
        list_data_length_max = get_list_length_from_list_str(list_header, AMOUNT_SPACING_HEADER)

        # Loop to adjust values in list_data_length_max
        for event_current in self._interpretable_recorder.get_list_event():
            for i, data in enumerate(get_list_data_of_event(event_current)):
                cell_length = len(str(data)) + AMOUNT_SPACING_HEADER

                if cell_length > list_data_length_max[i]:
                    list_data_length_max[i] = cell_length

        # Print the Header
        print(get_str_from_list_str_and_length(list_header, list_data_length_max))

        # Loop print the table body
        for event_current in self._interpretable_recorder.get_list_event():
            """
            str_space_for_code = Space * (Stack frame - 1) * Spacing

            Notes:
                - 1 to subtract from the outer scope, if there is not outer scope then expect some breaking 
            """
            str_space_for_code = self._get_str_space_for_code(event_current, amount_spacing_multiple)

            list_data = get_list_data_of_event(event_current)

            str_data = get_str_from_list_str_and_length(list_data, list_data_length_max)

            str_full = "{}{}{}".format(str_data, str_space_for_code, event_current.get_str_pseudo_like())
            print(str_full)

    def print_event_call_order_debug(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE):
        """
        Debug print

        :param amount_spacing_multiple:
        :return:
        """

        # for k, v in self.event_recorder.get_dict_k_tuple_id_python_frame_line_number_v_list_interpretable().items():

        for event_current in self._interpretable_recorder.get_list_event():
            str_space_for_code = " " * event_current.get_stack_frame_index() * amount_spacing_multiple

            str_formal_event = event_current.get_str_formal()

            str_data = " ".join([str(i) for i in get_list_data_of_event(event_current)])

            str_full = "{}{} {} {}".format(
                str_space_for_code,
                str_formal_event,
                str_data,
                event_current.get_str_pseudo_like()
            )
            print(str_full)

    def _print_dict_k_str_v_list(self,
                                 str_sorted_by: str,
                                 dict_k_v_list: Dict[Any, Sequence],
                                 amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE):
        """
        Given a name of what the dict is sorted by, a dict, and the amount of space


        :param str_sorted_by:
        :param dict_k_v_list:
        :param amount_spacing_multiple:
        :return:
        """
        # Spacing before printing the table (Basically the margin on the left side)
        str_space_margin = " " * amount_spacing_multiple

        # Header names
        list_header = ["Index+1", *DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD]

        # Loop over dictionary's key and value
        for key, list_interpretable in dict_k_v_list.items():

            # List of lengths for each cell in the row
            list_data_length_max = get_list_length_from_list_str(list_header, AMOUNT_SPACING_HEADER)

            # Loop to adjust values in list_data_length_max
            for interpretable in self._interpretable_recorder.get_list_event():
                for i, data in enumerate(get_list_data_of_event(interpretable)):
                    cell_length = len(str(data)) + AMOUNT_SPACING_HEADER

                    if cell_length > list_data_length_max[i]:
                        list_data_length_max[i + 1] = cell_length

            if key == -1:
                key = "N/A"

            # Print the Key from the dict and the size of its value
            print("{}: {}\n"
                  "Amount: {}".format(str_sorted_by, key, len(list_interpretable)))

            # Print header table
            print("{}{}".format(str_space_margin, get_str_from_list_str_and_length(list_header, list_data_length_max)))

            # Loop print the table body
            for index, interpretable in enumerate(list_interpretable):
                str_space_for_code = self._get_str_space_for_code(interpretable, amount_spacing_multiple)

                list_data = [index + 1, *get_list_data_of_event(interpretable)]

                str_data = get_str_from_list_str_and_length(list_data, list_data_length_max)

                str_full = "{}{}{}{}".format(str_space_margin,
                                             str_data,
                                             str_space_for_code,
                                             interpretable.get_str_pseudo_like())

                print(str_full)
            print()

    def print_dict_k_str_id_v_list_interpretable(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict where the key is the interpretable's str_id and it's value is a list of interpretables with the
        same str_id.

        Notes:
            The example below does include the printing of the interpretables, but it can't fit in the 120
            char limit so I removed it from the example below.

        :param amount_spacing_multiple:
        :return:
        """

        self._print_dict_k_str_v_list("str_id",
                                      Interpretable.get_dict_k_str_id_v_list_interpretable(),
                                      amount_spacing_multiple)

    def print_dict_k_name_v_list_interpretable(
            self,
            amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict where the key is the interpretable's name and it's value is a list of interpretables with the
        same name.

        :param amount_spacing_multiple:
        :return:
        """

        self._print_dict_k_str_v_list("name",
                                      Interpretable.get_dict_k_name_v_list_interpretable(),
                                      amount_spacing_multiple)

    def print_dict_k_qualname_v_list_interpretable(
            self,
            amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict where the key is the interpretable's __qualname__ and it's value is a list of interpretables
        with the same __qualname__.

        :param amount_spacing_multiple:
        :return:
        """

        self._print_dict_k_str_v_list("__qualname__",
                                      Interpretable.get_dict_k_type_qualname_v_list_type_self(),
                                      amount_spacing_multiple)

    def print_dict_k_tuple_line_number_v_list_interpretable(
            self,
            amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict where the key is the interpretable's tuple line number and it's value is a list of interpretables
        with the same tuple line number.

        :param amount_spacing_multiple:
        :return:
        """
        self._print_dict_k_str_v_list("Tuple Line number",
                                      Interpretable.get_dict_k_tuple_id_python_frame_line_number_v_list_interpretable(),
                                      amount_spacing_multiple)

    def print_dict_k_line_number_v_list_interpretable(
            self,
            amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict where the key is the interpretable's line number and it's value is a list of interpretables
        with the same line number.

        :param amount_spacing_multiple:
        :return:
        """
        self._print_dict_k_str_v_list("Line number",
                                      Interpretable.get_dict_k_line_number_v_list_interpretable(),
                                      amount_spacing_multiple)

    @staticmethod
    def _get_str_space_for_code(event: Event, amount_spacing_multiple: int, offset: int = 1):
        """
        Get standard indenting

        :param event:
        :param amount_spacing_multiple:
        :param offset:
        :return:
        """
        return " " * (event.get_stack_frame_index() - offset) * amount_spacing_multiple


def get_list_data_of_event(event: Event):
    """
    Get interpretable data into a list

    Notes:
        Note that if a result from a callable from the dict returns the int -1 then it will be replaced with N/A.
        The reason why N/A is returned is because I don't really have a use for -1 as a value returned, so it could
        be used to signify an error instead

    :param event:
    :return:
    """

    list_data = []

    for header, function_interpretable in DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD.items():

        result = function_interpretable(event)

        if result == -1:
            result = "N/A"

        list_data.append(result)

    return list_data
