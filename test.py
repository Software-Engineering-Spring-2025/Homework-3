'''
test for negative numbers
'''
from hw2_debugging import merge_sort  # Assuming your code is in my_module.py

def test_case3():
    '''
    test for negative numbers
    '''
    random_array = [-1,-2,-3,-4,-5,-1]
    sorted_array = merge_sort(random_array)
    assert sorted_array == [-5,-4,-3,-2,-1,-1], "works no probs"

def test_case2():
    '''
    testing begins here
    '''
    random_array = [9,8,7,6,5,4,3,2,1]
    sorted_array = merge_sort(random_array)
    assert sorted_array == [1,2,3,4,5,6,7,8,9], "works no probs"
