def nametofile ():
    my_file = open("names.txt", "a+")
    yourname = input("Your name:")
    my_file.write(f"{yourname}\n")

def hello ():
    my_file.read(yourname)
    print(f"Hello {yourname}" )




my_file = open("names.txt", "a+")
nametofile()
hello()

my_file.close()