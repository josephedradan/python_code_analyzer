"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/18/2021

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
def test(n):
    z = 0
    while (z < n ** 2):
        algorithm_recorder.iteration_scope_start("z", z)
        i = 1
        while (i <= n):
            algorithm_recorder.iteration_scope_start("i", i)
            algorithm_recorder.iteration_scope_end_none()
            i += 1
        j = 1
        while ((2 * j) < n):
            algorithm_recorder.iteration_scope_start("j", j)

            p = n
            while (p >= 1):
                algorithm_recorder.iteration_scope_start("p", p)

                algorithm_recorder.iteration_scope_end_none()
                p /= 2

            algorithm_recorder.iteration_scope_end_none()
            j += 1

        algorithm_recorder.iteration_scope_end_none()


if __name__ == '__main__':
    test(2)
    print()
    algorithm_recorder.print()
