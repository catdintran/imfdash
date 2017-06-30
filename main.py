from flask import Flask, render_template
app = Flask(__name__)

from random import randint

@app.route('/')
def hello_world():
  version = randint(0,1000)
  return render_template("index.html", version=version)

if __name__ == '__main__':
  app.run()


