input_str = input("请输入一系列逗号分隔的数字（可以是整数或浮点数）: ")
num_list = [float(num) if '.' in num else int(num) for num in input_str.split(",")]
total_sum = sum(num_list)
print("列表中所有数字的和为:", total_sum)