from flask import Flask
from dao import DAO
app = Flask(__name__)
@app.route('/arquivo/<int:id>')
def helloword(id):
    c = buscar(id)
    return "Dados <br/> {}".format(c)



def main():
    app.env='development'
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()