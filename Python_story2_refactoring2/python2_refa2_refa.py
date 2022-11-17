import json

#json_open = open('input2_error.json', 'r')                                                    #input1.jsonファイルを開く
json_open = open('input2_no_error.json', 'r')
json_load = json.load(json_open) 

f = open('check_no_error_results_refa.txt', 'w')
#f = open('check_error_results2_1.txt', 'w')

class Person():                 #Personクラス
    def __init__(self, id_list :int, name_list: int):
        """_summary_

        Args:
            id_list (int): _description_
            name_list (int): _description_
        """

        self.id_list = id_list
        self.name_list = name_list

    def input_id(self, id : int) ->int:
        """_summary_

        Args:
            id (int): _description_

        Returns:
            int: _description_
        """
        self.id = id
        self.id_list.append(self.id)

        return self.id_list
    
    def input_name(self, name : int)->int:
        """_summary_

        Args:
            name (int): _description_

        Returns:
            int: _description_
        """
        self.name = name
        self.name_list.append(self.name)
        
        return self.name_list

class Room(Person):                   #Roomクラス
      
    def __init__(self, id_list:int, name_list:int, subject:int, subject_list:int, room_name:int, room_name_list:int,):
        """_summary_

        Args:
            id_list (int): _description_
            name_list (int): _description_
            subject (int): _description_
            subject_list (int): _description_
            room_name (int): _description_
            room_name_list (int): _description_
        """
        self.room_name = room_name
        self.room_name_list = room_name_list
        self.teacher = Teacher(id_list, name_list, subject, subject_list)         #Teacherクラス呼び出し宣言
        self.students = Students(id_list, name_list)

        super(Room, self).__init__(id_list, name_list)
        

    def input_room_name(self)->int:
        """_summary_

        Returns:
            int: _description_
        """
        
        self.room_name_list.append(self.room_name)
        
        return self.room_name_list 

class Teacher(Person):          #Teacherクラス  Personクラスを継承
    def __init__(self, id_list:int, name_list:int, subject:int, subject_list:int)->int:
        """_summary_

        Args:
            id_list (int): _description_
            name_list (int): _description_
            subject (int): _description_
            subject_list (int): _description_

        Returns:
            int: _description_
        """
        self.subject = subject
        self.subject_list = subject_list

        super(Teacher, self).__init__(id_list, name_list)
    
    def input_subject(self)->int:
    
        self.subject_list.append(self.subject)

        return self.subject_list

class Students(Person):
    def __init__(self, id_list:int, name_list:int):
        """_summary_

        Args:
            id_list (int): _description_
            name_list (int): _description_
        """
        self.score = Score()

        super(Students, self).__init__(id_list, name_list)

class Score():
        
    def score(self, score_list:int, japanese:int, mathematics:int, science:int, social_studies:int, english:int)->int:
        """_summary_

        Args:
            score_list (int): _description_
            japanese (int): _description_
            mathematics (int): _description_
            science (int): _description_
            social_studies (int): _description_
            english (int): _description_

        Returns:
            int: _description_
        """
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
            room = Room(id_list, name_list, json_load['room'][i]['teacher']['subject'], 
            subject_list, json_load['room'][i]['name'], room_name_list)
        
            room_name_list = room.input_room_name() 
            teacher = Teacher(id_list, name_list, json_load['room'][i]['teacher']['subject'], subject_list)
            id_list = room.teacher.input_id(json_load['room'][i]['teacher']['id'])                                           #RoomクラスからTeacherクラスのinput_id()を呼ぶ方法
            #id_list = teacher.input_id(json_load['room'][i]['teacher']['id'])
            #name_list = room.teacher.input_name(json_load['room'][i]['teacher']['name'])                                        #RoomクラスからTeacherクラスのinput_name()を呼ぶ方法
            name_list = teacher.input_name(json_load['room'][i]['teacher']['name'])
            subject = room.teacher.input_subject()                                  #RoomクラスからTeacherクラスのinput_subject()を呼ぶ方法                        
            #subject_list = teacher.input_subject()

            for n in range(st_students):
                json_student = json_load['room'][i]['students'][n]                      #長いので省略

                student = Students(id_list, name_list)
                #id_list = room.students.input_id(json_student['id'])                                           #RoomクラスからStudentsクラス呼び出し
                id_list = student.input_id(json_student['id'])
                #name_list = room.students.input_name(json_student['name'])                                       #RoomクラスからStudentsクラス呼び出し
                name_list = student.input_name(json_student['name'])
                #print(id_list)
                scores = Score()
                """ score_list = scores.score(score_list, json_student['score']['japanese'], json_student['score']['mathematics'], 
                        json_student['score']['science'], json_student['score']['social_studies'], json_student['score']['english']) """
                score_list = student.score.score(score_list, json_student['score']['japanese'], json_student['score']['mathematics'], 
                        json_student['score']['science'], json_student['score']['social_studies'], json_student['score']['english'])
                #score_list = room.students.score.score(score_list, json_student['score']['japanese'], json_student['score']['mathematics'], 
                        #json_student['score']['science'], json_student['score']['social_studies'], json_student['score']['english'])
                
                


        print(id_list)
        print(name_list)
        #print(subject)
        print(score_list)

        carry_on = Carry_on()
        carry_on.carry(st_room, st_students, room_name_list, id_list, score_list, name_list)
        #a = room.teacher.input_id()
        #print(a)

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
