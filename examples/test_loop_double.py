"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 2/13/2021

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
def test_loop_double(string, n):
    _count = 0

    i = 1

    algorithm_recorder.event_iteration_start("W1", {"i": i}, str_id="test")
    while i <= n:

        # print(i)

        j = 1
        algorithm_recorder.event_iteration_start("W2", {"i": i, "j": j}, str_id="test")
        while j <= i:
            # print("\t", j)
            # print(string)

            j = j * 2

            _count += 1

            algorithm_recorder.event("W2V", {"j": j, "_count": _count})

        algorithm_recorder.event_iteration_end()

        i = i + 1
    algorithm_recorder.event_iteration_end()

    # print(f"Count: {_count}")


if __name__ == '__main__':
    test_loop_double("Hello", 2)
    print()

    algorithm_recorder.print()
