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

    def get_line_number_by_python_frame_object_index(self, index: int) -> int:
        """
        Due to objects of this class being created from a decorator, Python frame objects DO NOT have access to the
        line where the decorator was placed.

        :param index:
        :return:
        """
        return -1
