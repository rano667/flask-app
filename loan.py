from flask import Flask, request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to the Loan Application Service! V2</h1>"

@app.route("/predict", methods=['GET'])
def predict():
    
    return """I will make the prediction for you.<br>
    Please send a POST request with the required data.<br>
    Endpoint:
    http://127.0.0.1:5000/predict <br>
    Sample JSON
    data required:
    ```{
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 200,
        "CreditHistory": 1
    }```
    """


@app.route("/predict", methods=['POST'])
def make_prediction():
    loan_req = request.get_json()
    
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "No":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    CreditHistory = loan_req['CreditHistory']
    LoanAmount = loan_req['LoanAmount']

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]

    pred = model.predict([input_data])

    print(pred)


    if pred[0] == 1:
        pred = "Approved"
    else:
        pred = "Rejected"


    return {"loan_approval_status": pred}



@app.route("/carpredict", methods=['GET'])
def car_predict():
    return "I'll predict the eligibility for Car Loan prediction endpoint"



if __name__ == "__main__":
    app.run(debug=True)