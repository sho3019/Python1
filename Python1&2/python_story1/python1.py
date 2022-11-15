from ftplib import error_perm
import json

json_open = open('input1.json', 'r')                                                    #input1.jsonファイルを開く
json_load = json.load(json_open)                                                        #開いたファイルを読み込み

f = open('check_results.txt', 'w')

st = len(json_load['students'])                                                         #jsonファイルのリストのstudentsの要素を確認

def id_unique(st):
    counts = []
    for n in range (st):                                                                    #studentsの要素文forループ
        flag = 0
        num = n - 1
        while(num >= 0):                                                                   #nが0以上の間whileループ
            if(json_load['students'][n]['id'] == json_load['students'][num]['id']):   #n番目とn-1番目のidが等しいか?
                    
                flag = 1
                break                                                              #nをデクリメント
            else:                                                                       #idがn番目とn - 1のidを比べて、idがユニークなとき    
                num = num - 1                                                               #nをデクリメント
        
        counts.append(flag)
            
    return counts

def subject_score(st, id_flag):
    for n in range(st):
        score_flag = []
        if(0 <= json_load['students'][n]['japanese'] <= 100):               #国語の点数
            score_flag.append(0) 
        
        else:
            score_flag.append(1)
                    
        if(0 <= json_load['students'][n]['mathematics'] <= 100):            #数学の点数
            score_flag.append(0)
        
        else:
            score_flag.append(1)
        
        if(0 <= json_load['students'][n]['science'] <= 100):                #科学の点数
            score_flag.append(0)
        
        else:
            score_flag.append(1)
        
        if(0 <= json_load['students'][n]['social_studies'] <= 100):         #社会の点数
            score_flag.append(0) 
            
        else:
            score_flag.append(1)

        if(0 <= json_load['students'][n]['english'] <= 100):                #英語の点数
            score_flag.append(0)
        else:
            score_flag.append(1)

        text_write(score_flag, id_flag, n)

def text_write(score_flag, count, n):
    error_flag = 0
    
    if(count[n] == 1):
        f.write(json_load['students'][n]['name'] + " "+ json_load['students'][n]['id']+ "  is not unique\n")
        error_flag = 1

    if (score_flag[0] == 1):
        f.write(json_load['students'][n]['name'] + ' "japanese" is not valid value\n')
        error_flag = 1

    if(score_flag[1] == 1):
        f.write(json_load['students'][n]['name'] + ' "mathematics" is not valid value\n')
        error_flag = 1
    
    if(score_flag[2] == 1):
        f.write(json_load['students'][n]['name'] + ' "science" is not valid value\n')
        error_flag = 1

    if(score_flag[3] == 1):
        f.write(json_load['students'][n]['name'] + ' "social_studies" is not valid value\n')
        error_flag = 1

    if(score_flag[4] == 1):
        f.write(json_load['students'][n]['name'] + ' "english" is not valid value\n')
        error_flag = 1

    if(error_flag == 0):
        f.write(json_load['students'][n]['name'] + "  All check passed\n")
        
count = id_unique(st)
subject_score(st, count)
f.close()