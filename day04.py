def search():
    word = input("search for ... ")
    if word in dictionary :
        print(f"the meaning of the {word} is {dictionary[word]}")
def add():
    eng = input("add the word ... ")
    kor = input("the meaning is ... ")
    dictionary[eng] = kor
def delete():
    delWord = input("you want to delete ... ")
    if delWord in dictionary:
        del dictionary[delWord]
    print(f"Word '{delWord}' deleted complete")

def printAll():
    for word, meaning in dictionary.items():
        print(f"the Word {word}'s meaning :: {meaning} ")


dictionary = {}

while True :
    put = int(input("1)단어 검색 2)단어 추가 3)단어 삭제 4)모든 단어 출력 5)종료 : "))
    if put == 1:
        search()
    elif put == 2:
        add()
    elif put == 3:
        delete()
    elif put == 4:
        printAll()
    elif put == 5:
        print('quit program')
        break
    else:
        print("wrong input")








