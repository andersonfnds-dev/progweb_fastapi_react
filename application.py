from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def ola():
    print('Olá mundo, fiz meu primeiro endpoint com fastAPI')
    return 'Olá mundo, fiz meu primeiro endpoint com fastAPI'

@app.get('/name')
def typeName(name: str):
    
    return 'The user name is: ' + name

@app.get('/bookDictionary')
def bookDictionary():
    books = [{"bookName" : "Dune",
              "author" : "Frank Herbert"
              },
            {"bookName" : "Lord of the Rings",
              "author" : "J. J. R. Tolkien"
              },
            {"bookName" : "Foundation",
              "author" : "Isaac Asimov"
              }]
    return books

@app.post('/sendLogin')
def loginData(username: str, password: str):
    
    return 'Login data sent with success'

uvicorn.run(app, port=7777)