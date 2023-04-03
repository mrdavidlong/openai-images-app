import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        description = request.form["description"]
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="256x256",
            response_format="url",
        )
        return redirect(url_for("index", result=response.data[0].url))

    result = request.args.get("result")
    return render_template("index.html", result=result)