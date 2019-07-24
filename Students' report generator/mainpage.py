from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import model as db
from model import (PrimaryOneMarksBeginningOfTerm,PrimaryOneMarksMidTerm,PrimaryOneMarksEndOfTerm,PrimaryTwoMarksBeginningOfTerm,
                   PrimaryTwoMarksMidTerm,PrimaryTwoMarksEndOfTerm,PrimaryThreeMarksBeginningOfTerm,
                   PrimaryThreeMarksMidTerm,PrimaryThreeMarksEndOfTerm,PrimaryFourMarksBeginningOfTerm,PrimaryFourMarksMidTerm,PrimaryFourMarksEndOfTerm,
                   PrimaryFiveMarksBeginningOfTerm,PrimaryFiveMarksMidTerm,PrimaryFiveMarksEndOfTerm,
                   PrimarySixMarksBeginningOfTerm,PrimarySixMarksMidTerm,PrimarySixMarksEndOfTerm,
                   PrimarySevenMarksBeginningOfTerm,PrimarySevenMarksMidTerm,PrimarySevenMarksEndOfTerm)
filename = "logo.png"

class Message(QMessageBox):
    def __init__(self,title="",message=""):
        self.title = title
        self.message = message
        QMessageBox.__init__(self)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.exec_()

class MainPage(QWidget):
    """THE APPLICATIONS MAINPAGE"""
    def __init__(self):
        QWidget.__init__(self)
        l1 = QHBoxLayout(self)
        layout = QVBoxLayout(self)
        empty_label1 = QLabel(self)
        empty_label2 = QLabel(self)
        self.sch_label = QLabel("THE NAME OF THE SCHOOL",self)
        self.image = QLabel(self)
        image = QPixmap(filename)
        self.image.setPixmap(image)
        self.image.resize(image.width(),image.height())
        self.image.setFrameShape(QFrame.Panel)
        self.image.setStyleSheet("color:blue;font:20px;width:20px;border: 1px solid blue;border-radius:50%;")
        self.sch_label.setStyleSheet("color:blue;font:20px;width:20px;border: 1px solid blue;border-radius:10px;")
        self.sch_label.setFrameShape(QFrame.Panel)
        #self.sch_label.setFrameShadow(QFrame.Sunken)
        self.sch_label.setAlignment(Qt.AlignCenter)
        #self.sch_label.setLineWidth(1)
        self.sch_label.resize(400,50)
        self.bio_data = QPushButton("STUDENT BIO DATA",self)
        self.bio_data.setStyleSheet("height:40px;width:200px;color:black;border: 1px solid blue;border-radius:2px;")
        self.marks = QPushButton("STUDENT MARKS",self)
        self.marks.setStyleSheet("height:40px;width:200px;color:black;border: 1px solid blue;border-radius:2px;")
        self.performance = QPushButton("PERFORMANCE SHEET",self)
        self.performance.setStyleSheet("height:40px;width:200px;color:black;border: 1px solid blue;border-radius:2px;")
        self.teacher = QPushButton("REGISTER CLASS TEACHER", self)
        self.teacher.setStyleSheet("height:40px;width:200px;color:black;border: 1px solid blue;border-radius:2px;")
        layout.addStretch()
        layout.addWidget(self.sch_label)
        layout.addWidget(empty_label1)
        layout.addWidget(self.image)
        layout.addWidget(empty_label2)
        layout.addWidget(self.bio_data)
        layout.addWidget(self.marks)
        layout.addWidget(self.performance)
        layout.addWidget(self.teacher)
        layout.addStretch()
        l1.addStretch()
        l1.addLayout(layout)
        l1.addStretch()
        self.setLayout(l1)
        self.resize(1000,600)
        self.setWindowTitle("STUDENT APPLICATION")
        self.bio_data.clicked.connect(self.startUIStudentBioData)
        self.marks.clicked.connect(self.startUIStudentMarks)
        self.performance.clicked.connect(self.startUIPerformanceSheet)
        self.teacher.clicked.connect(self.startUITeacher)

    def startUIStudentBioData(self):
        self.bio_data_page = StudentBioData()
        self.close()
        self.bio_data_page.show()

    def startUIStudentMarks(self):
        self.marks_page = StudentMarks()
        self.close()
        self.marks_page.show()

    def startUIPerformanceSheet(self):
        self.performance_page = Mainmenu()
        self.close()
        self.performance_page.show()

    def startUITeacher(self):
        self.teacher_page = Teacher()
        self.close()
        self.teacher_page.show()

        
