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

k = 1


@algorithm_recorder.decorator_wrapper_callable()
def func_mid(n):
    """"""
    
    count  = 0

    k = 1
    z = 0
    while z < n:
        algorithm_recorder.event_iteration_start("z", z)

        i = 1

        while i <= n / 2:
            algorithm_recorder.event_iteration_start("i", i)

            count +=1

            i += 1
            algorithm_recorder.event_iteration_end()

        j = 1
        while j < (n - 1):
            algorithm_recorder.event_iteration_start("j", j)

            p = 0
            while (p < j):
                algorithm_recorder.event_iteration_start("p", p)

                count += 1

                p += 1
                algorithm_recorder.event_iteration_end()

            j += 1
            algorithm_recorder.event_iteration_end()

        z += 1

        k += 1
        algorithm_recorder.event_iteration_end()

    return k, count


if __name__ == '__main__':
    result = func_mid(5)
    print(result)
    algorithm_recorder.print()
