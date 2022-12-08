from attr import validate
from jsonschema.validators import Draft4Validator, extend
from jsonschema import validate, ValidationError
import json

from pyparsing import results, traceback

total_schema = open("total.json", 'r')
total_schema = json.load(total_schema)
json_load = open('input3_error.json', 'r')
json_load = json.load(json_load)

#json_load = open('input3_no_error.json', 'r')
#json_load = json.load(json_load)
#f = open('check_no_error_results_refa.txt', 'w')
f = open('check_error_results_refa.txt', 'w')

class Check():
    def check_room(self, st_room):
        room_list = [0] * st_room
        room = Draft4Validator(total_schema)

        for i in range(len(json_load["room"])):
            room_error = sorted(room.iter_errors(json_load['room'][i]), key=lambda e: e.path)              #roomをschemaでチェック
        
            for room_errors in room_error:
                room_list[i] = 1
        return room_list

    def check_teacher(self, st_room, st_student):
        subject_list = [0] * st_room
        name_match_list = [0] * (st_room + st_student)
        name_type_list = [0] * (st_room + st_student)
        id_type_list = [0] * (st_room + st_student)

        teacher = Draft4Validator(total_schema["teacher"])
        for i in range(len(json_load["room"])):
            teacher_error = sorted(teacher.iter_errors(json_load['room'][i]['teacher']), key=lambda e: e.path) #teacherをschemaでチェック

            for teacher_errors in teacher_error:                #teacherのエラーを格納
                #print(teacher_errors.message)
                if(i == 1):
                    t_num = i + len(json_load['room'][i -1]["students"])
                else:
                    t_num = i
                if("Failed validating 'type' in schema['properties']['id']:" in str(teacher_errors)):   #idのtypeが違うか
                    id_type_list[t_num] = 1
                
                if(str(json_load["room"][i]["teacher"]["name"]) + " is not of type 'string'" in str(teacher_errors)):      #nameの型のチェック
                    name_type_list[t_num] = 1
                
                elif("'" + str(json_load["room"][i]["teacher"]["name"]) + "'" + " does not match '^[a-zA-Z]+$'" in str(teacher_errors)): #nameがA-Zかチェック
                    name_match_list[t_num] = 1
                
                if(str(json_load["room"][i]["teacher"]["subject"]) + " is not of type 'string'" in str(teacher_errors)):      #nameの型のチェック
                    subject_list[i] = 1
        
        return subject_list, name_match_list, name_type_list, id_type_list

    def check_students(self, name_match_list, name_type_list, id_type_list):
        students = Draft4Validator(total_schema["students"])
        
        for i in range(len(json_load["room"])):
            students_error = sorted(students.iter_errors(json_load['room'][i]['students']), key=lambda e: e.path)#studentsをschemaでチェック

            for students_errors in students_error:
                
                for k in range(4):
                    if (i == 1):
                        p = k + 6
                    else:
                        p = k + 1
                    
                    if(str(json_load['room'][i]['students'][k]["name"]) + " is not of type 'string'" in str(students_errors)):
                        name_type_list[p] = 1

                    if("'" + str(json_load["room"][i]["students"][k]["name"]) + "'" + " does not match '^[a-zA-Z]+$'" in str(students_errors)):
                        name_match_list[p] = 1
                    if(str(json_load["room"][i]["students"][k]["id"]) + " is not of type 'string'" in str(students_errors)):
                        #print("string Not")
                        id_type_list[p] = 1
        
        return name_match_list, name_type_list, id_type_list

    def check_score(self, st_student):
        s = Draft4Validator(total_schema["score"])
        score_type_list = [0] * (st_student * 5)
        score_value_list = [0] * (st_student * 5)
        subject = ["['japanese']", "['mathematics']","['science']", "['social_studies']", "['english']"] 
        for i in range(len(json_load["room"])):
            for n in range(len(json_load["room"][i]["students"])):
                score_error = sorted(s.iter_errors(json_load['room'][i]['students'][n]['score']), key=lambda e: e.path)
                
                for score_errors in score_error:                                                        #エラーからstudentsを特定し、リストに格納
                    #print(score_errors.message)
                    score = traceback.format_exception_only(score_errors)
                    if (i == 1):
                            n = n + 3
                    for st in range(len(subject)):
                        if("'type' in schema['properties']" + subject[st] in score[0]):
                            score_type_list[(i + n)* 5 + st] = 1

                        if("'minimum' in schema['properties']" + subject[st] in score[0] ):
                            score_value_list[(i + n)* 5 + st] = 1
                        elif("'maximum' in schema['properties']" + subject[st] in score[0]):
                            score_value_list[(i + n)* 5 + st] = 1
                            
                        else:
                            pass

                    
        return score_type_list, score_value_list
                
    def check_id(self, id_list):
        id_unique_list = [0]
        item = {
            "id_unique":[
                {
                    "id_uni":id_list
                }
            ]
        }

        try:
            validate(item["id_unique"], total_schema["id_unique"])
        except ValidationError as e:
            #print(e.message)
            id_unique_list[0] = 1
        
        return id_unique_list

    def check_unique_id(seif, id_list):
        list_st = len(id_list)
        id_flag = [0] * list_st

        for i in range(list_st - 1):                  # 0 ~ studentsの数 -1だけループ　　最後の人は見る必要ないから     
            for n in range(i + 1, list_st):
                if(id_list[i] == id_list[n]):             #今のidと他のidが一致しているか
                    id_flag[i] = 1              #今のidに1を入れる
                    id_flag[n] = 1              #今のidと一致した他のidに1を入れる                   
        
        return id_flag

