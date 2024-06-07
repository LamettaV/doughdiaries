from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        
        # Process the data (for now, just print it)
        print(f"Name: {name}, Email: {email}")
        
        # Redirect to a new page or render a success template
        return redirect(url_for('success'))
    
    return render_template('form.html')

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
