def getnumber ():
    numberimp = input("Type number : ")
    return numberimp

def calculate (numberimp):
    summary = 0
    digit = len (numberimp)
    for x in str(numberimp):
        summary = summary+(int(x))
    print (summary)


numberimp = getnumber()
calculate (numberimp)