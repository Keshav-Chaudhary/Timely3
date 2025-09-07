# Timely 3
## Class Scheduler
<img width="1894" height="846" alt="image" src="https://github.com/user-attachments/assets/dd39072e-9663-444a-a8e7-cc33b7d5a9b9" />

**Timly 3** is a **modern web-based class scheduling application** built with Flask.
This version introduces a **professional project structure**, **advanced features**, and a **refined UI** to make managing your daily and weekly timetable effortless.

---

## 🚀 Features

* **Dynamic Daily Schedule**
  View today’s classes with *real-time status*: **Upcoming**, **Ongoing**, **Completed**.

* **Full Timetable View**
  See the complete weekly timetable at once.

* **Add & Delete Courses**

  * Add new classes through an intuitive form
  * Delete courses with validation and instant feedback

* **Enhanced Metadata**
  Includes instructor, room(s), type of class (Lecture/Lab/etc.), and notes.

* **Room Parsing**
  Supports multiple rooms (comma-separated input).

* **CSV Export**
  Download your timetable instantly as a `.csv` file.

* **Flash Messaging**
  Instant success/error messages for every action.

* **Timezone Aware**
  Accurate tracking with **Asia/Kolkata** timezone.

* **Responsive UI**
  Built with **Tailwind CSS**, optimized for mobile and desktop.

---

## 🌟 Highlights

* Professional **Flask Blueprint architecture**
* Real-time time parsing for class tracking
* Advanced **CRUD operations** for timetable management
* Export support (CSV now, PDF coming soon)
* Clean, mobile-friendly UI with modern UX

---

## 🛠 Technologies Used

* **Backend:** Python (Flask, Blueprints, Jinja2)
* **Frontend:** HTML, Tailwind CSS, Jinja2
* **Data Storage:** JSON timetable
* **Export:** CSV (PDF planned)
* **Deployment:** Vercel

---

## 📂 Project Structure

```
Timly3/
├── app/
│   ├── templates/        # HTML templates
│   │   ├── add_course.html
│   │   ├── base.html
│   │   ├── full.html
│   │   └── today.html
│   ├── __init__.py       # App factory
│   ├── models.py         # Data models
│   ├── routes.py         # Routes (Blueprints)
│
├── data/                 # Timetable JSON
├── instance/             # Flask instance folder
├── migrations/           # Database migrations (future-ready)
├── static/images/        # Static assets (images, CSS, JS)
├── venv/                 # Virtual environment
├── main.py               # App entry point
├── requirements.txt      # Dependencies
├── vercel.json           # Deployment config
├── .env                  # Environment variables
```

---

## 📖 Usage

1. **Homepage** → Shows today’s classes with live status
2. **Full View** → Browse the complete weekly timetable
3. **Add Course** → Fill in details (code, name, time, room, instructor, type, notes)
4. **Delete Course** → Remove unwanted entries
5. **Export CSV** → Download timetable for external use

---

## 🔮 Future Enhancements

* ✅ **PDF Export** (placeholder now)
* 🔔 Notifications for upcoming classes
* 🔑 Student login for personal schedules
* 📅 Calendar sync (Google/Outlook)
* 🎨 Multiple UI themes & dark mode

---

## 🌐 Live Access

👉 Try it here: [Timly 3](https://timly3.vercel.app/)

---

⚡ **Timly 3 = Professional structure + Advanced features + Modern UI.**

---
