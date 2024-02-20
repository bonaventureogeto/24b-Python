# for number in range(0, 10):
#     if (number % 2 == 0):
#         print(f"{number} is even!")


# using a for loop, write a python program that prints multiples of 3


numbers = [1, "two", 3, 4.34, 5, "six", 7.8, 8, 9, True]

for number in numbers:
    if (number == "six"):
        print("You got the number!")


students = [("Ken", 23), ("Jen", 2)]


def marks():
    for student in students:
        print(student[1])


marks()