class Write:
    def write_text(self, room_list, subject_list, name_match_list, name_type_list, id_type_list,
 score_value_list, score_type_list, id_unique_flag, name_list, id_list):
        
        subjects = ['"japanese"', '"mathematics"', '"science"', '"social_studies"', '"english"']    #教科のリストを作成

        #st_id = len(id_flag)
        st_subject = len(subjects)
        i = 0
        error_list = []

        for i in range(len(json_load['room'])):
            st_student = len(json_load['room'][i]['students'])
            if(subject_list[i] == 1):
                t = 0
                f.write(str(name_list[t]) + " subject type is not string\n")
                check_flag = 1

            for n in range(st_student + 1):
                check_flag = 0
                if(room_list[i] == 1):
                    f.write(str(name_list[n]) + " Room name must be ['1st', '2nd']\n")
                    check_flag = 1
                if(name_type_list[n] == 1):
                    f.write(str(name_list[n]) + " name type is not string\n")
                    check_flag = 1
                if(name_match_list[n] == 1):
                    f.write(str(name_list[n]) + " name is not match name\n")
                    check_flag = 1
                if(id_type_list[n] == 1):
                    f.write(str(name_list[n]) + " " + str(id_list[n]) + " is not type string\n")
                    check_flag = 1
                if(id_unique_flag[n] == 1):
                    f.write(str(name_list[n]) + " " + str(id_list[n]) + "  is not unique\n")
                    check_flag = 1
                #print(name_list[0])
                if(n != 0 and n != 5):
                    for s in range(st_subject):
                        if(score_value_list[s] == 1):
                            f.write(str(name_list[n]) + " " + str(subjects[s]) + " is not valid value\n")
                            check_flag = 1
                        if(score_type_list[s] == 1):
                            f.write(str(name_list[n]) + " " + str(subjects[s]) + " is not type integer\n")
                            check_flag = 1

                    del score_value_list[:5]
                    del score_type_list[:5]            
            
                error_list.append(check_flag)
                if(check_flag == 0):
                    f.write(str(name_list[n]) + " All check passed\n")
            del name_list[:5]
            del name_type_list[:5]
            del name_match_list[:5]
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
                sum = int(cp['japanese']) + int(cp['mathematics']) + int(cp['science']) + int(cp['social_studies']) + int(cp['english'])
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
        return 0

class Error():
    def check_error(self, error_list, st_room):
        error_flag = [0] * len(error_list)
        if(error_flag == error_list):
            result = "OK"
        else:
            print("error data is contain")
            result = "error data is contain"
        
        return result

st_room = len(json_load["room"])

st_student = 0
name_list = []
id_list = []
for i in range(st_room):  
    st_student = st_student + len(json_load["room"][i]["students"])
    st_students = len(json_load["room"][i]["students"])
    name_list.append(json_load["room"][i]["teacher"]["name"])
    id_list.append(json_load["room"][i]["teacher"]["id"])
    for n in range(st_students):
        name_list.append(json_load["room"][i]["students"][n]["name"])
        id_list.append(json_load["room"][i]["students"][n]["id"])

#print(name_list)
#print(id_list)
check = Check()
room_list = check.check_room(st_room)
teacher_list = check.check_teacher(st_room, st_student)
subject_list = teacher_list[0]
name_match_list = teacher_list[1]
name_type_list = teacher_list[2]
id_type_list = teacher_list[3]
#print(teacher_list)

student_list = check.check_students(name_match_list, name_type_list, id_type_list)
name_match_list = student_list[0]
name_type_list = student_list[1]
id_type_list = student_list[2]

score_list = check.check_score(st_student)
score_type_list = score_list[0]
score_value_list = score_list[1]

id_unique_list = check.check_id(id_list)

write = Write()
id_unique_flag = [0] * (st_room + st_student)
if(id_unique_list == [1]):
    id_unique_flag = check.check_unique_id(id_list)

#print("id_flag : " + str(id_unique_flag))
error_list = write.write_text(room_list, subject_list, name_match_list, name_type_list, id_type_list,
score_value_list, score_type_list, id_unique_flag, name_list, id_list)

print(error_list)

error = Error()
result = error.check_error(error_list, st_room)

""" if(error_list == error_flag):
    total = evaluation.total_score(st_room)
    judge = evaluation.judge_evaluation(total)
    make_json.output_json(judge, st_room)
else:
    print("error data is contain") """
evaluation = Evaluation()
make_json  = Make_json()
if(result == "OK"):
    total = evaluation.total_score(st_room)
    judge = evaluation.judge_evaluation(total)
    make_json.output_json(judge, st_room)
