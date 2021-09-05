from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
@app.route('/home')
@app.route('/about')
@app.route('/services')
@app.route('/portfolio')
@app.route('/testimonials')
@app.route('/contact')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
