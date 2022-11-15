import json

#json_open = open('input2_no_error.json', 'r')                                                    #input1.jsonファイルを開く
json_open = open('input2_no_error.json', 'r')
json_load = json.load(json_open) 

f = open('check_no_error_results.txt', 'w')

st_room = len(json_load['room'])
st = len(json_load['room'][0]['students'])

#roomのnemeをチェックする関数   nameが'1st'か'2nd'のいずれかでなければroom_flagを1にする
def room_name(st_room):
    check_room = []
    for n in range(st_room):
        if(json_load['room'][n]['name'] == '1st' or json_load['room'][n]['name'] == '2nd'):
            room_flag = 0
        else:
            room_flag = 1
        
        check_room.append(room_flag)

    return check_room


################################################idチェック開始###############################
#idのリストを取得し、id_listに格納する関数
def id_check(st_room, st):                                  
    id_list = []

    for i in range(st_room):
        id_list.append(json_load['room'][i]['teacher']['id'])
        for n in range(st):
            id_list.append(json_load['room'][i]['students'][n]['id'])
    
    return id_list

#nameを取得し、name_listに格納する
def get_name(st_room, st):
    name_list = []
    for i in range(st_room):
        name_list.append(json_load['room'][i]['teacher']['name'])
        for n in range(st):
            name_list.append(json_load['room'][i]['students'][n]['name'])
    
    return name_list

 #idがユニークかチェックする関数   
def id_checker(id_list):
    
    id_flag = []
    list_st = len(id_list)

    for k in range(list_st):
        iflag = 0
        l = k - 1
        while(l >= 0):
            if(id_list[k] == id_list[l]):
                iflag = 1
                break
            else:
                l = l - 1
        id_flag.append(iflag)
    
    return id_flag

########################################idチェックここまで######################################

#各教科の点数をチェックする関数
def subject_score(st_room, st):
    score_flag = []
    for i in range(st_room):
        for n in range(st):
            #score_flag = []
            if(0 <= json_load['room'][i]['students'][n]['score']['japanese'] <= 100):               #国語の点数
                score_flag.append(0) 
            
            else:
                score_flag.append(1)
                        
            if(0 <= json_load['room'][i]['students'][n]['score']['mathematics'] <= 100):            #数学の点数
                score_flag.append(0)
            
            else:
                score_flag.append(1)
            
            if(0 <= json_load['room'][i]['students'][n]['score']['science'] <= 100):                #科学の点数
                score_flag.append(0)
            
            else:
                score_flag.append(1)
            
            if(0 <= json_load['room'][i]['students'][n]['score']['social_studies'] <= 100):         #社会の点数
                score_flag.append(0) 
                
            else:
                score_flag.append(1)

            if(0 <= json_load['room'][i]['students'][n]['score']['english'] <= 100):                #英語の点数
                score_flag.append(0)
            else:
                score_flag.append(1)
            #print("クラス"+ str(i) + "生徒" + str(n) ,score_flag)
    return score_flag

#text出力する関数
def text_write(check_room, score_flag, id_flag, id_list, name_list):
    
    #text = []
    id_st = len(id_flag)
    i = 0
    error_list = []
    for n in range(id_st):
        check_flag = 0
        if(n > 4):
            i = 1
        
        if(check_room[i] == 1):
            f.write(name_list[n] + " Room name must be ['1st', '2nd']\n")
            check_flag = 1

        if(id_flag[n] == 1):
            f.write(name_list[n] + " " + id_list[n] + "  is not unique\n")
            check_flag = 1

        if(n != 0 and n != 5):
            if(score_flag[0] == 1):
                f.write(name_list[n] + '"Japanese" is not valid value\n')
                check_flag = 1

            if(score_flag[1] == 1):
                f.write(name_list[n] + '"mathematics" is not valid value\n')
                check_flag = 1
                
            if(score_flag[2] == 1):
                f.write(name_list[n] + '"science" is not valid value\n')
                check_flag = 1

            if(score_flag[3] == 1):
                f.write(name_list[n] + '"social_studies" is not valid value\n')
                check_flag = 1

            if(score_flag[4] == 1):
                f.write(name_list[n] + '"english" is not valid value\n')
                check_flag = 1

            del score_flag[:5]              
        
        error_list.append(check_flag)
        if(check_flag == 0):
            f.write(name_list[n] + " All check passed\n")
    
    return error_list

#合計点数を求める関数
def total_score(st_room):
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
def evalution_judge(total):
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

#評価を基にjsonファイルを加工
def json_outputs(judge, st_room):
    for n in range(st_room):
        st_students = len(json_load['room'][n]['students'])
        
        for i in range(st_students):

            json_load['room'][n]['students'][i]['evaluation'] = judge[i]
            
            if(i == st_students - 1):
                del judge[:4]
    
    json_result = open('results3.json', 'w')
    json.dump(json_load, json_result, indent=4)


check_room = room_name(st_room)
id_list = id_check(st_room, st)
name_list = get_name(st_room, st)
id_flag = id_checker(id_list)
score_flag = subject_score(st_room, st)
error_list = text_write(check_room, score_flag, id_flag, id_list, name_list)
error_st = len(error_list)
han = []
for e in range(error_st):
    han.append(0)


if(error_list == han):
    total = total_score(st_room)
    judge = evalution_judge(total)
    json_outputs(judge, st_room)
else:
    print("error data is contain")
