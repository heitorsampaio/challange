import collections

def find_duplicates(array):
    """
    Write a python function that finds the duplicate items in any given array
    """
    return [item for item, count in collections.Counter(array).items() if count > 1]

l = [1,1,3,3,4,5,6,7,7,7,9,8,5]
print(find_duplicates(l))

## [1, 3, 5, 7]