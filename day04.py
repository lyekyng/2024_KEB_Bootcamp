#연습문제 3
e2f = dict(dog = "chien", cat = "chat", walrus = "morse")
fe2 = dict((value, key) for key, value in e2f.items())
print(e2f)