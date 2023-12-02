from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/addNew")
def addNew():
    return render_template('addNew.html')

@app.route("/addNewData",methods=('GET', 'POST'))
def addNewData():
    transaction = request.form.get("transaction")
    transactionAmount =   request.form.get("transactionAmount")
    return render_template('addNew.html')

@app.route("/history")
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)