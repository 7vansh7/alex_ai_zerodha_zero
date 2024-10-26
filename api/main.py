from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from zero_model import zero_chat

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/zero_chat') 
def zero(question:str = Form(...)):
    res = zero_chat.send_message(question)
    print(res.candidates)
    return {"question":question,"answer":res.text}


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000,reload=True)

