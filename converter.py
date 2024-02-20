# function to convert temperature
def temp_converter(temp_from, temp_to, temp_value):
    # converting farenheit to degree celcius
    if (temp_from == "FARENHEIGHT" and temp_to == "DEGREE"):
        temp = temp_value - 33.5
        print(f"{temp_value} FarenHeight is equivalent to {temp} degree celcius!")
    elif (temp_from == "DEGREE" and temp_to == "FARENHEIGHT"):
        temp = temp_value + 33.5
        print(f"{temp_value} FarenHeight is equivalent to {temp} degree celcius!")
    else:
        print("Invalid input")


temp_from = input(
    "Are you converting from 'FarenHeight' or 'Degree': ").upper()
temp_to = input("Are you converting to 'FarenHeight' or 'Degree': ").upper()
temp_value = float(input("Enter temp value: "))

temp_converter(temp_from, temp_to, temp_value)
