try:

    a=int(input("enter first number : "))
    b = int(input("enter second number: "))
    print (a/b)
    r = open ("file_not_exist.txt")
except ZeroDivisionError:
    print ("could not divide by zero")
except FileNotFoundError:
    print ("file could not be found")
except Exception as e:
    print (e.args)
print ("BLAVLA")