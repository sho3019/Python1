import json
json_open = open('input2_no_error.json', 'r')                                                    #input1.jsonファイルを開く
#json_open = open('input2_error.json', 'r') 
json_load = json.load(json_open)                                                        #開いたファイルを読み込み

f = open('check_no_error_results_refa.txt', 'w')
#f = open('check_error_results_refa.txt', 'w')

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


class Check():
    def name_room(self, room_list):
        check_room = []

        for n in range(len(room_list[0])):
            if(room_list[0][n] == '1st' or  '2nd'):
                room_flag = 0
            else:
                room_flag = 1
            
            check_room.append(room_flag)

        return check_room
    #idがユニークかチェックする関数   
    def check_id(seif, id_list):
        
        list_st = len(id_list)
        id_flag = [0] * list_st

        for i in range(list_st - 1):                  # 0 ~ studentsの数 -1だけループ　　最後の人は見る必要ないから     
            for n in range(i + 1, list_st):
                if(id_list[i] == id_list[n]):             #今のidと他のidが一致しているか
                    id_flag[i] = 1              #今のidに1を入れる
                    id_flag[n] = 1              #今のidと一致した他のidに1を入れる                   
        
        return id_flag

    def subject_score(self, room_list):
        score_list = room_list[2][2]
        #sprint(score_list)
        score_flag = []
        st_score = len(score_list)

        for i in range(st_score):
            if(0 <= score_list[i] <= 100):               #各教科の点数が0点以上100点以下か判定
                score_flag.append(0) 
            
            else:
                score_flag.append(1)
        
        return score_flag

    def write_text(self, room_flag, score_flag, id_flag, id_list, name_list):
        
        subjects = ['"japanese"', '"mathematics"', '"science"', '"social_studies"', '"english"']    #教科のリストを作成

        st_id = len(id_flag)
        st_subject = len(subjects)
        i = 0
        error_list = []

        for i in range(len(json_load['room'])):
            st_student = len(json_load['room'][i]['students'])

            for n in range(st_student + 1):
                check_flag = 0
                if(room_flag[i] == 1):
                    f.write(name_list[n] + " Room name must be ['1st', '2nd']\n")
                    check_flag = 1

                if(id_flag[n] == 1):
                    f.write(name_list[n] + " " + id_list[n] + "  is not unique\n")
                    check_flag = 1
                #print(name_list[0])
                if(n != 0 and n != 5):
                    for s in range(st_subject):
                        if(score_flag[s] == 1):
                            f.write(name_list[n] + " " + subjects[s] + " is not valid value\n")
                            check_flag = 1

                    del score_flag[:5]              
            
                error_list.append(check_flag)
                if(check_flag == 0):
                    f.write(name_list[n] + " All check passed\n")
            del name_list[:5]
            #print(name_list)
        
        return error_list

class Evaluation():
#合計点数を求める関数
    def total_score(self, st_room):
        sum = 0
        total = []
        
        for n in range(st_room):
            st_students = len(json_load['room'][n]['students'])
            for i in range(st_students):
                cp = json_load['room'][n]['students'][i]['score']
                sum = cp['japanese'] + cp['mathematics'] + cp['science'] + cp['social_studies'] + cp['english']
                total.append(sum)
        return total

    #合計点から評価を判定する関数       
    def judge_evaluation(self, total):
        st_total = len(total)
        judge = []
        for i in range(st_total):
            if(0 <= total[i] <= 100 ):
                judge.append('E')
            
            elif(101 <= total[i] <= 200):
                judge.append('D')
            
            elif(201 <= total[i] <= 300):
                judge.append('C')
            
            elif(301 <= total[i] <= 400):
                judge.append('B')
            
            elif(401 <= total[i] <= 500):
                judge.append('A')
        return judge

class Make_json():
    #評価を基にjsonファイルを加工
    def output_json(self, judge, st_room):
        for n in range(st_room):
            st_students = len(json_load['room'][n]['students'])
            
            for i in range(st_students):

                json_load['room'][n]['students'][i]['evaluation'] = judge[i]
                
                if(i == st_students - 1):
                    del judge[:4]
        
        json_result = open('results3.json', 'w')
        json.dump(json_load, json_result, indent=4)


room_list :list[Room] = []
input = Input()
room_name_list = input.input_room()
teacher_list = input.input_teacher()
student_list = input.input_student()

room_list = [room_name_list, teacher_list, student_list]


check = Check()
id_list = room_list[2][1]
id_list.insert(0, room_list[1][1][0])
id_list.insert(5, room_list[1][1][1])

#print(id_list)

name_list = room_list[2][0]
name_list.insert(0, room_list[1][0][0])
name_list.insert(5, room_list[1][0][1])
#print(name_list)
room_flag = check.name_room(room_list)
#print(room_flag)
id_flag = check.check_id(id_list)
#print(id_flag)

score_flag = check.subject_score(room_list)
#print(score_flag)

error_list = check.write_text(room_flag, score_flag, id_flag, id_list, name_list)
#print(error_list)
evaluation = Evaluation()
make_json  = Make_json()
error_st = len(error_list)
han = [0] * error_st
st_room = len(room_list[0])
print(room_list[0])
if(error_list == han):
    total = evaluation.total_score(st_room)
    judge = evaluation.judge_evaluation(total)
    make_json.output_json(judge, st_room)
else:
    print("error data is contain")