"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/12/2021

Purpose:

Details:

Description:

Notes:
    It's some random algorithm i thought in my head, idk what it does

IMPORTANT NOTES:

Explanation:

Reference:

"""
from algorithm_analyzer.algorithm_recorder import AlgorithmRecorder

algorithm_recorder = AlgorithmRecorder()


@algorithm_recorder.decorator_wrapper_callable
def recursive(x, sum=None):

    if sum is None:
        sum = 0

    if x == 0:
        return 1

    for i in range(x):
        algorithm_recorder.iteration_scope_start("For each loop", i)

        value = recursive(i, sum)

        sum += value
        algorithm_recorder.iteration_scope_end_none()

    return sum


if __name__ == '__main__':

    print(recursive(7))

    # algorithm_recorder.print()
    print()
    algorithm_recorder.get_scope_recorder().print_call_order_scope_complete()
    print()
    algorithm_recorder.get_scope_recorder().print_call_order_scope()
    print()
    algorithm_recorder.get_scope_recorder().print_amount_scopes_per_scope_name()
