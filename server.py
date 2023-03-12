import os
from flask import Flask
from threading import Thread

HOST = 'HOST' # IP dafault=0.0.0.0
PORT = 'PORT' # Port default=3000

app = Flask('')

@app.route("/")
def home():
    return "Result: [OK]."

def run():
  app.run(host=HOST, port=PORT)

def keep_alive():
  t = Thread(target=run)
  t.start()
