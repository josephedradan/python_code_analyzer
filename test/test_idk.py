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

from algorithm_analyzer.algorithm_recorder import AlgorithmRecorder

algorithm_recorder = AlgorithmRecorder()


@algorithm_recorder.decorator_wrapper_callable
def greeting(n):
    if n <= 1: return
    for i in range(n):
        algorithm_recorder.iteration_scope_start("i", i)
        print("hello")
        algorithm_recorder.iteration_scope_end_none()


if __name__ == '__main__':
    greeting(10)

    algorithm_recorder.print()

    # print()
    # algorithm_recorder.get_scope_recorder().print_call_order_scope_complete()
    # print()
    # algorithm_recorder.get_scope_recorder().print_call_order_scope()
    # print()
    # algorithm_recorder.get_scope_recorder().print_amount_scopes_per_scope_name()
