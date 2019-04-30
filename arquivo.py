from flask import Flask
app = Flask(__name__)
@app.route('/arquivo/<int:a>/<int:b>')
def helloword(a,b):
    c = soma(a,b)
    return "soma: {} <br/> A: {} + B: {}".format(c,a,b)


def soma(a,b):
    return a+b

def main():
    app.env='development'
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()