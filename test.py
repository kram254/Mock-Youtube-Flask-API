import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 2000, "name": "How to be Karios", "views": 50000},
#     {"likes": 300, "name": "RestAPis with Flask", "views": 42069},
#     {"likes": 786, "name": "We gonna make it one day", "views": 42069}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/"+ str(i), data[i])
#     print (response.json())

# input()
# response= requests.delete(BASE + 'video/0')
# print(response)
# input()
response = requests.patch(BASE + "video/2", {"views":420, "likes": 69})
print (response.json())

# response = requests.get(BASE + "video/2")
# print (response.json())