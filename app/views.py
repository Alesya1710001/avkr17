
from app import app, db
from flask import request
from flask import render_template

from models import Form


@app.route('/')
def form():
  return render_template('form.html', name=__name__)

@app.route('/form_values')
def form_values():
  names = Form.query.all()
  return render_template('formValues.html', names=names)

@app.route('/submit', methods=['POST'])
def submit_form():
  name_list = []
  for key in request.form:
    name_list.append(request.form[key])

  form = Form(name_list)
  db.session.add(form)
  db.session.commit()
  
  return render_template('form.html', name=__name__)
