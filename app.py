from flask import Flask, request, jsonify ,render_template
import pickle

app=Flask(__name__)

#loading the model
with open('model/model.pkl','rb') as f:
    model=pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        input_features = [[cgpa, iq]]
        prediction = model.predict(input_features)
        result = 'Placed' if prediction[0] == 1 else 'Not Placed'
        message = f'Student is predicted as "{result}".'
        return render_template('index.html', result=message, cgpa=cgpa, iq=iq)

    except KeyError as e:
        error_message = f"Missing input: {str(e)}"
        return render_template('index.html', error=error_message,
                               cgpa=request.form.get('cgpa', ''),
                               iq=request.form.get('iq', ''))
    except Exception as e:
        return render_template('index.html', error=str(e),
                               cgpa=request.form.get('cgpa', ''),
                               iq=request.form.get('iq', ''))

if __name__=='__main__':
    app.run(debug=True)
