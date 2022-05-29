def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age can not be negative")

a = input("Enter Name : ")
def check_my_number(num):
    a = ""
    try:
        a = (num)
    except ValueError:
        return False
    if str(num).isdecimal() or str (num).isdigit():
        return True
