## multiprocess-shared-numpy-arrays

### Easily share numpy arrays between processes
Convenience functions for sharing
[numpy arrays](https://docs.scipy.org/doc/numpy/) 
between multiple processes using 
[multiprocessing.Array](https://docs.python.org/3.4/library/multiprocessing.html?highlight=process#multiprocessing.Array)
as process safe shared memory arrays.

Example usage:

```python
import numpy as np
from share_array.share_array import make_shared_array, get_shared_array

# create a numpy array
np_array = np.arange(5,3).reshape(5,3)

# create shared memory array from numpy array
if __name__ == '__main__':
    make_shared_array(np_array, name='my_shared_array')
    
# get process safe shared memory array as numpy array
shared_np_array = get_shared_array('my_shared_array')
print(shared_np_array)
```

### Installation

```bash
pip install git+https://github.com/widmi/multiprocess-shared-numpy-arrays
```

