import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(URL)
    # we could do checking for correct response code here
    return response.json()

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    # we could do checking for correct response code here
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    # should check we have the correct status code
    return response.json()

def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    book= {
        'Author':"Booker Wright",
        'Title':"The Name of The Book",
        "Price": 123
    }
    bookdiff= {
        "Price": 1234444
    }
    print(readbooks())
    #print(createbook(book))
    #print(readbook(494))
    #print(updatebook(495, bookdiff))
    #print(deletebook(495))

