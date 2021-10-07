   ---Binary Search---
# Write a function that takes in a sorted array of integers as well as target integer.
# The function should use binary search algo to determine if the target integer is contained in the array and should return its index if it is, otherwise -1

def solution(arr,target):
    mid=len(arr)//2
    while(mid>=0 and mid<len(arr)):
        if arr[mid]==target:
            return mid
        elif target<arr[mid]: 
            mid=mid//2
        else:
            mid=mid+mid//2
    return -1
