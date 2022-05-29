def get_name():
    n=input(" Enter your name: ")
    my_file = open(name.txt, "a")
    my_file.write(f"{n}\n")

def show_names():
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print (f"hello {line}", end='')

def call_urls():
    with open ("url.txt") as urls:
        for line in urls.readlines()
            url_caller[line.strip()]


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")

