from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, BooleanField, validators
from compute import compute


app = Flask(__name__)

# Model
class InputForm(Form):
    ticker = StringField(validators=[validators.InputRequired()])
#    ticker = StringField()
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
#  if request.method == 'POST':
      ticker = form.ticker.data
      ticker = ticker.upper()
      p1 = form.p1.data
      p2 = form.p2.data
      p3 = form.p3.data
      p4 = form.p4.data
      cols = []
      if p1:
          cols.append('close')
      if p2:
          cols.append('adj_close')   
      if p3:
          cols.append('open')
      if p4:
          cols.append('adj_open')
      s = True
      s, js_resources, css_resources, script, div = compute(ticker, cols)
      if s:
          return render_template("view_output.html", js_resources=js_resources, css_resources=css_resources, plot_script=script, plot_div=div, ticker=ticker)
      else:
          return render_template("view_error.html")
  else:
      return render_template("view_input.html", form=form)

if __name__ == '__main__':
#  app.run(port=33507)
#    port = int(os.environ.get("PORT", 5000))
#   app.run(host='0.0.0.0')
    app.run()

