from flask import Flask,render_template,request
import firebase_admin
from firebase_admin import credentials,db

app=Flask(__name__)
cred=credentials.Certificate("C:/Users/Ashish/OneDrive/Desktop/python3.10/ishwari-e06de-firebase-adminsdk-fbsvc-99ad2fa7d1.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred,{"databaseURL":"https://ishwari-e06de-default-rtdb.firebaseio.com/"})

@app.route('/',methods=['GET','POST'])
def calculator():
    result=''
    if request.method=='POST':
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        op=request.form['operation']

        if op=='add':
            result =num1+ num2
            operation=f"{num1}+{num2}={result}"
        elif op =='sub':
            result= num1-num2
            operation=f"{num1}-{num2}={result}" 
        elif op =='mul':
            result= num1*num2
            operation=f"{num1}*{num2}={result}"     
        elif op =='div':
            result= num1/num2 if num2 !=0 else 'error'
            operation=f"{num1}/{num2}={result}"

        #push to firebase realtime database
        if result !='error':
            ref=db.reference('calculations')
            ref.push({'result':result,'operation':operation})

    return render_template('index.html', result=result)                   


if __name__=="__main__":
    app.run(debug=True)
    