from main.app import db
from datetime import datetime


clas Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    first_name   = db.Column(db.String(69), nullable = False)
    last_name    = db.Column(db.String(69), nullable = False)
    gender       = db.Column(db.String(1))
    birth_date   = db.Column(db.DateTime)
    phone_number = db.Column(db.Integer)
    email        = db.Column(db.String(69))
    date_added   = db.Column(db.DateTime, default = datetime.utcnow)
    
    db.relationship('Student')
    
    def __repr__(self):
        return f"Person({self.id=}, {self.first_name=}, {self.last_name=})"


class Section(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    section_name  = db.Column(db.String(69), nullable = False, unique = True)
    mayor_id      = db.Column(db.Integer, db.ForeignKey('student.id'))
    vice_mayor_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    secretary_id  = db.Column(db.Integer, db.ForeignKey('student.id'))
    treasurer_id  = db.Column(db.Integer, db.ForeignKey('student.id'))
    auditor_id    = db.Column(db.Integer, db.ForeignKey('student.id'))
    pro_id        = db.Column(db.Integer, db.ForeignKey('student.id'))
    
    students = db.relationship('Student')


    def __repr__(self):
        return f"Section({self.id=}, {self.section_name=})"


class Student(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('person.id'),
            nullable = False, primary_key = True)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'),
            nullable = False)
    
    db.relationship('Section')

    def __repr__(self):
        return f"Student({self.id=})"

