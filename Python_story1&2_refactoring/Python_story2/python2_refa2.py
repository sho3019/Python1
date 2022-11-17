import json

#json_open = open('input2_error.json', 'r')                                                    #input1.jsonファイルを開く
json_open = open('input2_no_error.json', 'r')
json_load = json.load(json_open) 

f = open('check_no_error_results.txt', 'w')
#f = open('check_error_results2_1.txt', 'w')

class Room():                   #Roomクラス
      
    def __init__(self, name):
        self.name = name

    def input_room_name(self, room_name_list):
        self.room_name_list = room_name_list
        self.room_name_list.append(self.name)
        

        return self.room_name_list

class Person():                 #Personクラス
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input_id(self, id_list):
        self.id_list = id_list
        self.id_list.append(self.id)

        return self.id_list
    
    def input_name(self, name_list):
        self.name_list = name_list
        self.name_list.append(self.name)
        
        return self.name_list

class Teacher(Person):          #Teacherクラス  Personクラスを継承
    
    def input_subject(self, subject, subject_list):
        self.subject = subject
        self.subject_list = subject_list
        self.subject_list.append(self.subject)

        return self.subject_list

class Student(Person):

    def score(self, score_list, japanese, mathematics, science, social_studies, english):
        self.score_list = score_list
        self.japanese = japanese
        self.mathematics = mathematics
        self.science = science
        self.social_studies = social_studies
        self.english = english
        
        list = [self.japanese, self.mathematics, self.science, self.social_studies, self.english]

        for i in list:
            self.score_list.append(i)
    
        return self.score_list
              
class Check_room():
    #roomのnemeをチェックする関数   nameが'1st'か'2nd'のいずれかでなければroom_flagを1にする
    def name_room(self, st_room, room_name_list):
        check_room = []
        
        for n in range(st_room):
            if(room_name_list[n] == '1st' or room_name_list[n] == '2nd'):
                room_flag = 0
            else:
                room_flag = 1
            
            check_room.append(room_flag)

        return check_room

class Check_id():
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


class Check_score():
    #各教科の点数をチェックする関数
    def subject_score(self, score_list):
        score_flag = []
        st_score = len(score_list)

        for i in range(st_score):
            if(0 <= score_list[i] <= 100):               #各教科の点数が0点以上100点以下か判定
                score_flag.append(0) 
            
            else:
                score_flag.append(1)
        
        return score_flag


class Output_text():
    def write_text(self, check_room, score_flag, id_flag, id_list, name_list):
        
        subjects = ['"japanese"', '"mathematics"', '"science"', '"social_studies"', '"english"']    #教科のリストを作成

        st_id = len(id_flag)
        st_subject = len(subjects)
        i = 0
        error_list = []

        for n in range(st_id):
            check_flag = 0
            if(n > 4):                                                              #生徒の数が4人超えたら2つ目のクラス
                i = 1
            
            if(check_room[i] == 1):
                f.write(name_list[n] + " Room name must be ['1st', '2nd']\n")
                check_flag = 1

            if(id_flag[n] == 1):
                f.write(name_list[n] + " " + id_list[n] + "  is not unique\n")
                check_flag = 1

            if(n != 0 and n != 5):
                for s in range(st_subject):
                    if(score_flag[s] == 1):
                        f.write(name_list[n] + " " + subjects[s] + " is not valid value\n")
                        check_flag = 1

                del score_flag[:5]              
            
            error_list.append(check_flag)
            if(check_flag == 0):
                f.write(name_list[n] + " All check passed\n")
        
        return error_list


class Evaluation():
#合計点数を求める関数
    def total_score(self, score_list, st_students, st_room):
        st_students = st_students * st_room
        total = [0] * st_students

        for n in range(st_students):
            sum = 0
            for i in range(5):
                sum = sum + score_list[i]
            total[n] = sum
            del score_list[:5]
        
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
    def output_json(self, judge, st_room, st_students):
        for n in range(st_room):
            for i in range(st_students):

                json_load['room'][n]['students'][i]['evaluation'] = judge[i]
                
                if(i == st_students - 1):
                    del judge[:4]
        
        json_result = open('results.json', 'w')
        json.dump(json_load, json_result, indent=4)


class Json_class():

    def make_class(self):
        room_name_list = []
        id_list = []
        name_list = []
        subject_list = []
        score_list = []
        st_room = len(json_load['room'])
        st_students = len(json_load['room'][0]['students'])
        #print(st_students)
        for i in range(st_room):
            room = Room(json_load['room'][i]['name'])
            room_name_list = room.input_room_name(room_name_list)

            teacher = Teacher(json_load['room'][i]['teacher']['id'], json_load['room'][i]['teacher']['name'])
            id_list = teacher.input_id(id_list)
            name_list = teacher.input_name(name_list)
            subject_list = teacher.input_subject(json_load['room'][i]['teacher']['subject'], subject_list)
            for n in range(st_students):
                json_student = json_load['room'][i]['students'][n]                      #長いので省略

                student = Student(json_student['id'], json_student['name'])
                id_list = student.input_id(id_list)
                name_list = student.input_name(name_list)

                score_list = student.score(score_list, json_student['score']['japanese'], json_student['score']['mathematics'], 
                json_student['score']['science'], json_student['score']['social_studies'], json_student['score']['english'])
    
        carry_on = Carry_on()
        carry_on.carry(st_room, st_students, room_name_list, id_list, score_list, name_list)


class Carry_on():

    def carry(self, st_room, st_students, room_name_list, id_list, score_list, name_list):
        check_room = Check_room()
        check_room = check_room.name_room(st_room, room_name_list) 
        
        check_id = Check_id()
        id_flag = check_id.check_id(id_list)

        check_score = Check_score()
        score_flag = check_score.subject_score(score_list)

        output_txt = Output_text()
        error_list = output_txt.write_text(check_room, score_flag, id_flag, id_list, name_list)


        evaluation = Evaluation()
        make_json  = Make_json()
        error_st = len(error_list)
        flag = [0] * error_st

        if(error_list == flag):
            total = evaluation.total_score(score_list, st_students, st_room)
            #print(total)
            judge = evaluation.judge_evaluation(total)
            #print(judge)
            make_json.output_json(judge, st_room, st_students)
        else:
            print("error data is contain")



def main():
    
    json_class = Json_class()
    json_class.make_class()
    

if __name__ == '__main__':

    main()
