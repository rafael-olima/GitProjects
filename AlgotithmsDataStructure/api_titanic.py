from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import pandas as pd
import pickle
from pydantic import BaseModel

app = FastAPI(title="Titanic API")

@app.get("/")
def homepage():
    html = """
    <html>
    <head><title>Test API</title></head>
    <body>
        <h1> Welcome to the Titanic API</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)

class Input(BaseModel):
    pclass: int
    sex: int
    age: int
    sibSp: int
    parch: int
    embarked: str


@app.post('/predict')
def predict_titanic(input : Input):
    pipe = pickle.load(open('titanic-pipe.pkl','rb'))

    columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch','Embarked']
    print("Input",input)
    X = pd.DataFrame(data=[[input.pclass,input.sex,input.age,input.sibSp,input.parch,input.embarked]], columns=columns)
    print(X)

    prediction = pipe.predict(X)

    pred = int(prediction[0])

    return {'prediction': pred,
            'status':'OK'}

if __name__ == "__main__":
    uvicorn.run("api_titanic:app",
                host="127.0.0.1",
                port=8000,
                reload=True)

# http://127.0.0.1:8000/docs para acessar a documentacao.