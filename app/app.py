from flask import Flask, render_template

app = Flask(__name__)
app.Debug=True

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

#@app.route('/greet/')

#def hello():
#    return 'Hello world'
#print("Hello world")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
