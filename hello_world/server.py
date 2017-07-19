from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# @app.route('/ninjas')
# @app.route('/ninjas/new')
def index():
  return render_template("index.html", phrase="dredamonsta1",times=5)


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojos/new')
def dojo():
    return render_template('dojos.html')
app.run(debug=True)
