numbers = input("请输入一系列逗号分隔的数字: ")
num_list = [int(num) for num in numbers.split(",")]
print("列表中的偶数有:")
for num in num_list:
    if num % 2 == 0:
        print(num)