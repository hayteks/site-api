from app import app

@app.route('/')
def index():
    return "seja bem vindo!!"