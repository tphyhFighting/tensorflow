#!/usr/bin/env python
# coding=utf8
#bubble sort 平均的时间复杂度为O(n**2)，平均的空间复杂度为O(1)
#其实理解冒泡排序就可以根据这种现象来理解：每一次遍历，都把大的往后面排（当然也可以把小的往后面排），所以每一次都可以把无序中最大的（最小）的元素放到无序的最后面（或者说有序元素的最开始）


def bubble_sort(numbers):
    for i in range(1,len(numbers)):
        for j in range(len(numbers)-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print "numbers:",numbers
    return numbers

print bubble_sort([23, 12, 9, 15, 6,0])