"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 8/12/2021

Purpose:

Details:

Description:

Notes:
    Double While Loop that has a recursive call inside the inner loop and it has an abrupt escape via return

IMPORTANT NOTES:

Explanation:

Reference:

"""
from python_code_analyzer.python_code_analyzer import PythonCodeAnalyzer

python_code_analyzer = PythonCodeAnalyzer()


@python_code_analyzer.decorator_wrapper_callable
def _recursive(given):
    count = given

    python_code_analyzer.event_iteration_start("W1")  # While 1

    while count < 10:

        python_code_analyzer.event_iteration_start("W2", dict_recorded_vars={"count": count})  # While 2

        while count < 10:
            count += 1

            python_code_analyzer.event("W2 Vars", dict_recorded_vars={"count": count})  # While 2 Vars

            return _recursive(count)

        python_code_analyzer.event_iteration_end()

    python_code_analyzer.event_iteration_end()


if __name__ == '__main__':
    _recursive(1)
    print()

    python_code_analyzer.print_all()
