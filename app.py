from flask import Flask,request,jsonify,render_template

app=Flask(__name__)  #app name we can give any

#route 1
@app.route('/welcome')  
def hello_world():
    return "<h1>hello world</h1>"

#route 2
@app.route('/test_operation',methods=['POST'])   #testing this using postman
def math_operations():
    if request.method == 'POST':
        ope=request.json['operation']  # getting variables from json object
        num1=request.json['num1']
        num2=request.json['num2']
        # return f"the sum is {num1+num2}"

        if ope=='add':
            return jsonify(f"the {ope} is :{num1+num2}")
        elif ope=='sub':
            return jsonify(f"the {ope} is :{num1-num2}")
        elif ope=='mul':
            return jsonify(f"the {ope} is :{num1*num2}")
        elif ope=='div':
            return jsonify(f"the {ope} is :{num1/num2}")
        else:
            return "wrong operation"

#route 3
@app.route('/')  
def get_homepage():
    return render_template("index.html") # render the index.html page


#route 4        # for web app
@app.route('/operation',methods=['POST'])   #testing this using postman
def get_operations():
    if request.method == 'POST':
        ope=request.form['operation']  # getting variables from json object
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        # return f"the sum is {num1+num2}"

        if ope=='add':
            result =f"the {ope} is :{num1+num2}"
        elif ope=='sub':
            result =f"the {ope} is :{num1-num2}"
        elif ope=='mul':
            result =f"the {ope} is :{num1*num2}"
        elif ope=='div':
            result =f"the {ope} is :{num1/num2}"
        else:
            result ="wrong operation"

        # return result
        return render_template("result.html",result=result)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)