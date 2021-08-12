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
from typing import List, Sequence, Dict, Any

from python_code_analyzer.functions_common import get_list_length_from_list_str, \
    get_str_from_list_str_and_length
from python_code_analyzer.interpretable.event.event import Event
from python_code_analyzer.interpretable.interpretable import Interpretable
from python_code_analyzer.interpretable_recorder.interpretable_recorder import InterpretableRecorder

"""
Python frame index for the line number when an event is created

Notes:
    The assumption is -3, it may change if whatever makes events change.
    -3 will probably give you the line number of the event call put in by the user in their code
"""
PYTHON_FRAME_INDEX_DEFAULT = -3

AMOUNT_SPACING_MULTIPLE = 4
AMOUNT_SPACING_HEADER = 2

"""
Dictionary of Interpretable Header and the method to get that header information given a interpretable
Notes:
    Interp. C.# = Interpretable Count Number
    type C.# = Type Count Number
    Line# = Line Number
    Line# C.# = Line Number Count Number
    str_id = String ID
    str_id C.# = String ID Count Number
    name = Name
    name C.# = Name Count Number

"""
DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD = {
    "Interp. C.#": lambda interpretable: interpretable.get_call_number_interpretable(),
    "type C.#": lambda interpretable: interpretable.get_call_number_type(),
    "Line#": lambda interpretable: interpretable.get_line_number_by_python_frame_object_index(
        PYTHON_FRAME_INDEX_DEFAULT),
    "Line# C.#": lambda interpretable: interpretable.get_call_number_tuple_id_line_number(),
    "str_id": lambda interpretable: interpretable.get_str_id(),
    "str_id C.#": lambda interpretable: interpretable.get_call_number_str_id(),
    "name": lambda interpretable: interpretable.get_name(),
    "name C.#": lambda interpretable: interpretable.get_call_number_name()
}


