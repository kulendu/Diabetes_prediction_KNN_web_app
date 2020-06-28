from flask import Flask, render_template, request
import pickle


model = pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def diabetes():
    
    if request.method == 'POST':
        preg = float(request.form['preg'])
        glucose = float(request.form['glucose'])
        bloodpres = float(request.form['bloodpres'])
        skinthick = float(request.form['skinthick'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = float(request.form['age'])

        predict = model.predict([[preg,glucose,bloodpres,skinthick,insulin,bmi,dpf,age]])

        
        if predict == 1:
            return render_template("index.html", predictions="The Person is diagnosed with Diabetes" )
        else:
            return render_template("index.html", predictions="The Person is not diagnosed with Diabetes")

    


if __name__ == '__main__':
    app.run(debug=True)
    