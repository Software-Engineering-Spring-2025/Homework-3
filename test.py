'''
    test for reverse sorted list
    '''
from hw2_debugging import merge_sort

def test_case2():
   
    random_array = [9,8,7,6,5,4,3,2,1]
    sorted_array = merge_sort(random_array)
    assert sorted_array == [1,2,3,4,5,6,7,8,9], "works no probs"
 
