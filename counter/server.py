from flask import Flask, session, render_template, url_for, request, redirect

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1
@app.route('/')
def index():
    # Initialise the counter, or increment it
    sumSessionCounter()
    return render_template('index.html')
@app.route('/form')
def form():
  sumSessionCounter()
  # if a name has been sent, store it on a session variable
  if request.args.get('yourname'):
    session['name'] = request.args.get('yourname')
    # And then redirect the user to the main page
    return redirect(url_for('index'))
  else:
    # If no name has been sent, show the form
    return render_template('form.html', session=session)

# This dummy page will just load the session data
@app.route('/page1')
def page1():
  session['counter'] = session['counter'] + 1
  # if is sset name, store it on session
  return render_template('page1.html')

# This dummy page will just load the session data
@app.route('/page2')
def page2():
  session['counter'] = session['counter'] + 1
  # if is sset name, store it on session
  return render_template('page2.html')
@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('index'))
app.run(debug=True)
