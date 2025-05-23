# 🍿 SoulScript

**SoulScript** is a spiritual web app that lets users explore verses from the **Bhagavad Gita** and **Bible** — supporting daily inspiration and custom verse search. Built using Flask with a clean UI and interactive side navigation.

---

## 🔮 Features

* ✨ **Daily Verse Display**
  Shows a random verse from the Gita and Bible every day.

* 📖 **Custom Verse Search**
  Users can search for specific verses:

  * Bible: via reference (e.g., John 3:16)
  * Gita: by chapter and verse number (e.g., Chapter 7, Verse 14)

* 🔐 **User Authentication**
  Login and signup forms with basic credential validation.

* 🗭 **Sidebar Navigation**
  Responsive sidebar toggle menu to access main pages:

  * Daily Verse
  * Custom Bible Verse
  * Custom Gita Verse
  * Logout

* 🖼️ **Beautiful UI**
  Backgrounds and styles consistent across login, signup, and verse pages.

---

## 📁 Directory Structure

```
SoulScript/
│
├── app.py                      # Main Flask app
├── templates/                 # HTML templates
│   ├── login.html
│   ├── signup.html
│   ├── daily_verse.html
│   ├── custom_bible_verse.html
│   └── custom_gita_verse.html
│
├── static/                    # CSS + image assets
│   ├── login.css
│   ├── signup.css
│   ├── daily_verse.css
│   ├── custom_gita_verse.css
│   └── login_signup.jpg
│
├── utils/                     # Verse fetchers
│   ├── christianity/
│   │   └── random_bible_verse.py
│   └── hinduism/
│       ├── random_gita_verse.py
│       └── get_gita_verse_by_ref.py
│
├── data/                      # Verse datasets
│   ├── bhagavad_gita.csv
│   └── bible.csv
│
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend**: Python + Flask
* **Frontend**: HTML5, CSS3 (custom styles)
* **Dataset**: Bhagavad Gita and Bible CSVs
* **User Auth**: Basic session handling
* **Deployment**: Currently in local dev

---

## 🙌 Upcoming Features

* 🧠 **AI Chat** — Talk to a spiritually trained AI across Gita and Bible
* 🌐 **Multi-language Support**

---

## 🧘‍♂️ Credits

Created with 💛 by Sandeep Koirala
Faith-bridging through technology 🌏
