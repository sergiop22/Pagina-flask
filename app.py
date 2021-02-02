from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

'''   
@app.route('downloader/')
def downloader():
    return render_template("downloader.html")

@app.route('encrypt/')
def encrypt():
    return render_template("encrypt.html")

@app.route('translate/')
def translate():
    return render_template("translate.html") '''

if __name__ == '__main__':
    app.run(debug=True)



