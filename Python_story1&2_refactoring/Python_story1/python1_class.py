import json
from tabnanny import check
from unicodedata import name

json_open = open('input1.json', 'r')                                                    #input1.jsonファイルを開く
json_load = json.load(json_open)                                                        #開いたファイルを読み込み

f = open('check_results.txt', 'w')


class Student():
    def __init__(self, id :int, name :int, japanese :int, mathematics :int, science :int, social_studies :int, english :int):
        """_summary_

        Args:
            id (int): _description_
            name (int): _description_
            japanese (int): _description_
            mathematics (int): _description_
            science (int): _description_
            social_studies (int): _description_
            english (int): _description_
        """
        self.id = id
        self.name = name
        self.japanese = japanese
        self.mathematics = mathematics
        self.science = science
        self.social_studies = social_studies
        self.english = english

    
    def input_id(self, id_list :int) -> int:
        """_summary_

        Args:
            id_list (int): _description_

        Returns:
            int: _description_
        """
        self.id_list = id_list
        self.id_list.append(self.id)

        return self.id_list

    def input_name(self, name_list :int) -> int:
        """_summary_

        Args:
            name_list (int): _description_

        Returns:
            int: _description_
        """
        self.name_list = name_list
        self.name_list.append(self.name)

        return self.name_list

    def score(self, score_list :int) ->int:
        """_summary_

        Args:
            score_list (int): _description_

        Returns:
            int: _description_
        """
        self.score_list = score_list

        list = [self.japanese, self.mathematics, self.science, self.social_studies, self.english]

        for i in list:
            self.score_list.append(i)
        
        return self.score_list

class Check_data():
    def check_id(self, id_list : int, st_student : int) -> int:
        """_summary_

        Args:
            id_list (int): _description_
            st_student (int): _description_

        Returns:
            int: _description_
        """

        id_flag = [0] * st_student                      #id_flagを作成　studentsの数だけリストに0を入れる
        
        for i in range(st_student -1):                  # 0 ~ studentsの数 -1だけループ　　最後の人は見る必要ないから     
            for n in range(i + 1, st_student):
                if(id_list[i] == id_list[n]):             #今のidと他のidが一致しているか
                    id_flag[i] = 1              #今のidに1を入れる
                    id_flag[n] = 1              #今のidと一致した他のidに1を入れる                   

        return id_flag

    def subject_score(self, score_list :int) ->int:
        """_summary_

        Args:
            score_list (int): _description_

        Returns:
            int: _description_
        """
        score_flag = []
        st_score = len(score_list)

        for i in range(st_score):
            if(0 <= score_list[i] <= 100):               #各教科の点数が0点以上100点以下か判定
                score_flag.append(0) 
            
            else:
                score_flag.append(1)
        
        return score_flag

    def write_text(self, id_flag :int, score_flag :int, st_students :int, name_list :int, id_list :int):
        """_summary_

        Args:
            id_flag (int): _description_
            score_flag (int): _description_
            st_students (int): _description_
            name_list (int): _description_
            id_list (int): _description_
        """
        subjects = ['"japanese"', '"mathematics"', '"science"', '"social_studies"', '"english"']    #教科のリストを作成
        st_subject = len(subjects)

        #print(score_flag)
        for i in range(st_students):
            check_flag = 0
            if(id_flag[i] == 1):
                f.write(name_list[i] + " " + id_list[i] + "  is not unique\n")
                check_flag = 1

            for s in range(st_subject):
                if(score_flag[s] == 1):
                    f.write(name_list[i] + " " + subjects[s] + " is not valid value\n")
                    check_flag = 1 
            del score_flag[:5]
            
            if(check_flag == 0):
                f.write(name_list[i] + " All check passed\n")


class Storage():
    def storage_data(self):
        
        id_list = []
        name_list = []
        score_list = []


        st_students = len(json_load['students'])
        for i in range(st_students):
            student = Student(json_load['students'][i]['id'], json_load['students'][i]['name'], json_load['students'][i]['japanese'], 
            json_load['students'][i]['mathematics'], json_load['students'][i]['science'], json_load['students'][i]['social_studies'], json_load['students'][i]['english'])

            id_list = student.input_id(id_list)
            name_list = student.input_name(name_list)
            score_list = student.score(score_list)
        
        print(id_list)
        print(name_list)
        print(score_list)
        carryy_on = Carry_on()
        carryy_on.carry(id_list, name_list, score_list, st_students)

class Carry_on():
    def carry(self, id_list :int, name_list :int, score_list :int, st_students :int):
        """_summary_

        Args:
            id_list (int): _description_
            name_list (int): _description_
            score_list (int): _description_
            st_students (int): _description_
        """
        check_data = Check_data()
        id_flag = check_data.check_id(id_list, st_students)
        score_flag = check_data.subject_score(score_list)
        check_data.write_text(id_flag, score_flag, st_students, name_list, id_list)
        f.close()


def main():
    storage = Storage()
    storage.storage_data()

if __name__ == '__main__':

    main()


