from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    name = "Zidan Amikul Afham"
    npm = "5230411330"
    return render_template('about.html', name=name, npm=npm)

if __name__ == '__main__':
    app.run(debug=True)