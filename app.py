from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

class_dict = {0: 'aple',
              1: 'banana',
              2: 'blackgram',
              3: 'chickpea',
              4: 'coconut',
              5: 'coffee',
              6: 'cotton',
              7: 'grapes',
              8: 'jute',
              9: 'kidneybeans',
              10: 'lentil',
              11: 'maize',
              12: 'mango',
              13: 'mothbeans',
              14: 'mungbean',
              15: 'muskmelon',
              16: 'orange',
              17: 'papaya',
              18: 'pigeonpeas',
              19: 'pomegranate',
              20: 'rice',
              21: 'watermelon'}

@app.route('/')
def index():
    return render_template('index.html', hasil_prediksi_tanaman="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    suhu, kelembaban, phtanah, curahhujan  = [x for x in request.form.values()]

    data = []

    data.append(float(suhu))
    data.append(float(kelembaban))
    data.append(float(phtanah))
    data.append(float(curahhujan))

    prediction = model.predict([data])
    crop_name = class_dict[prediction[0]]
    output = crop_name

    return render_template('index.html', hasil_prediksi_tanaman=output, suhu=suhu, kelembaban=kelembaban, phtanah=phtanah, curahhujan=curahhujan)


if __name__ == '__main__':
    app.run(debug=True)