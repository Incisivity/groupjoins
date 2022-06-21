import requests
f = input("Enter Username: ")
url = "https://api.roblox.com/users/get-by-username?username=" + f
r = requests.get(url)
a = open("out.txt", "a")
a.write(r.text)
