from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

@app.get('/')
def simple_resp(name: str = Query('Recruto'), message: str = Query('Давай дружить')):
    
    text = f'Hello {name}! {message.capitalize()}!'
    
    return HTMLResponse(text)