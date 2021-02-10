from flask import Flask, render_template, request, flash, session
from pytube import YouTube
import time
from googletrans import Translator

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

@app.route('/synth')
def synth():
    return render_template("synth.html")

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    session['choose_language']= ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Belarusian', 'Bengali',
                                 'Bosnian', 'Bulgarian', 'Catalan', 'Chinese', 'Croatian', 'Czech', 'Danish',
                                 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French',
                                 'Galician', 'German', 'Greek', 'Hawaiian', 'Hebrew', 'Hindi', 'Hungarian',
                                 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Lao',
                                 'Latin', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Maltese', 'Maori',
                                 'Mongolian', 'Nepali', 'Norwegian' 'Persian', 'Polish', 'Portuguese', 'Romanian',
                                 'Russian', 'Serbian', 'Slovenian', 'Somali', 'Spanish', 'Swedish', 'Tajik',
                                 'Tamil', 'Thai', 'Turkish', 'Ukrainian', 'Vietnamese', 'Zulu']

    if request.method == "POST":
        lan = request.form.get('drop')
        text = request.form['trans']

        if text == '':
                flash('please fill the box')
        else:
                translator = Translator()
                output = translator.translate(text, dest=lan)
                output = output.text
                return render_template("translate.html", **locals()) 

    return render_template("translate.html") 

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)



