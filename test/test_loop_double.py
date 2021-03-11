"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/13/2021

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
def test_loop_double(string, n):
    count = 0

    i = 1

    while i <= n:
        algorithm_recorder.iteration_scope_start("Upper", i)

        # print(i)

        j = 1
        while j <= i:
            algorithm_recorder.iteration_scope_start("Inner", j)

            # print("\t", j)
            # print(string)

            j = j * 2

            count += 1
            algorithm_recorder.iteration_scope_end_none()

        i = i + 1
        algorithm_recorder.iteration_scope_end_none()

    # print(f"Count: {count}")


if __name__ == '__main__':

    test_loop_double("Hello", 20)
    print()
    algorithm_recorder.get_scope_recorder().print_call_order_scope_complete()
    print()
    algorithm_recorder.get_scope_recorder().print_call_order_scope()
    print()
    algorithm_recorder.get_scope_recorder().print_amount_scopes_per_scope_name()
