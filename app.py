from flask import Flask,request

app = Flask(__name__) # objects it represents website

@app.route("/") #connects fuctions with specific web page
def home():
    return 'Hello user! This is my first flask app'
@app.route('/about')
def about():
    return 'This is about us page'

@app.route('/contact')
def contant():
    return 'THis is a contact page'
@app.route('/submit',methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "You send data"
    else:
        return "You are only viewing the form"