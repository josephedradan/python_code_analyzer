"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/12/2021

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


@python_code_analyzer.decorator_wrapper_callable
def recursive(x):
    python_code_analyzer.event("Beginning", {"x": x})  # Event name "Beginning", "x" is recorded
    if x == 0:
        python_code_analyzer.event("Final")  # Event name "Final"
        return "Done"

    return recursive(x - 1)


if __name__ == '__main__':
    print(recursive(10))
    print()

    python_code_analyzer.print_all()
