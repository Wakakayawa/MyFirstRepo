def reverse_list(input_list):
    # 使用切片操作反转列表
    reversed_list = input_list[::-1]
    return reversed_list
example_list = [1, 'ab', 3, 4.21, "中"]
result = reverse_list(example_list)
print("反转后的列表:", result)