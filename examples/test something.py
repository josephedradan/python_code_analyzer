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
from python_code_analyzer.python_code_analyzer import CodeRecorder

algorithm_recorder = CodeRecorder()


@algorithm_recorder.decorator_wrapper_callable
def test(n):
    z = 0
    while (z < n ** 2):
        algorithm_recorder.event_iteration_start("z", z)
        i = 1
        while (i <= n):
            algorithm_recorder.event_iteration_start("i", i)
            algorithm_recorder.event_iteration_end()
            i += 1
        j = 1
        while ((2 * j) < n):
            algorithm_recorder.event_iteration_start("j", j)

            p = n
            while (p >= 1):
                algorithm_recorder.event_iteration_start("p", p)

                algorithm_recorder.event_iteration_end()
                p /= 2

            algorithm_recorder.event_iteration_end()
            j += 1

        algorithm_recorder.event_iteration_end()


if __name__ == '__main__':
    test(2)
    print()
    algorithm_recorder.print()
