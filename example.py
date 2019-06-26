# -*- coding: utf-8 -*-
"""example.py


Author -- Michael Widrich
Contact -- widrich@ml.jku.at
"""

import numpy as np
from multiprocessing import Pool
from share_array.share_array import get_shared_array, make_shared_array


def worker_function(i):
    """Function that uses the shared array"""
    array = get_shared_array('my_shared_array')  # get shared memory array as numpy array
    array[:] += i  # modify the shared memory array as numpy array
    
    
if __name__ == '__main__':
    np_array = np.arange(3*5).reshape((3, 5))  # make a numpy array
    make_shared_array(np_array, name='my_shared_array')  # create shared memory array from numpy array
    shared_array = get_shared_array('my_shared_array')  # get shared memory array as numpy array
    
    print("Shared array before multiprocessing:")
    print(shared_array)  # Print array
    
    with Pool(processes=2) as pool:
        pool.map(worker_function, range(15))  # use a multiprocessing.Pool to distribute work to worker processes

    print("Shared array after multiprocessing:")
    print(shared_array)  # Content of array was changed in worker processes
