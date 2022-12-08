import json

json_open = open('input1.json', 'r')                                                    #input1.jsonファイルを開く
json_load = json.load(json_open)                                                        #開いたファイルを読み込み

f = open('check_results1_4.txt', 'w')

st_student = len(json_load['students'])                                                         #jsonファイルのリストのstudentsの要素を確認


def get_id(st_student: int) -> int:
    """_summary_

    Args:
        st_student (int): _description_

    Returns:
        int: _description_
    """
    id_list = []

    for i in range(st_student):
        id_list.append(json_load['students'][i]['id'])

    return id_list

def check_id(id_list : int, st_student : int) -> int:
    """_summary_

    Args:
        id (int): _description_
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

def subject_score(st_student : int, id_flag : int):
    """_summary_

    Args:
        st_student (int): _description_
        id_flag (int): _description_
    """
    subject_list = ['japanese', 'mathematics', 'science', 'social_studies', 'english']
    

    for n in range(st_student):
        score_flag = []
        json = json_load['students'][n]

        for s in subject_list:
            if(0 <= json[s] <= 100):                #各教科が0点以上で100点以下かチェック
                score_flag.append(0)                #score_flagに0を追加
            
            else:
                score_flag.append(1)                #そうでないならscore_flagに1を追加

        #print(score_flag)
        write_text(score_flag, id_flag, n)

def write_text(score_flag : int, id_flag : int, n : int):
    """_summary_

    Args:
        score_flag (int): _description_
        id_flag (int): _description_
        n (int): _description_
    """
    error_flag = 0
    st_score = len(score_flag)
    subjects = ['"japanese"', '"mathematics"', '"science"', '"social_studies"', '"english"']    #教科のリストを作成

    json_name = json_load['students'][n]['name']                                                #json_nameにnameを格納
    
    if(id_flag[n] == 1):                                                                        #idがユニークでない場合の処理         
        f.write(json_name + " "+ json_load['students'][n]['id']+ "  is not unique\n")
        error_flag = 1

    for i in range(st_score):
        if (score_flag[i] == 1):                                                                #i番目の教科が異常値の場合の処理
            f.write(json_name + " " + subjects[i] + ' is not valid value\n')
            error_flag = 1

    if(error_flag == 0):
        f.write(json_name + "  All check passed\n")

id_list = get_id(st_student)        
id_flag = check_id(id_list, st_student)
subject_score(st_student, id_flag)
f.close()