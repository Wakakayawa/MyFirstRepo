def slice_with_step(mylist, start, step):
    result = mylist[start::step]
    return result
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_index = 2
step_size = 3
result = slice_with_step(example_list, start_index, step_size)
print("提取的子列表:", result)