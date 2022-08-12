"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/22/2021

Purpose:

Details:

Description:

Notes:
    Very basic example with a function and a loop

IMPORTANT NOTES:

Explanation:

Reference:

"""

from python_code_analyzer import PythonCodeAnalyzer

python_code_analyzer = PythonCodeAnalyzer()


@python_code_analyzer.decorator_wrapper_callable
def greeting(n):
    python_code_analyzer.event_iteration_start("for")  # Name of the event is "for"

    for i in range(n):
        print("hello")
        python_code_analyzer.event("Vars", {"i": i, "_i": i})  # Name of the event is "Vars". Recorded Vars is "i
    python_code_analyzer.event_iteration_end()


if __name__ == '__main__':
    greeting(10)
    print()

    python_code_analyzer.print_all()
