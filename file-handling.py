# file = open('test.txt', 'w')

# with open("test.txt", 'r') as file:
#     for item in file:
#         print(item)


def fileOpener(fileName, openMode):
    with open(fileName, openMode) as file:
        for line in file:
            print(line)


fileName = input("Enter the filename or path: ")
openMode = input("Open Mode? [w, r]: ")


fileOpener(fileName, openMode)
