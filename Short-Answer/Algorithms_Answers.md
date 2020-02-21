#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time is O(n) because the loop run time is directly related to the size of n


b) The running time is O(n^2) because when N doubles the running time increases by N*N


c) The running time is O(n) because the recursion will only be performed a set number of times

## Exercise II

Define a function that takes in 1 parameter, f, which is the floors in the building
```python
def building(floors):
    pass
```
The question states that an egg only breaks if its thrown off of floors f or higher, so if we take f - 1, no eggs will break
```python
    return floors - 1
```
