# https://www.codewars.com/kata/55b4f9906ac454650900007d/train/python

"""
You should write a function that takes a string and a positive integer n, 
splits the string into parts of length n and returns them in an array. 
It is ok for the last element to have less than n characters.

If n is not a number or not a valid size (> 0) (or is absent), you should return an empty array.

If n is greater than the length of the string, you should return an array 
with the only element being the same string.
"""

def string_chunk(st, n):
    res = list()
    for i in range(0,len(st),n):
        res.append(st[i:i+n])
    return res