class StudentBioData(QWidget):
    """STUDENT BIO DATA MAINPAGE"""
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1000,600)
        self.setWindowTitle("STUDENT APPLICATION - BIO DATA")
        mainlayout = QHBoxLayout(self)
        vbox = QVBoxLayout(self)
        label = QLabel("REGISTER STUDENT",self)
        label.setAlignment(Qt.AlignCenter)
        label.setFrameShape(QFrame.Panel)
        self.student_names = QLineEdit()
        self.nationality = QLineEdit()
        self.dateofbirth = QDateEdit()
        self.dateofbirth.setDisplayFormat("dd/MM/yyyy")
        self.age = QSpinBox()
        self.studentSexCombobox = QComboBox()
        self.studentSexCombobox.addItems(['MALE', 'FEMALE'])
        self.studentClassCombobox = QComboBox()
        self.studentClassCombobox.addItems(['BABY', 'MIDDLE', 'TOP', 'PRIMARY ONE', 'PRIMARY TWO', 'PRIMARY THREE', 'PRIMARY FOUR', 'PRIMARY FIVE','PRIMARY SIX', 'PRIMARY SEVEN'])
        self.father_names = QLineEdit()
        self.mother_names = QLineEdit()
        self.parent_contact = QLineEdit()
        self.non = QLineEdit()
        self.non_contact = QLineEdit()
        layout = QFormLayout(self)
        # layout.addRow("STUDENT ID",QLineEdit())
        layout.addRow("STUDENT NAMES",self.student_names)
        layout.addRow("NATIONALITY", self.nationality)
        layout.addRow("DATE OF BIRTH",self.dateofbirth)
        layout.addRow("AGE",self.age)
        layout.addRow("SEX",self.studentSexCombobox)
        layout.addRow("CLASS",self.studentClassCombobox)
        layout.addRow("FATHER'S NAMES",self.father_names)
        layout.addRow("MOTHER'S NAMES",self.mother_names)
        layout.addRow("PARENT'S CONTACT",self.parent_contact)
        layout.addRow("NEXT OF KIN (N.O.N)",self.non)
        layout.addRow("N.O.N CONTACT",self.non_contact)
        hbox = QHBoxLayout()
        back2main = QPushButton("BACK TO HOME")
        save = QPushButton("SAVE DETAILS")
        hbox.addWidget(back2main)
        hbox.addWidget(save)
        vbox.addStretch()
        vbox.addWidget(label)
        vbox.addLayout(layout)
        vbox.addLayout(hbox)
        vbox.addStretch()
        mainlayout.addStretch()
        mainlayout.addLayout(vbox)
        mainlayout.addStretch()
        self.setLayout(mainlayout)

        back2main.clicked.connect(self.back2mainpage)
        save.clicked.connect(self.savestudentbiodata)

    def back2mainpage(self):
        self.mainpage = MainPage()
        self.close()
        self.mainpage.show()

    def savestudentbiodata(self):
        try:
            student_names = self.student_names.text()
            nationality = self.nationality.text()
            dateofbirth = self.dateofbirth.date().toString(Qt.DefaultLocaleShortDate)
            age = self.age.value()
            sex = self.studentSexCombobox.currentText()
            student_class = self.studentClassCombobox.currentText()
            father_names = self.father_names.text()
            mother_names = self.mother_names.text()
            parent_contact = self.parent_contact.text()
            non = self.non.text()
            non_contact = self.non_contact.text()

            if (student_names.strip(" ") and nationality.strip(" ") and dateofbirth.strip(" ") and father_names.strip(" ") and mother_names.strip(" ")
            and parent_contact.strip(" ") and non.strip(" ") and non_contact.strip(" ")):
                sessionHandler = db.Session()
                student = db.Students(studentName=student_names,nationality=nationality,dateOfBirth=dateofbirth,age=age,sex=sex,student_class=student_class,father_names=father_names,
                mother_names=mother_names,parent_contact=parent_contact,non=non,non_contact=non_contact)
                sessionHandler.add(student)
                sessionHandler.commit()
                sessionHandler.close()
                self.student_names.setText("")
                self.nationality.setText("")
                self.age.setValue(0)
                self.father_names.setText("")
                self.mother_names.setText("")
                self.parent_contact.setText("")
                self.non.setText("")
                self.non_contact.setText("")
                Message("Success","Student added successfully")

            else:
                Message("Unsuccessful","Cannot Save without filling out all the input fields of the form")

        except Exception as error:
            Message("Error","Error has occured: {}".format(error))

