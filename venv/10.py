def validate(prompt, low , high, ok, not_ok):
    input_from_user = int (input(prompt))
    if low <  input_from_user < high:
        return ok
    else:
        return not_ok

a = 4
def moshe():
    print(a)

print(validate("Enter your age: ", 0, 120, "age is ok", "age is not ok" ))
print (validate ("enter amount of pets", 0, 4, "you are a good person", " you are not a good person"))
