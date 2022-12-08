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



room_list :list[Room] = []

room1 = Room()
room2 = Room()
room1.name = json_load['room'][0]['name']
#print(room1.name)
room2.name = json_load['room'][1]['name']
#print(room2.name)

teacher1 = Teacher()
teacher2 = Teacher()
teacher1.name = json_load['room'][0]['teacher']['name']
teacher2.name = json_load['room'][1]['teacher']['name']

#print(teacher1.name)
#print(teacher2.name)

teacher1.id = json_load['room'][0]['teacher']['id']
teacher2.id = json_load['room'][1]['teacher']['id']

#print(teacher1.id)
#print(teacher2.id)

teacher1.subject = json_load['room'][0]['teacher']['subject']
teacher2.subject = json_load['room'][1]['teacher']['subject']

#print(teacher1.subject)
#print(teacher2.subject)

room1.teacher = teacher1
room2.teacher = teacher2

teacher1_list = [teacher1.id, teacher1.name, teacher1.subject]
teacher2_list = [teacher2.id, teacher2.name, teacher2.subject]

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()
student6 = Student()
student7 = Student()
student8 = Student()

student1.name = json_load['room'][0]['students'][0]['name']
student2.name = json_load['room'][0]['students'][1]['name']
student3.name = json_load['room'][0]['students'][2]['name']
student4.name = json_load['room'][0]['students'][3]['name']
student5.name = json_load['room'][1]['students'][0]['name']
student6.name = json_load['room'][1]['students'][1]['name']
student7.name = json_load['room'][1]['students'][2]['name']
student8.name = json_load['room'][1]['students'][3]['name']

student1.id = json_load['room'][0]['students'][0]['id']
student2.id = json_load['room'][0]['students'][1]['id']
student3.id = json_load['room'][0]['students'][2]['id']
student4.id = json_load['room'][0]['students'][3]['id']
student5.id = json_load['room'][1]['students'][0]['id']
student6.id = json_load['room'][1]['students'][1]['id']
student7.id = json_load['room'][1]['students'][2]['id']
student8.id = json_load['room'][1]['students'][3]['id']

#score_name = ["score1", "score2", "score3", "score4", "score5", "score6", "score7", "score8"]

score1 = Score()
score2 = Score()
score3 = Score()
score4 = Score()
score5 = Score()
score6 = Score()
score7 = Score()
score8 = Score()

score1.japanese = json_load['room'][0]['students'][0]['score']['japanese']
score1.mathematics = json_load['room'][0]['students'][0]['score']['mathematics']
score1.science = json_load['room'][0]['students'][0]['score']['science']
score1.social_studies = json_load['room'][0]['students'][0]['score']['social_studies']
score1.english = json_load['room'][0]['students'][0]['score']['english']

score2.japanese = json_load['room'][0]['students'][1]['score']['japanese']
score2.mathematics = json_load['room'][0]['students'][1]['score']['mathematics']
score2.science = json_load['room'][0]['students'][1]['score']['science']
score2.social_studies = json_load['room'][0]['students'][1]['score']['social_studies']
score2.english = json_load['room'][0]['students'][1]['score']['english']

score3.japanese = json_load['room'][0]['students'][2]['score']['japanese']
score3.mathematics = json_load['room'][0]['students'][2]['score']['mathematics']
score3.science = json_load['room'][0]['students'][2]['score']['science']
score3.social_studies = json_load['room'][0]['students'][2]['score']['social_studies']
score3.english = json_load['room'][0]['students'][2]['score']['english']

score4.japanese = json_load['room'][0]['students'][3]['score']['japanese']
score4.mathematics = json_load['room'][0]['students'][3]['score']['mathematics']
score4.science = json_load['room'][0]['students'][3]['score']['science']
score4.social_studies = json_load['room'][0]['students'][3]['score']['social_studies']
score4.english = json_load['room'][0]['students'][3]['score']['english']

score5.japanese = json_load['room'][1]['students'][0]['score']['japanese']
score5.mathematics = json_load['room'][1]['students'][0]['score']['mathematics']
score5.science = json_load['room'][1]['students'][0]['score']['science']
score5.social_studies = json_load['room'][1]['students'][0]['score']['social_studies']
score5.english = json_load['room'][1]['students'][0]['score']['english']

score6.japanese = json_load['room'][1]['students'][1]['score']['japanese']
score6.mathematics = json_load['room'][1]['students'][1]['score']['mathematics']
score6.science = json_load['room'][1]['students'][1]['score']['science']
score6.social_studies = json_load['room'][1]['students'][1]['score']['social_studies']
score6.english = json_load['room'][1]['students'][1]['score']['english']


score7.japanese = json_load['room'][1]['students'][2]['score']['japanese']
score7.mathematics = json_load['room'][1]['students'][2]['score']['mathematics']
score7.science = json_load['room'][1]['students'][2]['score']['science']
score7.social_studies = json_load['room'][1]['students'][2]['score']['social_studies']
score7.english = json_load['room'][1]['students'][2]['score']['english']

score8.japanese = json_load['room'][1]['students'][3]['score']['japanese']
score8.mathematics = json_load['room'][1]['students'][3]['score']['mathematics']
score8.science = json_load['room'][1]['students'][3]['score']['science']
score8.social_studies = json_load['room'][1]['students'][3]['score']['social_studies']
score8.english = json_load['room'][1]['students'][3]['score']['english']


student1.score = score1
student2.score = score2
student3.score = score3
student4.score = score4
student5.score = score5
student6.score = score6
student7.score = score7
student8.score = score8

#print(student1.score.japanese)

#room1.students = [student1, student2, student3, student4]
#print(room1.students.student1)
student1_list = [student1.id, student1.name, student1.score.japanese, student1.score.mathematics, student1.score.science,
student1.score.social_studies, student1.score.english]

student2_list = [student2.id, student2.name, student2.score.japanese, student2.score.mathematics, student2.score.science,
student2.score.social_studies, student2.score.english]

student3_list = [student3.id, student3.name, student3.score.japanese, student3.score.mathematics, student3.score.science,
student3.score.social_studies, student3.score.english]

student4_list = [student4.id, student4.name, student4.score.japanese, student4.score.mathematics, student4.score.science,
student4.score.social_studies, student4.score.english]

student5_list = [student5.id, student5.name, student5.score.japanese, student5.score.mathematics, student5.score.science,
student5.score.social_studies, student5.score.english]

student6_list = [student6.id, student6.name, student6.score.japanese, student6.score.mathematics, student6.score.science,
student6.score.social_studies, student6.score.english]

student7_list = [student7.id, student7.name, student7.score.japanese, student7.score.mathematics, student7.score.science,
student7.score.social_studies, student7.score.english]

student8_list = [student8.id, student8.name, student8.score.japanese, student8.score.mathematics, student8.score.science,
student8.score.social_studies, student8.score.english]

room1.students = [student1_list, student2_list, student3_list, student4_list]

room2.students = [student5_list, student6_list, student7_list, student8_list]




print(room1.name)
print(room1.teacher.name)
print(room1.teacher.id)
print(room1.students)
#print(room1.students[0])
#print(room2.students[0])


room_list = [room1.name, teacher1_list, room1.students, room2.name, teacher2_list, room2.students]

#print(room_list)
#print(room_list[2][0][0])