##############################class marks########################################################

class StudentMarks(QTabWidget):
    """CLASS FOR ENTERING STUDENT MARKS"""
    def __init__(self, parent=None):
        super(StudentMarks,self).__init__(parent)
        self.resize(1000,600)
        self.setWindowTitle("STUDENT APPLICATION - CLASS MARKS")
        self.addTab(P1Tab(self),"PRIMARY ONE")
        self.addTab(P2Tab(self),"PRIMARY TWO")
        self.addTab(P3Tab(self),"PRIMARY THREE")
        self.addTab(P4Tab(self),"PRIMARY FOUR")
        self.addTab(P5Tab(self),"PRIMARY FIVE")
        self.addTab(P6Tab(self),"PRIMARY SIX")
        self.addTab(P7Tab(self),"PRIMARY SEVEN")

class MarksForm(QWidget):
    def __init__(self,name,par):
        self.name = name
        self.par = par
        QWidget.__init__(self)
        self.mainLayout = QVBoxLayout(self)
        self.student_names = QLineEdit(self)
        self.math = QLineEdit()
        self.english = QLineEdit()
        self.science = QLineEdit()
        self.sst = QLineEdit()
        self.total = QLineEdit()
        self.average = QLineEdit()
        self.vbox = QVBoxLayout(self)
        self.layout = QFormLayout(self)
        self.examGroup = QGroupBox(self.name)
        self.id = QLineEdit()
        self.layout.addRow("INDEX NUMBER",self.id)
        self.layout.addRow("STUDENT NAMES", self.student_names)
        self.class_teachers = QComboBox()
        self.list_of_teachers = ["TEACHER 1", "TEACHER 2", "TEACHER 3", "TEACHER 4", "TEACHER 5", "TEACHER 6"]  # retrive data from class teacher table.
        self.class_teachers.addItems(self.list_of_teachers)
        self.layout.addRow("SELECT TEACHER", self.class_teachers)
        self.term = QComboBox()
        self.terms = ["TERM 1","TERM 2","TERM 3"]
        self.term.addItems(self.terms)
        self.streams = QComboBox()
        self.layout.addRow("SELECT TERM",self.term)
        self.list_of_streams = ["STREAM A", "STREAM B", "STREAM C", "STREAM D"]
        self.streams.addItems(self.list_of_streams)
        self.layout.addRow("SELECT STREAM", self.streams)
        self.exams = QComboBox()
        self.exams_list = ["BEGINNING OF TERM(BOT)","MID TERM EXAMS(MTD)","END OF TERM(EOT)"]
        self.exams.addItems(self.exams_list)
        self.layout.addRow("SELECT EXAM",self.exams)
        self.layout.addRow("MATH", self.math)
        self.layout.addRow("ENGLISH",  self.english)
        self.layout.addRow("SCIENCE",  self.science)
        self.layout.addRow("SOCIAL STUDIES(SST)", self.sst)
        self.layout.addRow("TOTAL", self.total)
        self.layout.addRow("AVERAGE", self.average)
        self.hbox = QHBoxLayout()
        self.back2main = QPushButton("BACK TO HOME")
        self.save_marks = QPushButton("SAVE MARKS")
        self.hbox.addWidget(self.back2main)
        self.hbox.addWidget(self.save_marks)
        self.vbox.addLayout(self.layout)
        self.label = QLabel("")
        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch()
        self.examGroup.setLayout(self.vbox)
        self.mainLayout.addWidget(self.examGroup)
        self.mainLayout.addStretch()
        self.back2main.clicked.connect(self.back2mainpage)
        self.save_marks.clicked.connect(self.savemarks)
        self.setLayout(self.mainLayout)

    def returnPressed(self):
        print("yesss!!")

    def back2mainpage(self):
        self.mainpage = MainPage()
        self.par.close()
        self.mainpage.show()
    def inputresults(self):
        student_id = self.id.text()
        student_names = self.student_names.text()
        class_teacher = self.class_teachers.currentText()
        term = self.term.currentText()
        stream = self.streams.currentText()
        math = self.math.text()
        eng = self.english.text()
        science = self.science.text()
        sst = self.sst.text()
        total = self.total.text()
        average = self.average.text()
        results = [student_id,student_names,class_teacher,term,stream,math,eng,science,sst,total,average]
        return results

    def clear(self):
        self.id.setText("")
        self.student_names.setText("")
        self.math.setText("")
        self.english.setText("")
        self.science.setText("")
        self.sst.setText("")
        self.total.setText("")
        self.average.setText("")

    def savemarks(self):
        if self.name == "PRIMARY ONE MARKS":
            p1_dic = {PrimaryOneMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimaryOneMarksMidTerm:"MID TERM EXAMS(MTD)",PrimaryOneMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p1_dic[PrimaryOneMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(" ") and student[7].strip(" ") and student[8].strip(" ")
                        and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryOneMarksBeginningOfTerm(studentId=student[0],student_names=student[1],class_teacher=student[2],term=student[3],
                                stream=student[4],mathematics=int(student[5]), english=int(student[6]),science=int(student[7]),social_studies=int(student[8]),
                                total=int(student[9]),average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Successful","Student added successfully!")

                    else:
                        Message("Error","Please fill in all the neccessary details")

                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p1_dic[PrimaryOneMarksMidTerm]:
                try:
                     student = self.inputresults()

                     if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(" ") and student[7].strip(" ") and student[8].strip(" ")
                        and student[9].strip(" ") and student[10].strip(" ")):
                         sessionHandler = db.Session()
                         student = PrimaryOneMarksMidTerm(studentId=student[0], student_names=student[1],
                                class_teacher=student[2],term=student[3],stream=student[4], mathematics=int(student[5]),
                                english=int(student[6]), science=int(student[7]),social_studies=int(student[8]),
                                total=int(student[9]), average=float(student[10]))
                         sessionHandler.add(student)
                         sessionHandler.commit()
                         sessionHandler.close()
                         self.clear()
                         Message("Success","Student added successfully!")

                     else:
                         Message("Error","Please fill in all the necessary details!")

                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p1_dic[PrimaryOneMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(" ") and student[7].strip(" ") and student[8].strip(" ")
                        and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryOneMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                 class_teacher=student[2],term=student[3],stream=student[4],mathematics=int(student[5]),
                                english=int(student[6]), science=int(student[7]),social_studies=int(student[8]),
                                total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")

                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))
        elif self.name == "PRIMARY TWO MARKS":
            p2_dic = {PrimaryTwoMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimaryTwoMarksMidTerm:"MID TERM EXAMS(MTD)",PrimaryTwoMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p2_dic[PrimaryTwoMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryTwoMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                                 class_teacher=student[2], term=student[3],
                                                                 stream=student[4],
                                                                 mathematics=int(student[5]), english=int(student[6]),
                                                                 science=int(student[7]),
                                                                 social_studies=int(student[8]),
                                                                 total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p2_dic[PrimaryTwoMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryTwoMarksMidTerm(studentId=student[0], student_names=student[1],
                                                                 class_teacher=student[2], term=student[3],
                                                                 stream=student[4],
                                                                 mathematics=int(student[5]), english=int(student[6]),
                                                                 science=int(student[7]),
                                                                 social_studies=int(student[8]),
                                                                 total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))
            elif examination == p2_dic[PrimaryTwoMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryTwoMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

        elif self.name == "PRIMARY THREE MARKS":
            p3_dic = {PrimaryThreeMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimaryThreeMarksMidTerm:"MID TERM EXAMS(MTD)",PrimaryThreeMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p3_dic[PrimaryThreeMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryThreeMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                           class_teacher=student[2], term=student[3],
                                                           stream=student[4],
                                                           mathematics=int(student[5]), english=int(student[6]),
                                                           science=int(student[7]),
                                                           social_studies=int(student[8]),
                                                           total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")

                    else:
                        Message("Error", "Please fill in all the necessary details!")

                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))
            elif examination == p3_dic[PrimaryThreeMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryThreeMarksMidTerm(studentId=student[0], student_names=student[1],
                                                                   class_teacher=student[2], term=student[3],
                                                                   stream=student[4],
                                                                   mathematics=int(student[5]), english=int(student[6]),
                                                                   science=int(student[7]),
                                                                   social_studies=int(student[8]),
                                                                   total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p3_dic[PrimaryThreeMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryThreeMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                           class_teacher=student[2], term=student[3],
                                                           stream=student[4],
                                                           mathematics=int(student[5]), english=int(student[6]),
                                                           science=int(student[7]),
                                                           social_studies=int(student[8]),
                                                           total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error", "Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

        elif self.name == "PRIMARY FOUR MARKS":
            p4_dic = {PrimaryFourMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimaryFourMarksMidTerm:"MID TERM EXAMS(MTD)",PrimaryFourMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p4_dic[PrimaryFourMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFourMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                           class_teacher=student[2], term=student[3],
                                                           stream=student[4],
                                                           mathematics=int(student[5]), english=int(student[6]),
                                                           science=int(student[7]),
                                                           social_studies=int(student[8]),
                                                           total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error", "Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p4_dic[PrimaryFourMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFourMarksMidTerm(studentId=student[0], student_names=student[1],
                                                           class_teacher=student[2], term=student[3],
                                                           stream=student[4],
                                                           mathematics=int(student[5]), english=int(student[6]),
                                                           science=int(student[7]),
                                                           social_studies=int(student[8]),
                                                           total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error", "Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p4_dic[PrimaryFourMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFourMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                           class_teacher=student[2], term=student[3],
                                                           stream=student[4],
                                                           mathematics=int(student[5]), english=int(student[6]),
                                                           science=int(student[7]),
                                                           social_studies=int(student[8]),
                                                           total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error", "Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

        elif self.name == "PRIMARY FIVE MARKS":
            p5_dic = {PrimaryFiveMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimaryFiveMarksMidTerm:"MID TERM EXAMS(MTD)",PrimaryFiveMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p5_dic[PrimaryFiveMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFiveMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p5_dic[PrimaryFiveMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFiveMarksMidTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p5_dic[PrimaryFiveMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimaryFiveMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                          class_teacher=student[2], term=student[3],
                                                          stream=student[4],
                                                          mathematics=int(student[5]), english=int(student[6]),
                                                          science=int(student[7]),
                                                          social_studies=int(student[8]),
                                                          total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success", "Student added successfully!")
                    else:
                        Message("Error", "Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error", "Error has occured: {}".format(error))

        elif self.name == "PRIMARY SIX MARKS":
            p6_dic = {PrimarySixMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimarySixMarksMidTerm:"MID TERM EXAMS(MTD)",PrimarySixMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p6_dic[PrimarySixMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySixMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p6_dic[PrimarySixMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySixMarksMidTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p6_dic[PrimarySixMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySixMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

        elif self.name == "PRIMARY SEVEN MARKS":
            p7_dic = {PrimarySevenMarksBeginningOfTerm:"BEGINNING OF TERM(BOT)",PrimarySevenMarksMidTerm:"MID TERM EXAMS(MTD)",PrimarySevenMarksEndOfTerm:"END OF TERM(EOT)"}
            examination = self.exams.currentText()
            if examination == p7_dic[PrimarySevenMarksBeginningOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySevenMarksBeginningOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p7_dic[PrimarySevenMarksMidTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySevenMarksMidTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

            elif examination == p7_dic[PrimarySevenMarksEndOfTerm]:
                try:
                    student = self.inputresults()

                    if (student[0].strip(" ") and student[1].strip(" ") and student[5].strip(" ") and student[6].strip(
                            " ") and student[7].strip(" ") and student[8].strip(" ")
                            and student[9].strip(" ") and student[10].strip(" ")):
                        sessionHandler = db.Session()
                        student = PrimarySevenMarksEndOfTerm(studentId=student[0], student_names=student[1],
                                                         class_teacher=student[2], term=student[3],
                                                         stream=student[4],
                                                         mathematics=int(student[5]), english=int(student[6]),
                                                         science=int(student[7]),
                                                         social_studies=int(student[8]),
                                                         total=int(student[9]), average=float(student[10]))
                        sessionHandler.add(student)
                        sessionHandler.commit()
                        sessionHandler.close()
                        self.clear()
                        Message("Success","Student added successfully!")
                    else:
                        Message("Error","Please fill in all the necessary details!")
                except Exception as error:
                    Message("Error","Error has occured: {}".format(error))

class P1Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY ONE MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P2Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY TWO MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P3Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY THREE MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P4Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY FOUR MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P5Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY FIVE MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P6Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY SIX MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

class P7Tab(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.marks = MarksForm("PRIMARY SEVEN MARKS",parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addStretch()
        self.hbox.addWidget(self.marks)
        self.hbox.addStretch()
        self.setLayout(self.hbox)

############################################################################################################

class Mainmenu(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 600)
        self.setWindowTitle("STUDENT APPLICATION - PERFORMANCE SHEET")
        # creating PerformanceUI and setting it as central
        self.performance_sheet = PerformanceSheet(parent=self)
        self.setCentralWidget(self.performance_sheet)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        p1 = bar.addMenu("Primary One")
        p1.addAction("BOT")
        p1.addAction("MID")
        p1.addAction("EOT")
        p2 = bar.addMenu("Primary Two")
        p2.addAction("BOT")
        p2.addAction("MID")
        p2.addAction("EOT")
        p3 = bar.addMenu("Primary Three")
        p3.addAction("BOT")
        p3.addAction("MID")
        p3.addAction("EOT")
        p4 = bar.addMenu("Primary Four")
        p4.addAction("BOT")
        p4.addAction("MID")
        p4.addAction("EOT")
        p5 = bar.addMenu("Primary Five")
        p5.addAction("BOT")
        p5.addAction("MID")
        p5.addAction("EOT")
        p6 = bar.addMenu("Primary Six")
        p6.addAction("BOT")
        p6.addAction("MID")
        p6.addAction("EOT")
        p7 = bar.addMenu("Primary Seven")
        p7.addAction("BOT")
        p7.addAction("MID")
        p7.addAction("EOT")

class PerformanceSheet(QWidget):
    """A TEACHER CAN DELETE, UPDATE, AND PRINT REPORT CARDS """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000,600)
        self.setWindowTitle("STUDENT APPLICATION - PERFORMANCE SHEET")
        # menu bar
        # mainMenu = self.menuBar()
        vbox_main = QVBoxLayout(self)
        functions = QGroupBox("FUNCTIONS")
        classes = QComboBox(self)
        list_of_classes = ["P1","P2","P3","P4","P5","P6","P7"]
        classes.addItems(list_of_classes)
        hbox = QHBoxLayout(self)
        select = QFormLayout(self)
        select.addRow("SELECT CLASS:",classes)
        update_marks = QPushButton("UPDATE MARKS")
        delete_student = QPushButton("DELETE STUDENT")
        print_performance_sheet = QPushButton("PRINT PERFORMANCE SHEET")
        print_report = QPushButton("PRINT REPORTS")
        back2main = QPushButton("BACK TO HOME")
        hbox.addLayout(select)
        hbox.addWidget(update_marks)
        hbox.addWidget(delete_student)
        hbox.addWidget(print_performance_sheet)
        hbox.addWidget(print_report)
        hbox.addWidget(back2main)
        functions.setLayout(hbox)
        #TableWidget
        table = QTableWidget(self)
        #setting the number of columnss
        table.setColumnCount(8)
        #headers resizing
        header = table.horizontalHeader()
        header.setSectionResizeMode(0,QHeaderView.Stretch)
        header.setSectionResizeMode(1,QHeaderView.Stretch)
        header.setSectionResizeMode(2,QHeaderView.Stretch)
        header.setSectionResizeMode(3,QHeaderView.Stretch)
        header.setSectionResizeMode(4,QHeaderView.Stretch)
        header.setSectionResizeMode(5,QHeaderView.Stretch)
        header.setSectionResizeMode(6,QHeaderView.Stretch)
        header.setSectionResizeMode(7,QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(["STUDENT NAMES","STREAM","MATH","ENGLISH","SCIENCE","SST","TOTAL","AVERAGE"])
        #selection behavior
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        vbox_main.addWidget(table)
        vbox_main.addWidget(functions)
        back2main.clicked.connect(self.back2mainpage)
        self.setLayout(vbox_main)

    def back2mainpage(self):
        self.mainpage = MainPage()
        self.close()
        self.mainpage.show()

class Teacher(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1000, 600)
        self.setWindowTitle("STUDENT APPLICATION - REGISTER CLASS TEACHER")
        hbox = QHBoxLayout(self)
        vbox = QVBoxLayout(self)
        label = QLabel("REGISTER A CLASS TEACHER",self)
        label.setFrameShape(QFrame.Panel)
        label.setAlignment(Qt.AlignCenter)
        layout = QFormLayout(self)
        layout.addRow("EMPLOYEE NUMBER",QLineEdit())
        layout.addRow("TEACHER'S NAMES",QLineEdit())
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("ADDRESS",QLineEdit())
        layout.addRow("CONTACT",QLineEdit())
        layout.addRow("RESPONSIBILITY",QLineEdit())
        buttons = QHBoxLayout(self)
        back2main = QPushButton("BACK TO HOME")
        save_details = QPushButton("SAVE DETAILS")
        space = QLabel(self)
        buttons.addWidget(back2main)
        buttons.addWidget(save_details)
        vbox.addStretch()
        vbox.addWidget(label)
        vbox.addLayout(layout)
        vbox.addWidget(space)
        vbox.addLayout(buttons)
        vbox.addStretch()
        vbox.addStretch()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()
        back2main.clicked.connect(self.back2mainpage)
        self.setLayout(hbox)

    def back2mainpage(self):
        self.mainpage = MainPage()
        self.close()
        self.mainpage.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MainPage()
    screen.show()
    sys.exit(app.exec_())













































