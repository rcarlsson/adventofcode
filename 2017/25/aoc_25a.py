import sys


def test_input_as_py(state, tape, cursor):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'B'

    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'

    return state, tape, cursor


def input_as_py(state, tape, cursor):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'E'

    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'A'

    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'D'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'C'

    elif state == 'D':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'F'

    elif state == 'E':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'

    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'

    return state, tape, cursor


def solve(file_name, state, steps):
    tape = [0]
    cursor = 0

    while steps:
        if file_name == 'input':
            state, tape, cursor = input_as_py(state, tape, cursor)
        elif file_name == 'test_input':
            state, tape, cursor = test_input_as_py(state, tape, cursor)

        if cursor < 0:
            tape.insert(0, 0)
            cursor += 1
        elif cursor >= len(tape):
            tape.append(0)
        steps -= 1

    return tape.count(1)


def main():
    file_name = sys.argv[1]
    state = 'A'
    steps = 12386363
    result = solve(file_name, state, steps)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()
