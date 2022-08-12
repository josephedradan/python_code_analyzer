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
from python_code_analyzer.python_code_analyzer import PythonCodeAnalyzer

python_code_analyzer = PythonCodeAnalyzer()

k = 1


@python_code_analyzer.decorator_wrapper_callable()
def func_mid(n):

    k = 1
    z = 0

    python_code_analyzer.event_iteration_start("W1 S", {"z": z})  # While 1 Start
    while z < n:

        i = 1

        python_code_analyzer.event_iteration_start("W2A S", {"i": i})  # While 2A Start
        while i <= n / 2:
            python_code_analyzer.event("Counter")

            i += 1

        python_code_analyzer.event_iteration_end("W2A E")  # While 2A End

        j = 1

        python_code_analyzer.event_iteration_start("W2B S", {"j": j})  # While 2B Start
        while j < (n - 1):

            p = 0

            python_code_analyzer.event_iteration_start("W3 S", {"p": p})  # While 3 Start
            while p < j:
                python_code_analyzer.event("Counter")

                p += 1
            python_code_analyzer.event_iteration_end("W3 E")  # While 3 End

            j += 1
        python_code_analyzer.event_iteration_end("W2B E")  # While 2B End

        z += 1

        k += 1
    python_code_analyzer.event_iteration_end("W1 E")  # While 1 Start

    return k


if __name__ == '__main__':
    result = func_mid(5)
    print(result)

    python_code_analyzer.print_all()
