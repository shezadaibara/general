import random


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]


def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j + 1] = items[j + 1], items[j]
            j -= 1


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) / 2
    left = items[0:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(_merge(left, right))


def _merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(left[l])
            r += 1
    if left:
        result.extend(left[l:])
    if right:
        result.extend(right[r:])
    return result


def quick_sort(items):
    if len(items) <= 1:
        return items
    result = []
    pivot_index = len(items) / 2
    less = []
    more = []
    for i, val in enumerate(items):
        if i != pivot_index:
            if val < items[pivot_index]:
                less.append(val)
            else:
                more.append(val)
    quick_sort(less)
    quick_sort(more)
    

if __name__ == '__main__':
    items = [random.randint(-50, 100) for x in range(32)]
    print items
    bubble_sort(items)
    print items
