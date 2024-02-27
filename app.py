from flask import Flask, request, render_template, send_file, jsonify
import json
import os
import json


path = os.getcwd()+"/apps/GameSnacks"
app = Flask(__name__)

@app.route('/')
def page_home():
    with open(f"{path}/index.html", "r", encoding="utf-8") as f:
        page = f.read()
        f.close()

    return page

# Fichiers
@app.route('/css')
def css():
    return send_file(f"{path}/style.css")

@app.route('/images/logo.png')
def logo():
    return send_file(f"{path}/images/logo.png")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5502)