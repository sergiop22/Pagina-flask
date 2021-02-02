from flask import Flask, render_template, request, flash
from pytube import YouTube
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sergiosergio'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/downloader', methods=['GET', 'POST'])
def downloader():
    if request.method =='POST':
        url = request.form['url']
        if url == "":
            flash('Error, Please Paste Video URL')
        elif 'https://' not in url:
            flash('Error, Wrong Video Url')
        else:
            try:
                yt = YouTube(url)
                stream = yt.streams.first()
                stream.download()
                flash('Video has been download successfully')
            except:
                flash('Error, Something wrong with URL')

    return render_template("downloader.html")

@app.route('/encrypt')
def encrypt():
    return render_template("encrypt.html")

@app.route('/translate')
def translate():
    return render_template("translate.html") 

if __name__ == '__main__':
    app.run(debug=True)



