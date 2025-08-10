from . import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(12), nullable=False)
    courseCode = db.Column(db.String(16), nullable=False)
    courseName = db.Column(db.String(128), nullable=False)
    instructor = db.Column(db.String(64))
    time = db.Column(db.String(32), nullable=False)
    room = db.Column(db.String(128), nullable=False)  # Comma-separated string
    type = db.Column(db.String(16), nullable=False)
    notes = db.Column(db.String(256))

    def to_dict(self):
        return {
            "id": self.id,
            "day": self.day,
            "courseCode": self.courseCode,
            "courseName": self.courseName,
            "instructor": self.instructor or "TBA",
            "time": self.time,
            "room": self.room,
            "type": self.type,
            "notes": self.notes or "",
        }
