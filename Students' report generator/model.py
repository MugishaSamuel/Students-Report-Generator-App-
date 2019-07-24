from sqlalchemy import Column, Integer, String, Float, ForeignKey,create_engine
from sqlalchemy.orm import backref, relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Teachers(Base):
    __tablename__="teachers"
    employee_no = Column(String(10), primary_key=True)
    name = Column(String(60))
    sex = Column(String(10))
    address = Column(String(100))
    contact = Column(String(15))
    role = Column(String(20))

    def __init__(self,employee_no, name, address, contact, role):
        self.employee_no = employee_no
        self.name = name
        self.address = address
        self.contact = contact
        self.role = role

class Students(Base):
    __tablename__ = "students"

    studentId = Column(Integer, primary_key=True)
    studentName = Column(String(50))
    nationality = Column(String(50))
    dateOfBirth = Column(String(50))
    age = Column(Integer)
    sex = Column(String(10))
    student_class = Column(String(20))
    father_names = Column(String(60))
    mother_names = Column(String(60))
    parent_contact = Column(String(15))
    non = Column(String(60))
    non_contact = Column(String(60))

    contact = Column(String)

    child1 = relationship('Baby', uselist=False, backref='students')
    child2 = relationship('Middle', uselist=False, backref='students')
    child3 = relationship('Top', uselist=False, backref='students')
    child4 = relationship('PrimaryOneMarksBeginningOfTerm', uselist=False, backref='students')
    child5 = relationship('PrimaryOneMarksMidTerm', uselist=False, backref='students')
    child6 = relationship('PrimaryOneMarksEndOfTerm', uselist=False, backref='students')
    child7 = relationship('PrimaryTwoMarksBeginningOfTerm', uselist=False, backref='students')
    child8 = relationship('PrimaryTwoMarksMidTerm', uselist=False, backref='students')
    child9 = relationship('PrimaryTwoMarksEndOfTerm', uselist=False, backref='students')
    child10 = relationship('PrimaryThreeMarksBeginningOfTerm', uselist=False, backref='students')
    child11 = relationship('PrimaryThreeMarksMidTerm', uselist=False, backref='students')
    child12 = relationship('PrimaryThreeMarksEndOfTerm', uselist=False, backref='students')
    child13 = relationship('PrimaryFourMarksBeginningOfTerm', uselist=False, backref='students')
    child14 = relationship('PrimaryFourMarksMidTerm', uselist=False, backref='students')
    child15 = relationship('PrimaryFourMarksEndOfTerm', uselist=False, backref='students')
    child16 = relationship('PrimaryFiveMarksBeginningOfTerm', uselist=False, backref='students')
    child17 = relationship('PrimaryFiveMarksMidTerm', uselist=False, backref='students')
    child18 = relationship('PrimaryFiveMarksEndOfTerm', uselist=False, backref='students')
    child19 = relationship('PrimarySixMarksBeginningOfTerm', uselist=False, backref='students')
    child20 = relationship('PrimarySixMarksMidTerm', uselist=False, backref='students')
    child21= relationship('PrimarySixMarksEndOfTerm', uselist=False, backref='students')
    child22 = relationship('PrimarySevenMarksBeginningOfTerm', uselist=False, backref='students')
    child23 = relationship('PrimarySevenMarksMidTerm', uselist=False, backref='students')
    child24 = relationship('PrimarySevenMarksEndOfTerm', uselist=False, backref='students')
   

    def __init__(self,studentName,nationality,dateOfBirth,age,sex,student_class,father_names,mother_names,parent_contact,non,non_contact):
        self.studentName = studentName
        self.nationality = nationality
        self.dateOfBirth = dateOfBirth
        self.age = age
        self.sex = sex
        self.student_class = student_class
        self.father_names = father_names
        self.mother_names = mother_names
        self.parent_contact = parent_contact
        self.non = non
        self.non_contact = non_contact

class Baby(Base):
    __tablename__ = "baby"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    reading = Column(Integer)
    writing = Column(Integer)
    physical_education = Column(Integer)

    def __init__(self, studentId, reading, writing, physical_education):
        self.studentId = studentId
        self.reading = reading
        self.writing =writing
        self.physical_education = physical_education

class Middle(Base):
    __tablename__ = "middle"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    reading = Column(Integer)
    writing = Column(Integer)
    physical_education = Column(Integer)

    def __init__(self, studentId, reading, writing, physical_education):
        self.studentId = studentId
        self.reading = reading
        self.writing =writing
        self.physical_education = physical_education

class Top(Base):
    __tablename__ = "top"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    reading = Column(Integer)
    writing = Column(Integer)
    physical_education = Column(Integer)

    def __init__(self, studentId, reading, writing, physical_education):
        self.studentId = studentId
        self.reading = reading
        self.writing = writing
        self.physical_education = physical_education

class PrimaryOneMarksBeginningOfTerm(Base):
    __tablename__ = "primary_one_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryOneMarksMidTerm(Base):
    __tablename__ = "primary_one_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryOneMarksEndOfTerm(Base):
    __tablename__ = "primary_one_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryTwoMarksBeginningOfTerm(Base):
    __tablename__ = "primary_two_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryTwoMarksMidTerm(Base):
    __tablename__ = "primary_two_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average


class PrimaryTwoMarksEndOfTerm(Base):
    __tablename__ = "primary_two_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self, studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryThreeMarksBeginningOfTerm(Base):
    __tablename__ = "primary_three_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryThreeMarksMidTerm(Base):
    __tablename__ = "primary_three_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryThreeMarksEndOfTerm(Base):
    __tablename__ = "primary_three_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFourMarksBeginningOfTerm(Base):
    __tablename__ = "primary_four_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFourMarksMidTerm(Base):
    __tablename__ = "primary_four_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFourMarksEndOfTerm(Base):
    __tablename__ = "primary_four_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFiveMarksBeginningOfTerm(Base):
    __tablename__ = "primary_five_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFiveMarksMidTerm(Base):
    __tablename__ = "primary_five_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimaryFiveMarksEndOfTerm(Base):
    __tablename__ = "primary_five_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySixMarksBeginningOfTerm(Base):
    __tablename__ = "primary_six_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySixMarksMidTerm(Base):
    __tablename__ = "primary_six_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySixMarksEndOfTerm(Base):
    __tablename__ = "primary_six_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySevenMarksBeginningOfTerm(Base):
    __tablename__ = "primary_seven_marks_beginning_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySevenMarksMidTerm(Base):
    __tablename__ = "primary_seven_marks_mid_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

class PrimarySevenMarksEndOfTerm(Base):
    __tablename__ = "primary_seven_marks_end_of_term"
    Id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('students.studentId'))
    student_names = Column(String(60))
    class_teacher = Column(String(60))
    term = Column(String(10))
    stream = Column(String(40))
    mathematics = Column(Integer)
    english = Column(Integer)
    science = Column(Integer)
    social_studies = Column(Integer)
    total = Column(Integer)
    average = Column(Integer)

    def __init__(self,studentId,student_names,class_teacher,term,stream,mathematics,english,science,social_studies,total,average):
        self.studentId = studentId
        self.student_names = student_names
        self.class_teacher = class_teacher
        self.term = term
        self.stream = stream
        self.mathematics = mathematics
        self.english = english
        self.science = science
        self.social_studies = social_studies
        self.total = total
        self.average = average

Base.metadata.create_all(engine)