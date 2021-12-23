from flask import Flask, request, render_template
import pickle
import json
import numpy as np


app = Flask(__name__)

def get_predict_profit(r_d_expenses, administration_expenses, marketing_expenses, state):
    """
    * method: get_predict_profit
    * description: method to predict the results
    * return: prediction result
    *
    * Parameters
    *   r_d_expenses: R&D spent
    *   administration_expenses: admin cost
    *   marketing_expenses: marketing expenses
    *   state: state name
    """
    with open('models/profit_prediction_model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open("models/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']


    try:
        state_index = data_columns.index('state_'+str(state).lower())
    except:
        state_index = -1

    x = np.zeros(len(data_columns))
    x[0] = r_d_expenses
    x[1] = administration_expenses
    x[2] = marketing_expenses
    if state_index >= 0:
        x[state_index] = 1

    return round(model.predict([x])[0], 2)

@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    * method: predict
    * description: method to predict
    * return: index.html
    *
    * Parameters
    *   None
    """
    if request.method == 'POST':
        r_d_expenses = request.form['r_d_expenses']
        administration_expenses = request.form["administration_expenses"]
        marketing_expenses = request.form["marketing_expenses"]
        state = request.form["state"]
        output = get_predict_profit(r_d_expenses, administration_expenses, marketing_expenses, state)
        return render_template('index.html', show_hidden=True, prediction_text='Startup Profit must be $ {}'.format(output))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=False)