import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'Hello': 'это мое первое приложение на  FastAPI'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)