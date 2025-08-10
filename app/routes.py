from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, Response
from datetime import datetime
import csv
import io

main_bp = Blueprint('main', __name__)

def parse_time_range(time_range):
    """Convert 'h:mm AM/PM-h:mm AM/PM' to (start_datetime, end_datetime) today."""
    try:
        start_str, end_str = [t.strip() for t in time_range.split('-')]
        today = datetime.now().date()
        start_dt = datetime.strptime(start_str, "%I:%M %p").replace(year=today.year, month=today.month, day=today.day)
        end_dt = datetime.strptime(end_str, "%I:%M %p").replace(year=today.year, month=today.month, day=today.day)
        return start_dt, end_dt
    except Exception:
        return None, None

@main_bp.route("/")
def home():
    data = current_app.load_timetable()
    today = datetime.now().strftime("%A")
    now = datetime.now()
    today_classes = data.get("timetable", {}).get(today, [])

    for cls in today_classes:
        cls.setdefault("instructor", "TBA")
        cls.setdefault("notes", "")
        try:
            if "-" in cls.get("time", ""):
                start_dt, end_dt = parse_time_range(cls["time"])
                if start_dt and end_dt:
                    if start_dt <= now <= end_dt:
                        cls["status"] = "Ongoing"
                    elif now < start_dt:
                        cls["status"] = "Upcoming"
                    else:
                        cls["status"] = "Completed"
                else:
                    cls["status"] = "Unknown"
            else:
                cls["status"] = "Unknown"
        except Exception:
            cls["status"] = "Unknown"

    return render_template(
        "today.html",
        day=today,
        classes=today_classes,
        ongoing=[c for c in today_classes if c.get("status") == "Ongoing"],
        upcoming=[c for c in today_classes if c.get("status") == "Upcoming"],
        completed=[c for c in today_classes if c.get("status") == "Completed"],
        current_year=now.year
    )

@main_bp.route("/view")
def view_timetable():
    data = current_app.load_timetable()
    timetable = data.get("timetable", {})
    current_day = datetime.now().strftime("%A")
    now = datetime.now()

    for class_list in timetable.values():
        for cls in class_list:
            cls.setdefault("instructor", "TBA")
            cls.setdefault("notes", "")
            if "time" in cls and "-" in cls["time"]:
                start_dt, end_dt = parse_time_range(cls["time"])
                if start_dt and end_dt:
                    if start_dt <= now <= end_dt:
                        cls["status"] = "Ongoing"
                    elif now < start_dt:
                        cls["status"] = "Upcoming"
                    else:
                        cls["status"] = "Completed"
                else:
                    cls["status"] = "Unknown"

    return render_template(
        "full.html",
        timetable=timetable,
        current_day=current_day,
        current_year=now.year
    )
@main_bp.route("/add_course", methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        data = current_app.load_timetable()
        day = request.form.get("day")
        course = {
            "courseCode": request.form.get('courseCode'),
            "courseName": request.form.get('courseName'),
            "instructor": request.form.get('instructor') or "TBA",
            "time": request.form.get('time'),
            "room": parse_room(request.form.get('room')),
            "type": request.form.get('type'),
            "notes": request.form.get('notes') or ""
        }
        data.setdefault("timetable", {}).setdefault(day, []).append(course)
        current_app.save_timetable(data)
        flash("Course added successfully", "success")
        return redirect(url_for('main.view_timetable'))
    return render_template('add_course.html')

def parse_room(room_input):
    # Support splitting rooms on comma for multi-room input in advanced add UI
    if room_input and "," in room_input:
        return [r.strip() for r in room_input.split(",") if r.strip()]
    return room_input.strip() if room_input else "N/A"

@main_bp.route("/delete_course/<day>/<int:index>")
def delete_course(day, index):
    data = current_app.load_timetable()
    if day in data["timetable"] and 0 <= index < len(data["timetable"][day]):
        data["timetable"][day].pop(index)
        current_app.save_timetable(data)
        flash("Course deleted", "success")
    else:
        flash("Could not delete course. Invalid index or day.", "error")
    return redirect(url_for("main.view_timetable"))

# ADVANCED: Export as CSV
@main_bp.route("/export_csv")
def export_csv():
    data = current_app.load_timetable()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Day", "Time", "Course Code", "Course Name", "Instructor", "Room(s)", "Type", "Notes"])

    for day, class_list in data.get("timetable", {}).items():
        for cls in class_list:
            room = cls["room"]
            if isinstance(room, list):
                room = ", ".join(room)
            writer.writerow([
                day,
                cls.get("time", ""),
                cls.get("courseCode", ""),
                cls.get("courseName", ""),
                cls.get("instructor", "TBA"),
                room,
                cls.get("type", ""),
                cls.get("notes", "")
            ])
    return Response(output.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=timetable.csv"})

# ADVANCED: Export as PDF Stub (implement with your chosen PDF library)
@main_bp.route("/export_pdf")
def export_pdf():
    flash("PDF export not implemented in this sample.", "error")
    return redirect(url_for('main.home'))