class EventRecorderPrinter:

    def __init__(self, event_recorder: InterpretableRecorder):
        self.interpretable_recorder = event_recorder

        # List of events called in order with event start and event end (start and end are not explicitly stated)
        self._list_interpretable: List[Event] = self.interpretable_recorder.get_list_event()

    def print_call_order_simple(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
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

        for interpretable in self._list_interpretable:
            """
            indenting = Space * (Stack frame - 1) * Spacing
            
            Notes:
                - 1 to subtract from the outer scope, if there is not outer scope then expect some breaking 
            """
            indenting = self._get_indenting(interpretable, amount_spacing_multiple)

            str_temp = "{}{}".format(indenting, interpretable.get_str_pseudo_like())
            print(str_temp)

    def print_call_order_detailed(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Prints all the features of the basic example and a lot more

        Notes:
            In the example below, the table is included along with the with is printed with the print_call_order_simple
            
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

        list_header = DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD

        list_data_length_max = get_list_length_from_list_str(list_header, AMOUNT_SPACING_HEADER)

        for interpretable in self._list_interpretable:
            for i, data in enumerate(get_list_data_of_interpretable(interpretable)):

                length = len(str(data)) + AMOUNT_SPACING_HEADER

                if length > list_data_length_max[i]:
                    list_data_length_max[i] = length

        print(get_str_from_list_str_and_length(list_header, list_data_length_max))

        for interpretable in self._list_interpretable:
            """
            indenting = Space * (Stack frame - 1) * Spacing

            Notes:
                - 1 to subtract from the outer scope, if there is not outer scope then expect some breaking 
            """
            indenting = self._get_indenting(interpretable, amount_spacing_multiple)

            list_data = get_list_data_of_interpretable(interpretable)

            str_data = get_str_from_list_str_and_length(list_data, list_data_length_max)

            str_full = "{}{}{}".format(str_data, indenting, interpretable.get_str_pseudo_like())
            print(str_full)

    def print_call_order_event_simple(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE,
                                      len_name_args_kwargs=None):
        """

        :param amount_spacing_multiple:
        :return:
        """

        # for k, v in self.event_recorder.get_dict_k_tuple_id_line_number_v_list_interpretable().items():

        for event_current in self.interpretable_recorder.get_list_event():
            part_1 = " " * event_current.get_stack_frame_index() * amount_spacing_multiple
            part_2 = event_current.get_str_formal()
            part_3 = "Source Code Count: {}".format(event_current.get_call_number_tuple_id_line_number())
            part_4 = "Source Code Line Tuple ID: {}".format(event_current.get_tuple_id_line_number())
            part_5 = "{} Call Number: {}".format(type(event_current).__qualname__,
                                                 event_current.get_call_number_type())
            part_6 = "Interpretable Call Number: {}".format(event_current.get_call_number_interpretable())

            str_temp = "{}{} {} {} {} {}".format(part_1,
                                                 part_2,
                                                 part_3,
                                                 part_4,
                                                 part_5,
                                                 part_6
                                                 )
            print(str_temp)

    def _print_dict_k_str_v_list(self,
                                 str_dict_key_header: str,
                                 dict_k_v_list: Dict[Any, Sequence],
                                 amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE):

        # Pre spacing
        str_space_pre = " " * amount_spacing_multiple

        for str_id, list_interpretable in dict_k_v_list.items():

            list_header = ["Index+1", *DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD]

            list_data_length_max = get_list_length_from_list_str(list_header, AMOUNT_SPACING_HEADER)

            # Print the Key from the dict and the size of the sequence
            print("{}: {}\n"
                  "Amount: {}".format(str_dict_key_header, str_id, len(list_interpretable)))

            # Print header table
            print("{}{}".format(str_space_pre, get_str_from_list_str_and_length(list_header, list_data_length_max)))

            for index, interpretable in enumerate(list_interpretable):
                indenting = self._get_indenting(interpretable, amount_spacing_multiple)

                list_data = [index + 1, *get_list_data_of_interpretable(interpretable)]

                str_data = get_str_from_list_str_and_length(list_data, list_data_length_max)

                str_full = "{}{}{}{}".format(str_space_pre, str_data, indenting, interpretable.get_str_pseudo_like())

                print(str_full)
            print()

    def print_dict_k_str_id_v_list_interpretable(self, amount_spacing_multiple: int = AMOUNT_SPACING_MULTIPLE) -> None:
        """
        Print the dict containing the interpretable's str_id with the amount of interpretables and the interpretables
        themselves with data that have the same str_id.

        Notes:
            The example below does include the printing of the interpretables, but it can't fit in the 120
            char limit so I removed it from the example below.

        Example:
            str_id: test
            Amount: 3
                Index+1  Interp. C.#  type C.#  Line#  Line# C.#  str_id  str_id C.#  name  name C.#
                1        2            1         33     1          test    1           W1    1
                2        3            2         39     1          test    2           W2    1
                3        6            3         39     2          test    3           W2    2


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
        Print the dict containing the interpretable's name with the amount of interpretables and the interpretables
        themselves with data that have the same name.

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
        Print the dict containing the interpretable's __qualname__ with the amount of interpretables and the
        interpretables themselves with data that have the same __qualname__.

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
        Print the dict containing the interpretable's tuple line number with the amount of interpretables and the
        interpretables themselves with data that have the same tuple line number.

        :param amount_spacing_multiple:
        :return:
        """
        self._print_dict_k_str_v_list("Tuple Line number",
                                      Interpretable.get_dict_k_tuple_id_line_number_v_list_interpretable(),
                                      amount_spacing_multiple)

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
        for key, value in Interpretable.get_dict_k_str_id_v_list_interpretable().items():
            print("Event name: {0:<{1}} Amount of events: {2}".format(key, spacing if len(key) < spacing else len(
                key) // 5 * 6, len(value)))

    @staticmethod
    def _get_indenting(interpretable: Interpretable, amount_spacing_multiple: int, offset: int = 1):
        """
        Get standard indenting

        :param interpretable:
        :param amount_spacing_multiple:
        :param offset:
        :return:
        """
        return " " * (interpretable.get_stack_frame_index() - offset) * amount_spacing_multiple


def get_list_data_of_interpretable(interpretable: Interpretable):
    """
    Get interpretable data into a list

    Notes:
        Note that if a result from a callable from the dict returns the int -1 then it will be replaced with N/A.
        The reason why N/A is returned is because I don't really have a use for -1 as a value returned, so it could
        be used to signify an error instead

    :param interpretable:
    :return:
    """

    list_data = []

    for header, function_interpretable in DICT_K_HEADER_INTERPRETABLE_V_INTERPRETABLE_METHOD.items():

        result = function_interpretable(interpretable)

        if result == -1:
            result = "N/A"

        list_data.append(result)

    return list_data
