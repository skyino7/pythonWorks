# Challenge: write a function merge_arrays(), that takes two lists of integers as inputs,
#   combines them, removes duplicates, sorts the combined list and returns it

def merge_arrays(arrayA, arrayB):
  return


def test():
    tests = {
        1: [1,2,3,4,5] == merge_arrays([1,2,3,4], [3,4,5]),
        2: [3,4,5] == merge_arrays([3,4,5], [3,4,5]),
        3: [1,2,3,4,5] == merge_arrays([1,2], [3,4,5]),
        4: [1,2,3,4,5] == merge_arrays([4,3,2,1], [3,4,5]),
        5: [2,3,4,5] == merge_arrays([2,2,2,2], [5,4,3])
    }
    if all(tests.values()):
        print('Tests passed!')
    else:
        print('Tests failed!')

if __name__ == '__main__':
    test()