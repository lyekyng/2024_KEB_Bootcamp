#연습문제 3
e2f = dict(dog = "chien", cat = "chat", walrus = "morse")
f2e = dict((value, key) for key, value in e2f.items())
print(f2e)