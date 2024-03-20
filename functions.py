# declaring a function
def greetings(name):
    if (name == "John"):
        print("I'm not sure I like John")

    elif (name == "Paul"):
        print("Paul is a great footballer!")

    elif (name == "Jane"):
        print("Welcome home!")

    else:
        print("I don't know that person")


# name = input("Enter a name: ")

# calling a function
# greetings(name)

def sum(num1, num2):
    return (num1 + num2)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(sum(num1, num2))

scores = []


def grading():
    while True:
        score = int(input("Enter student score: "))
        scores.append(score)
