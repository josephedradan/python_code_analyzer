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
from typing import Union

from python_code_analyzer.interpretable.scope.scope import Scope


class ScopeCallable(Scope):

    def __init__(self,
                 name: Union[str, None] = None,
                 str_id: Union[str, None] = None
                 ):
        super().__init__(name, str_id)
