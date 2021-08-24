"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/12/2021

Purpose:

Details:

Description:

Notes:
    Loop that has a recursive call inside it

IMPORTANT NOTES:

Explanation:

Reference:

"""

from python_code_analyzer.python_code_analyzer import PythonCodeAnalyzer

python_code_analyzer = PythonCodeAnalyzer()


@python_code_analyzer.decorator_wrapper_callable
def recursive(x, sum_previous=None):
    if sum_previous is None:
        python_code_analyzer.event("Sum is None")  # Event name "Sum is None"
        sum_previous = 0

    if x == 0:
        python_code_analyzer.event("Final")  # Event name "Final"
        return 1

    python_code_analyzer.event_iteration_start(name="for")  # Event name "for"
    for i in range(x):
        value = recursive(i, sum_previous)

        sum_previous += value

        # "sum_previous" and "value" recorded
        python_code_analyzer.event(dict_recorded_vars={"sum_previous": sum_previous, "value": value})

    python_code_analyzer.event_iteration_end()

    return sum_previous


if __name__ == '__main__':
    print(recursive(4))

    python_code_analyzer.print_all()
