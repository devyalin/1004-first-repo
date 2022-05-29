import requests
respone = requests.post('http://127.0.0.1:5001/whatismyname')
expected = "saved new car"
assert expected == respone.text
print(respone.text)