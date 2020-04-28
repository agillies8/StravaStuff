from flask import Flask, render_template
from mapGen import createMap

app = Flask(__name__) #create instance of class object

@app.route('/') #decorator
def home():
    createMap()
    return render_template("MapAllActivities.html")

if __name__ == "__main__":
    app.run(debug=True)