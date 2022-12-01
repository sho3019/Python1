import json
json_open = open('input2_no_error.json', 'r')                                                    #input1.jsonファイルを開く
json_load = json.load(json_open)                                                        #開いたファイルを読み込み

class Person:

    id: int = 0
    name: str = ""

class Score:

    japanese: int = 0
    mathematics: int = 0
    science : int = 0
    social_studies : int = 0
    english: int = 0


class Teacher(Person):

    subject: str = ""

class Student(Person):

    evaluation: str = ""
    score: Score = Score()

class Room:

    name: str = ""
    teacher: Teacher = Teacher()
    students: list[Student] = []


class Input:
    def input_room(self):
        room_name_list = []
        for i in range(len(json_load['room'])):
            room1 = Room()
            room1.name = json_load['room'][i]['name']
            room_name_list.append(room1.name)
        return room_name_list
        

    def input_teacher(self):
        teacher_list = []
        teacher_name_list = []
        teacher_id_list = []
        teacher_subject_list = []
        teacher1 = Teacher()
        for i in range(len(json_load['room'])):                 #Teacherはroomに対して、1人だから
            teacher1.name    = json_load['room'][i]['teacher']['name']
            teacher1.id      = json_load['room'][i]['teacher']['id']
            teacher1.subject = json_load['room'][i]['teacher']['subject']
            teacher_name_list.append(teacher1.name)
            teacher_id_list.append(teacher1.id)
            teacher_subject_list.append(teacher1.subject)
        teacher_list = [teacher_name_list, teacher_id_list, teacher_subject_list]
        return teacher_list


    def input_student(self):
        student1 = Student()
        score1   = Score()
        student_list       = []
        student_name_list  = []
        student_id_list    = []
        student_score_list = []
        student1.score = score1
        for i in range(len(json_load['room'])):
            st_student = 0
            st_student = len(json_load['room'][i]['students'])
        
            for n in range(st_student):
                student1.name = json_load['room'][i]['students'][n]['name']
                student1.id   = json_load['room'][i]['students'][n]['id']
                student_name_list.append(student1.name)
                student_id_list.append(student1.id)
                
                score1.japanese       = json_load['room'][i]['students'][n]['score']['japanese']
                score1.mathematics    = json_load['room'][i]['students'][n]['score']['mathematics']
                score1.science        = json_load['room'][i]['students'][n]['score']['science']
                score1.social_studies = json_load['room'][i]['students'][n]['score']['social_studies']
                score1.english        = json_load['room'][i]['students'][n]['score']['english']
                
                student_score_list.append(score1.japanese)
                student_score_list.append(score1.mathematics)
                student_score_list.append(score1.science)
                student_score_list.append(score1.social_studies)
                student_score_list.append(score1.english)
        
        student_list = [student_name_list, student_id_list, student_score_list]
        return student_list

room_list :list[Room] = []
input = Input()
room_name_list = input.input_room()
teacher_list = input.input_teacher()
student_list = input.input_student()

room_list = [room_name_list, teacher_list, student_list]
print(room_list)
