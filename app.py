from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, BooleanField, validators
from compute import compute


app = Flask(__name__)

# Model
class InputForm(Form):
    ticker = StringField(validators=[validators.InputRequired()])
    p1 = BooleanField()
    p2 = BooleanField()
    p3 = BooleanField()
    p4 = BooleanField()

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
  form = InputForm(request.form)
  if request.method == 'POST' and form.validate():
      ticker = form.ticker.data
      p1 = form.p1.data
      p2 = form.p2.data
      p3 = form.p3.data
      p4 = form.p4.data
      Cols = []
      if p1:
          Cols.append('Close')
      if p2:
          Cols.append('Adj_Close')   
      if p3:
          Cols.append('Open')
      if p4:
          Cols.append('Adj_Open')
	  s = compute(ticker, Cols)
	  print "Hello initial"
	  return render_template("view_output.html", form=form, s=s)
  else:
      return render_template("view_input.html", form=form)
  #return render_template('index.html')

if __name__ == '__main__':
  #app.run(port=33507)
  app.run(debug=True)
