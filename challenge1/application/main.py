import os
from flask import Flask,request,render_template
from requestHandler import make_authorized_get_request

app = Flask(__name__)
endpoint=os.environ.get('SERVENDPOINT')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["name"])
        if request.form["name"] is not None:
            data={"model":request.form["name"]}
            resp=make_authorized_get_request(endpoint,endpoint,data)
            return f"Document stored {resp}!"
        else:
            return "name should contain valid value"

    return render_template("home.html")
   



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))