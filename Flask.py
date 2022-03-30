from flask import Flask, request, render_template, make_response
import json
import pandas as pd

app = Flask(__name__)



@app.route("/")
def hello_word():
    return "Hello, World!"

@app.route("/name")
def helloking():
    return "Hello, king!"

##api
@app.route("/request",methods=['POST'])
def request_detail():
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)
    
    print(inmessage)
    
    json_data = json.dumps({'y':'received!'})
    return json_data

##web
@app.route("/home",methods=['POST','GET'])
def home():
    if request.method == "POST":
        dbpd = pd.read_csv('db.csv')
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        
        dbpd = dbpd.append({'name':first_name,'lastname':last_name}, ignore_index=True)
        dbpd.to_csv('db.csv',index=False)
        
        resp = make_response(render_template('home.html',name = f"{first_name} {last_name}",fav =""))
        resp.set_cookie('firstname',first_name)
        
        return resp   
    
    if request.method == 'GET':
        getval = request.args
        print(getval)
        print(getval.get('name'))
    return render_template("home.html",name = 'king')
@app.route('/home2',methods=['POST','GET'])
def home2():
    if request.method == "POST":
        ratio_choice = request.form.get("for_y")
        return render_template('home.html',ratio = f"{ratio_choice}")
    
    
    return render_template("home.html",name = 'king',ratio= '99h')

if __name__=="__main__":
    app.run()#host='0.0.0.0'  host='0.0.0.0', port=5001