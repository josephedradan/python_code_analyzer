"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/22/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""

from python_code_recorder.code_recorder import CodeRecorder

algorithm_recorder = CodeRecorder()


@algorithm_recorder.decorator_wrapper_callable
def greeting(n):
    if n <= 1: return
    for i in range(n):
        algorithm_recorder.iteration_scope_start("i", i)
        print("hello")
        algorithm_recorder.iteration_scope_end_none()


if __name__ == '__main__':
    greeting(4)

    algorithm_recorder.print()
