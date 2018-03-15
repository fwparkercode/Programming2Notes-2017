import time
import random


def insertion_sort(l):
    is_outer_count = 0
    is_inner_count = 0
    for key_pos in range(1, len(l)):
        key_value = l[key_pos]
        scan_pos = key_pos - 1  # look to the dancer on the left
        is_outer_count += 1
        while (scan_pos >= 0) and (l[scan_pos] > key_value):
            l[scan_pos + 1] = l[scan_pos]
            scan_pos -= 1
            is_inner_count += 1

        # now everything is shifted to make room for the key_value
        l[scan_pos + 1] = key_value
    print('insertion sort outer:', is_outer_count)
    print('insertion sort inner:', is_inner_count)
    return l


def selection_sort(l):
    ss_outer_count = 0
    ss_inner_count = 0
    for cur_pos in range(len(l)):
        min_pos = cur_pos
        ss_outer_count += 1
        for scan_pos in range(cur_pos + 1, len(l)):
            if l[scan_pos] < l[min_pos]:
                min_pos = scan_pos
            ss_inner_count += 1
        l[cur_pos], l[min_pos] = l[min_pos], l[cur_pos]
    print('selection sort outer:', ss_outer_count)
    print('selection sort inner:', ss_inner_count)
    return l






