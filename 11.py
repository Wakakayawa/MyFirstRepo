import time
import random
def sort_small_data():
    data = [5, 3, 9, 1, 8, 4, 7, 2, 6, 10, 15, 12, 18, 11, 14, 13, 17, 16, 20, 19]
    start_time = time.time()
    sorted_data = sorted(data, reverse=True)
    end_time = time.time()
    print("排序后的数据（20个）:", sorted_data)
    print("执行时间:", end_time - start_time, "秒")
def sort_large_data():
    data = [random.randint(1, 10000000) for _ in range(20000000)]
    start_time = time.time()
    sorted_data = sorted(data, reverse=True)
    end_time = time.time()
    print("执行时间（2千万个数据）:", end_time - start_time, "秒")