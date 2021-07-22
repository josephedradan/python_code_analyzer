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
from python_code_recorder.code_recorder import CodeRecorder

algorithm_recorder = CodeRecorder()


@algorithm_recorder.decorator_wrapper_callable
def recursive(x):
    if x == 0:
        return "Done "

    return recursive(x - 1)


if __name__ == '__main__':
    print(recursive(10))
    print()

    algorithm_recorder.print()

    # print()
    # algorithm_recorder.get_scope_recorder().print_call_order_scope_complete()
    # print()
    # algorithm_recorder.get_scope_recorder().print_call_order_scope()
    # print()
    # algorithm_recorder.get_scope_recorder().print_amount_scopes_per_scope_name()
    # print()
    # print("-"*100)
    # print()

    # TODO: WHY DID I WRITE THE BELOW????
    # import inspect
    #
    # x = inspect.getsource(recursive)
    # print(x)
    # print()
    #
    # from ast import parse
    # import ast
    #
    # z = parse(x, mode='exec')
    # print(z)
    # # print(dump(z, indent=4))
    # print(ast.dump(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval')))

    # pprint(dump(z), 2)
