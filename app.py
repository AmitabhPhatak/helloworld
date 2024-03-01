from flask import Flask
import os
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
#model = pickle.load(open('model_lr_ch1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
     output=0.9  
    #output = prediction[0]

    return render_template('index.html', prediction_text='CHD would be  $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])
    output=0.9 
    #output = prediction[0]
    return jsonify(output)

    app.run(port=port,host='0.0.0.0')