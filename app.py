from flask import Flask, render_template, request, session, redirect, url_for #lib used for making HTTP requests

#import api
from utils.christianity.bible_api import get_bible_verse

#import files
from utils.hinduism.random_gita_verse import random_gita_verse
from utils.hinduism.custom_gita_verse import get_gita_verse
from utils.christianity.random_bible_verse import random_bible_verse
from utils.ai_guru import get_spiritual_response




app = Flask(__name__)
app.secret_key = 'sandeep'


@app.route('/')
def root():
    return redirect(url_for('login'))


#for login page
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        
        #example login validation
        if user_email == "koiralasa@gmail.com" and user_password == "koiralasa":
            return redirect(url_for('daily_verse'))
        else:
            return render_template('login.html' , error = "Invalid Email or Password")
    
    return render_template('login.html')
        

#for signup page
@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if user_password == confirm_password:
            return redirect(url_for('login'))
        else:
            return render_template('signup.html' , error = "Passwords do not match")
    
    return render_template('signup.html')


#for random gita and bible verse for now
@app.route('/daily_verse')
def daily_verse():
    gita_verse = random_gita_verse()
    bible_verse = random_bible_verse()
    
    return render_template('daily_verse.html', gita_verse = gita_verse, bible_verse = bible_verse)


#for custom_bible_verse page
@app.route('/custom_bible_verse', methods = ["GET", "POST"])
def custom_bible_verse():
    bible_verse = None
    
    if request.method == "POST":
        #Get user question from form
        user_question = request.form.get("question")
        
        #Calling api function
        bible_verse = get_bible_verse(user_question)
        
    # Render the template and pass the verse
    return render_template("custom_bible_verse.html", bible_verse=bible_verse)


#for custom_gita_verse 
@app.route('/custom_gita_verse', methods=['GET', 'POST'])
def custom_gita_verse():
    gita_verse = None
    all_verses = get_gita_verse()  # returns dict of all verses

    if request.method == 'POST':
        user_input = request.form.get('question').strip()
        gita_verse = all_verses.get(user_input, "Verse not found. Please use format like: Chapter 2, Verse 47")

    return render_template('custom_gita_verse.html', gita_verse=gita_verse)


@app.route("/ai_guru", methods=["GET", "POST"])
def chat_with_ai():
    if "conversation" not in session:
        session["conversation"] = []

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            session["conversation"].append({"role": "user", "content": user_input})
            ai_reply = get_spiritual_response(user_input)
            session["conversation"].append({"role": "assistant", "content": ai_reply})

    return render_template('ai_guru.html', conversation=session["conversation"])


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
    
    
