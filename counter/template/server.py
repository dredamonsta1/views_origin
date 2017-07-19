from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1
@app.route('/')
def index():
  sumSessionCounter()
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   sumSessionCounter()
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   # redirects back to the '/' route
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
@app.route('/result')
def show():
    return render_template("result.html")

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], la=session['location'])
app.run(debug=True) # run our server
