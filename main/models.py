from main.__main__ import db
from datetime import datetime


class Person(db.Model):
    person_id  = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(69), nullable = False)
    last_name  = db.Column(db.String(69), nullable = False)
    gender     = db.Column(db.String(1))
    birth_date = db.Column(db.DateTime)
    phone_number = db.Column(db.Integer)
    email        = db.Column(db.String(69))
    date_added = db.Column(db.DateTime, default = datetime.utcnow,
            nullable = False)
    
    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}')"


class Section(db.Model):
    section_id   = db.Column(db.Integer,    primary_key = True)
    section_name = db.Column(db.String(69), nullable = False, unique = True)
    mayor_id     = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    vice_mayor_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    students = db.relationship('Student', backref = 'section', lazy = True)

    def __repr__(self):
        return f"Section('{self.section_name}'')"


class Student(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('person.person_id'),
            nullable = False, unique = True)
    section_id = db.Column(db.Integer. db.ForeignKey('section.section_id'),
            nullable = False)

    def __repr__(self):
        return f"Student('{self.student_id}', '{self.section_id}')"

