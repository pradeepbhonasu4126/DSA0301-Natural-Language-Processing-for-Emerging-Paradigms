def fsa_ends_with_ab(input_string):
    state = 0  # Start state

    for char in input_string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'a':
                state = 1
            elif char == 'b':
                state = 2
            else:
                state = 0
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    # Accepting state is state 2 if the last two characters were 'ab'
    return state == 2

# Test the automaton
test_strings = ['ab', 'aab', 'cab', 'baba', 'abc', 'abab']
for s in test_strings:
    result = fsa_ends_with_ab(s)
    print(f"Input: '{s}' => Accept: {result}")
