import flaskmethods as f
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("main.html")
  
@app.route("/test", methods = ["POST", "GET"])
def test():
  if request.method == "POST":
    hi = request.form["input"]
    return render_template("test.html", hi = hi)
@app.route("/cart", methods = ["POST", "GET"])
def cart():
  return render_template("cart.html")
@app.route("/membership", methods = ["POST", "GET"])
def membership():
  if request.method == "GET":
    return render_template("membership.html")
  else: 
    if "membership" in request.form:
      f.createmembership()
      return redirect("/")
    if "createmembership" in request.form:
      return render_template("membership.html") #type in the chat, cause whenever u type here it dont work
    
    
if __name__ == "__main__":  
  app.run(debug = True, host = '0.0.0.0')
