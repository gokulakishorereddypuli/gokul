from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"

@app.route("/", methods=["POST", "GET"])
def home():
  return "<h>Hellow Welcome</h>"

if __name__ == "__main__":
    app.run(debug=True)
