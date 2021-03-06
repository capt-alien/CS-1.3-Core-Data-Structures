#!python
import sys


def contains(text, pattern):
    #O^n
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pat_size = len(pattern)
    if pat_size ==0:
        return True
        # While Loop
    for i in range(0,len(text)-len(pattern)+1):
        right = (i +pat_size)
        if text[i:right] == pattern:
            return True
    return False


def find_index(text, pattern):
    #O^n
    # Return the starting index of the first occurrence of pattern in text,
    # or None if not found.
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    pat_size = len(pattern)
    if pat_size ==0:
        return 0
        # While Loop
    for i in range(0,len(text)-len(pattern)+1):
        right = (i +pat_size)
        if text[i:right] == pattern:
            return i


def find_all_indexes(text, pattern):
    # O^n
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pat_size = len(pattern)
    indicies = []
    if pat_size ==0:
        for i in range(0,len(text)):
            indicies.append(i)
        return indicies
        # While Loop
    for i in range(0,len(text)-len(pattern)+1):
        right = (i +pat_size)
        if text[i:right] == pattern:
            indicies.append(i)
    return indicies


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
