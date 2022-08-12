"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/13/2021

Purpose:

Details:

Description:

Notes:
    Double while loop

IMPORTANT NOTES:

Explanation:

Reference:

"""
from python_code_analyzer.python_code_analyzer import PythonCodeAnalyzer

python_code_analyzer = PythonCodeAnalyzer()


@python_code_analyzer.decorator_wrapper_callable
def loop_double(n):
    count = 0

    i = 1

    # While 1. "i" recorded. str_id = "loop"
    python_code_analyzer.event_iteration_start("W1", {"i": i}, str_id="loop")
    while i <= n:

        j = 1

        # While 2. "i", "j" recorded. str_id = "loop"
        python_code_analyzer.event_iteration_start("W2", {"i": i, "j": j}, str_id="loop")
        while j <= i:
            j = j * 2

            count += 1

            # While 2 Vars. "j", "count" recorded.
            python_code_analyzer.event("W2 Vars", {"j": j, "count": count})

        python_code_analyzer.event_iteration_end()

        i = i + 1

    python_code_analyzer.event_iteration_end()


if __name__ == '__main__':
    loop_double(10)

    python_code_analyzer.print_all()
