import test as t
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("main.html")
@app.route("/test", methods = "POST", "GET")
def test():
  if request.method = "POST":
    hi = request.form["sss"]
    return render_template("test.html", hi = hi)

if __name__ == "__main__":
  app.run(debug = True)

#update please