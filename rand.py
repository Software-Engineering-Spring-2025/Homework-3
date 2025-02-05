"""Module containing random subprocess."""

##import subprocess
##import random
import secrets

def random_array(arr):
    """Function creating random array."""
    ##shuffled_num = None
    ##for i, _ in enumerate(arr):
   ##shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"],
   # capture_output=True, check = False)
        ##arr[i] = int(shuffled_num.stdout)
        ##arr[i] = random.randint(1, 20)

    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1  # Generate a secure random number between 1 and 20
    return arr
