"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 8/9/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""

from python_code_analyzer.interpretable.event.event_border import EventBorder


class EventBorderCallable(EventBorder):
    """
    This class allows for more methods and method overrides specific to classes that have this class as a super class.
    Basically, we use this class to take advantage of python's MRO to to override specific methods for special reasons.

    Notes:
        Recall that objects that inherit from this class are created within a decorator.

    """

    def get_line_number(self) -> int:
        """
        Because the inspect module cannot see the line number of where a decorator is located, the creation and thus the
        line number for the creation of this object cannot be determined.

        :param index:
        :return:
        """
        return -1

    def get_call_number_line_number(self):
        """
        Because the inspect module cannot see the line number of where a decorator is located, the creation and thus the
        line number for the creation of this object cannot be determined.

        :return:
        """
        return -1

    def get_call_number_tuple_id_python_frame_line_number(self) -> int:
        """
        Because the inspect module cannot see the line number of where a decorator is located, the creation and thus the
        line number for the creation of this object cannot be determined.

        :return
        """
        return -1
