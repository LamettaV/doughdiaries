from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        # Form is valid and can be processed
        name = form.name.data
        email = form.email.data
        # Process the form data, e.g., save to database or send email
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('index'))
    elif form.is_submitted() and not form.validate():
        flash('Form submission failed. Please correct the errors and try again.', 'danger')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
