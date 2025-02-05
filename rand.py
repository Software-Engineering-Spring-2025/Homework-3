'''
generates random nums for us
'''
import secrets
def random_array(arr):
    '''
    rand number generator in range 1 - 20
    '''
    for index, _ in enumerate(arr):
        arr[index] = secrets.randbelow(20) + 1
    return arr
