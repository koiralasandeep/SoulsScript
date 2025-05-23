# 🍿 SoulScript

**SoulScript** is a spiritual web app that lets users explore verses from the **Bhagavad Gita** and **Bible** — supporting daily inspiration and custom verse search and also talk to the AI and share their problems and get the solutions. Built using Flask with a clean UI and interactive side navigation.

---

## 🔮 Features

* ✨ **Daily Verse Display**
  Shows a random verse from the Gita and Bible every day.

* 📖 **Custom Verse Search**
  Users can search for specific verses:

  * Bible: via reference (e.g., John 3:16)
  * Gita: by chapter and verse number (e.g., Chapter 7, Verse 14)
 
* ✨ **AI Guru**
   * Talk to AI guru

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
│   ├── ai_guru.html
├── static/                    # CSS + image assets
│   ├── login.css
│   ├── signup.css
│   ├── daily_verse.css
│   ├── custom_gita_verse.css
│   └── login_signup.jpg
│   ├── ai_guru.css
├── utils/                     # Verse fetchers
│   ├── christianity/
│   │   └── random_bible_verse.py
│   └── hinduism/
│       ├── random_gita_verse.py
│       └── get_gita_verse_by_ref.py
│   ├── ai_guru
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
## ⚙️ Screenshots
<img width="1708" alt="Screenshot 2025-05-23 at 1 54 02 AM" src="https://github.com/user-attachments/assets/047a2385-3b4a-4e69-9165-8b052f788309" />

<img width="1708" alt="Screenshot 2025-05-23 at 1 54 28 AM" src="https://github.com/user-attachments/assets/16e08cb7-d1e6-4349-b11d-38a798e74f1d" />

<img width="1708" alt="Screenshot 2025-05-23 at 1 54 49 AM" src="https://github.com/user-attachments/assets/a857f144-c12b-449f-bc89-bd19c5fd62a0" />

<img width="1708" alt="Screenshot 2025-05-23 at 1 55 11 AM" src="https://github.com/user-attachments/assets/01edc69c-db4a-474a-89ea-4bff029808b5" />

<img width="1708" alt="Screenshot 2025-05-23 at 1 55 36 AM" src="https://github.com/user-attachments/assets/70b4d9e1-3462-4726-adc0-ce61db3c2963" />

<img width="1708" alt="Screenshot 2025-05-23 at 1 57 37 AM" src="https://github.com/user-attachments/assets/1ac55c49-58e1-4240-bf3d-605afe97cde1" />

## 🙌 Upcoming Features

* 🌐 **Multi-language Support**

---

## 🧘‍♂️ Credits

Created with 💛 by Sandeep Koirala
Faith-bridging through technology 🌏
