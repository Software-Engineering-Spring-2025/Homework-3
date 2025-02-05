'''
3 test cases to test various scenarios that could possibly come up during merge sort
'''
from hw2_debugging import merge_sort
def test_case1():
    '''
    test for empty list edge case
    '''
    random_array = []
    sorted_array = merge_sort(random_array)
    assert sorted_array == [], "works no probs"
