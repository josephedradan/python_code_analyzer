"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 7/23/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from typing import Union

from python_code_analyzer.data_container.scope.scope import Scope

STR_SCOPE_OUTER_NAME = "Outer_Absolute"


class ScopeOuter(Scope):

    def __init__(self,
                 name: Union[str, None] = STR_SCOPE_OUTER_NAME,
                 str_id: Union[str, None] = None
                 ):
        super().__init__(name, str_id)
