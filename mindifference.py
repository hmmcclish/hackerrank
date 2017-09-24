#!/bin/python

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    min_difference = float('inf')
    for x in range(n -1):
        if abs(arr[x] - arr[x+1]) < min_difference:
            min_difference = abs(arr[x] - arr[x+1])
    return min_difference


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print minimumAbsoluteDifference(n, arr)
