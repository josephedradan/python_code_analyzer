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

k = 1


@algorithm_recorder.decorator_wrapper_callable()
def func_mid(n):
    """"""
    
    count  = 0

    k = 1
    z = 0
    while z < n:
        algorithm_recorder.iteration_scope_start("z", z)

        i = 1

        while i <= n / 2:
            algorithm_recorder.iteration_scope_start("i", i)

            count +=1

            i += 1
            algorithm_recorder.iteration_scope_end_none()

        j = 1
        while j < (n - 1):
            algorithm_recorder.iteration_scope_start("j", j)

            p = 0
            while (p < j):
                algorithm_recorder.iteration_scope_start("p", p)

                count += 1

                p += 1
                algorithm_recorder.iteration_scope_end_none()

            j += 1
            algorithm_recorder.iteration_scope_end_none()

        z += 1

        k += 1
        algorithm_recorder.iteration_scope_end_none()

    return k, count


if __name__ == '__main__':
    result = func_mid(5)
    print(result)
    algorithm_recorder.print()
