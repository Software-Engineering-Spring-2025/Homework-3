'''
3 test cases to test various scenarios that could possibly come up during merge sort
'''
from hw2_debugging import merge_sort
import rand
def test_case1():
    '''
    test for empty list edge case
    '''
    random_array = []
    sorted_array = merge_sort(random_array)
    assert sorted_array == [], "works no probs"
def test_case2():
    '''
    test for reverse sorted list
    '''
    random_array = [9,8,7,6,5,4,3,2,1]
    sorted_array = merge_sort(random_array)
    assert sorted_array == [1,2,3,4,5,6,7,8,9], "works no probs"
def test_case3():
    '''
    test for negative numbers
    '''
    random_array = [-1,-2,-3,-4,-5,-1]
    sorted_array = merge_sort(random_array)
    assert sorted_array == [-5,-4,-3,-2,-1,-1], "works no probs"

