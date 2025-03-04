from flask import Flask;

app = Flask(__name__);

#def rota raiz pag inicial e a funcao
@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)