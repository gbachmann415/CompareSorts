import time
import random
from merge_sort import merge_sort
from quick_sort import quick_sort


MAX_NUM = 300


def bumper_sort(data, k):
    hist = [0] * (k+1)
    for v in data:
        hist[v] += 1
    result = []
    i = 0
    while i < len(hist):
        count = hist[i]
        while count > 0:
            result.append(i)
            count -= 1
        i += 1
    return result


def test():
    small_list = [2, 5, 3, 0, 2, 3, 0, 3]
    big_list = []
    for i in range(1000):
        big_list.append(random.randrange(0, 300))

    print("Small list, unsorted: ", small_list)
    print("Small list, bump-sorted: ", bumper_sort(small_list, MAX_NUM))
    print("Big list, unsorted: ", big_list)
    print("Big list, bump-sorted: ", bumper_sort(big_list, MAX_NUM))

    print("")

    print("Sorting a randomized list of 1000 elements.")
    thousand_list = []
    for i in range(1000):
        thousand_list.append(random.randrange(0, 300))

    start_small_merge = time.process_time()
    answer_small_merge = merge_sort(thousand_list)
    end_small_merge = time.process_time()
    print("merge_sort time: ", end_small_merge - start_small_merge, "seconds")

    start_small_quick = time.process_time()
    answer_small_quick = quick_sort(thousand_list)
    end_small_quick = time.process_time()
    print("quick-sort time: ", end_small_quick - start_small_quick, "seconds")

    start_small_bumper = time.process_time()
    answer_small_bumper = bumper_sort(thousand_list, MAX_NUM)
    end_small_bumper = time.process_time()
    print("bumper-sort time: ", end_small_bumper - start_small_bumper, "seconds")

    """start_small_sort = time.process_time()
    answer_small_sort = thousand_list.sort()
    end_small_sort = time.process_time()
    print("sorted time: ", end_small_sort - start_small_sort, "seconds")"""

    print("")

    print("Sorting a randomized list of 1000000 elements.")
    million_list = []
    for i in range(1000000):
        million_list.append(random.randrange(0, 300))

    start_big_merge = time.process_time()
    answer_big_merge = merge_sort(million_list)
    end_big_merge = time.process_time()
    print("merge_sort time: ", end_big_merge - start_big_merge, "seconds")

    start_big_quick = time.process_time()
    answer_big_quick = quick_sort(million_list)
    end_big_quick = time.process_time()
    print("quick-sort time: ", end_big_quick - start_big_quick, "seconds")

    start_big_bumper = time.process_time()
    answer_big_bumper = bumper_sort(million_list, MAX_NUM)
    end_big_bumper = time.process_time()
    print("bumper-sort time: ", end_big_bumper - start_big_bumper, "seconds")

    """start_big_sort = time.process_time()
    answer_big_sort = million_list.sort()
    end_big_sort = time.process_time()
    print("sorted time: ", end_big_sort - start_big_sort, "seconds")"""



test()