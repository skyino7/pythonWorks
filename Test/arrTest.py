def merge_arrays(arrayA, arrayB):
    sortedArray = list(set(arrayA + arrayB))
    sortedArray.sort()
    return sortedArray

def test():
    tests = {
        "Test 1": [1,2,3,4,5] == merge_arrays([1,2,3,4], [3,4,5]),
        "Test 2": [3,4,5] == merge_arrays([3,4,5], [3,4,5]),
        "Test 3": [1,2,3,4,5] == merge_arrays([1,2], [3,4,5]),
        "Test 4": [1,2,3,4,5] == merge_arrays([4,3,2,1], [3,4,5]),
        "Test 5": [2,3,4,5] == merge_arrays([2,2,2,2], [5,4,3])
    }
    failed_tests = [name for name, passed in tests.items() if not passed]

    for name, passed in tests.items():
        print(name, 'passed' if passed else 'failed')

    print()

        # if not passed:
        #     print('Expected:', name.split()[1])
        #     print('Actual:', merge_arrays([1,2,3,4], [3,4,5]))
        #     print()

    # print('Sorted array:', merge_arrays([1,2,3,4], [3,4,5]))

    print('Tests run:', len(tests))
    print()

    print('Tests passed:', len(tests) - len(failed_tests), '/', len(tests))

    if failed_tests:
        print('Some tests failed:', ', '.join(failed_tests))
    else:
        print('All tests passed!')

if __name__ == '__main__':
    test()