"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 7/26/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Sequence, Dict, Union, List, Any


def get_dict_as_str(dict_given: Union[Dict, None]) -> str:
    """
    Kwargs as a string
    :param dict_given:
    :return:
    """
    if dict_given is not None:
        list_str_kwargs = [f"{i[0]}=\"{i[1]}\"" if isinstance(i[1], str) else f"{i[0]}={i[1]}" for i in
                           dict_given.items()]

        str_dict = ", ".join(list_str_kwargs) if dict_given else ""

    else:
        str_dict = ""

    return str_dict


def get_sequence_as_str(sequence_given: Union[Sequence, None]) -> str:
    """
    Args as a string

    :param sequence_given:
    :return:
    """

    if sequence_given is not None:
        list_str_args = [f"\"{i}\"" if isinstance(i, str) else str(i) for i in sequence_given]

        str_args = ", ".join(list_str_args) if sequence_given else ""
    else:
        str_args = ""

    return str_args


def get_spacing(length: int) -> int:
    """
    Finds the next discrete count given a number


    :param length:
    :return:
    """
    spacing_division = 3
    spacing_min = 2

    count = 0

    while True:
        result = spacing_division * count

        if result < (length + spacing_min):
            count += 1
            continue

        return result


def get_list_length_from_list_str(list_stings: Sequence[str], amount_space_additional) -> List[int]:
    """
    Get the lengths of each string and return it as a list of ints

    :param list_stings:
    :param amount_space_additional:
    :return:
    """
    return [len(i) + amount_space_additional for i in list_stings]


# def get_str_row(list_header: List[str], list_data: List[Any], size_additional=1) -> str:
#     """
#     Format the given list of data based on the list of headers' length
#
#     :param list_header:
#     :param list_data:
#     :param size_additional:
#     :return:
#     """
#
#     list_length = get_list_length_from_list_str(list_header, size_additional)
#
#     str_base = "{:<{}}" * len(list_header)
#
#     list_str_and_length = []
#
#     for data, length in zip(list_data, list_length):
#         list_str_and_length.extend([str(data), length])
#
#     str_base = str_base.format(*list_str_and_length)
#
#     return str_base


def get_str_from_list_str_and_length(list_data: Sequence[Any], list_length: List[int]) -> str:

    str_base = "{:<{}}" * len(list_data)

    list_str_and_length = []

    for data, length in zip(list_data, list_length):
        list_str_and_length.extend([str(data), length])

    str_base = str_base.format(*list_str_and_length)

    return str_base