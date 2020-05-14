# LAB 6: Comparison Sorts
# CPE 202 | Spring 2020
# Bethany Zeya Longid

import random
import time


def selection_sort(alist):
    """Uses selection method to sort a list of numbers.
    Attributes:
        alist (list): A list of unsorted numbers.
    Retrurns:
        comps (int): The number of comparisons made.
    Author:
        Bethany Zeya Longid
    """
    sorted_index = len(alist) - 1 # points to the next spot to put max_val
    comps = 0
    max_val = alist[0]
    while sorted_index >= 0:
        for i in range(sorted_index+1):
            comps += 1
            if alist[i] > max_val:
                max_val = alist[i]
        alist[sorted_index], alist[alist.index(max_val)] =\
            alist[alist.index(max_val)], alist[sorted_index]
        sorted_index -= 1
    return comps

def quick_sort(alist):
    """Uses 3-way quick method to sort a list of numbers.
    Attributes:
        alist (list): A list of unsorted numbers.
    Retrurns:
        comps (int): The number of comparisons made.
    Author:
        Bethany Zeya Longid
    """
    comps = 0
    lo = 0
    hi = len(alist) - 1
    lt = lo
    gt = hi
    pivot = alist[(lo+hi)//2]
    alist[lo], alist[pivot] = alist[pivot], alist[lo]
    i = lt
    while i in range(gt+1):
        comps += 1
        if alist[i] < pivot:
            alist[lt], alist[i] = alist[i], alist[lt]
            lt += 1
            i += 1
        elif alist[i] > pivot:
            alist[gt], alist[i] = alist[i], alist[gt]
            gt -= 1
        else: #if alist[i] == pivot
            i += 1
    return comps