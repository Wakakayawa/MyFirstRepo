class Student:
    def __init__(self, name, age, is_single):
        """
        初始化学生信息
        :param name: 学生姓名 (字符串)
        :param age: 学生年龄 (整数)
        :param is_single: 是否单身 (布尔类型)
        """
        self.name = name
        self.age = age
        self.is_single = is_single
        self.grades = []  # 初始化成绩列表为空

    def add_grade(self, grade):
        """
        添加一个成绩到 grades 列表中
        :param grade: 成绩 (整数)
        """
        self.grades.append(grade)

    def average_grade(self):
        """
        计算并返回学生的平均成绩
        :return: 平均成绩 (浮点数)，如果成绩列表为空，返回 0
        """
        if not self.grades:  # 如果成绩列表为空
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """
        返回学生成绩信息的字符串表示
        :return: 格式为 "姓名: {name}, 平均分: {average}"
        """
        average = self.average_grade()
        return f"姓名: {self.name}, 平均分: {average}"

    def print_status(self):
        """
        返回学生是否单身的字符串表示
        :return: 格式为 "姓名: {name}, 年龄: {age}, 单身否: {is_single}"
        """
        return f"姓名: {self.name}, 年龄: {self.age}, 单身否: {self.is_single}"


if __name__ == "__main__":
    student = Student("张三", 20, True)

    student.add_grade(85)
    student.add_grade(90)
    student.add_grade(78)

    print(student)
    print(student.print_status())