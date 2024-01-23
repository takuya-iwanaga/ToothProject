#fastapiのモジュール
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List
import re

#postgreの接続のモジュール
import psycopg2
from psycopg2 import errors

#エラーの種類
InFailedSqlTransaction = errors.lookup('25P02')

UndefinedColumn=errors.lookup('42703')



#メイン画面に表示される情報を取得する
main_view_info_query="""SELECT T1.user_name,T1.user_img,T3.ticket_id,T3.reserved_date,T1.user_id ,T3.reserved_time,T4.hospital_name FROM registrants_info as T1 INNER JOIN visiting_hospital_info as T2 ON T2.hospital_list_id=T1.hospital_list_id INNER JOIN hospital_reserved_info as T3 ON T3.user_id=T1.user_id INNER JOIN hospital_info as T4 ON T4.hospital_id=T2.hospital_id AND T4.hospital_id=T3.hospital_id where T3.reserved_date=(SELECT MIN(reserved_date) FROM hospital_reserved_info where reserved_check=false) AND T3.reserved_check=false;"""


#予約情報画面に表示される情報を取得する(前半)
reserved_view_info_query_first="""SELECT T3.reserved_date,T3.reserved_time,T4.hospital_name FROM hospital_reserved_info as T3 INNER JOIN hospital_info as T4 ON T3.hospital_id=T4.hospital_id where T3.user_id="""
#予約情報画面に表示される情報を取得する(後半)
reserved_view_info_query_second=""" AND T3.reserved_check=false ORDER BY T3.reserved_date"""


#予約追加できる時間帯のリストの取得
reserved_view_adding_list_query="""SELECT open_time,close_time,running_day FROM hospital_running_time_info where hospital_id="""

#予約する病院の予約追加可能状況の取得
reserved_view_adding_possible_list_query=""""""

#-----------------------------------------------------

#曜日の辞書を定義
keys = [ '0','1', '2','3', '4', '5','6']
values = ['月','火','水','木','金','土','日']
weekday = dict(zip(keys, values))

#数字を半角から全角に変換する
z_digit = '１２３４５６７８９０'
h_digit = '1234567890'

h2z_digit = str.maketrans(h_digit, z_digit)

#メイン画面に表示される情報を整理する関数
def main_view_info(main_view_info_query,weekday,h2z_digit):
    connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
    cur = connection.cursor()
    cur.execute(main_view_info_query)
    main_view_info_result = cur.fetchall()
    cur.close()

    print(main_view_info_result)
    #曜日情報を取得
    key=main_view_info_result[0][3].weekday()
    days=weekday[str(key)]

    #日時を文字列に変換
    dt_d=main_view_info_result[0][3].strftime('%Y/%m/%d')
    dt_t=main_view_info_result[0][5].strftime('%H:%M')

    reserved_date=dt_d.translate(h2z_digit)+'（'+days+')'+'　'+dt_t.translate(h2z_digit)+'〜'

    #送信するデータを作成
    main_info_result={"user_name":main_view_info_result[0][0],"user_id":str(main_view_info_result[0][4]),"reserved_number":str(main_view_info_result[0][2]),"reserved_data":reserved_date,"hospital_name":main_view_info_result[0][6]}
    
    return main_info_result

#------------------------------------------------------------------------------


##予約情報の画面に表示される情報を整理する関数
def reserved_view_info(reserved_view_info_query_first,reserved_view_info_query_second,user_id,h2z_digit):
    reserved_info_list_result=[]
    #予約情報のSQLの例外処理
    try:
        #user_idを元に予約情報を取得
        connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
        cur = connection.cursor()
        reserved_view_info_query=reserved_view_info_query_first+user_id+reserved_view_info_query_second
        cur.execute(reserved_view_info_query)
        reserved_view_info_result = cur.fetchall()
        connection.close()
        print(reserved_view_info_result)

        for i in range(len(reserved_view_info_result)):
            #曜日情報を取得
            key=reserved_view_info_result[i][0].weekday()
            days=weekday[str(key)]
            #日時を文字列に変換
            dt_d=reserved_view_info_result[i][0].strftime('%Y/%m/%d')
            dt_t=reserved_view_info_result[i][1].strftime('%H:%M')
            #送信するデータを作成
            reserved_date=dt_d.translate(h2z_digit)+'（'+days+')'+'　'+dt_t.translate(h2z_digit)+'〜'
            reserved_info_result={"reserved_data":reserved_date,"hospital_name":reserved_view_info_result[i][2]}
            reserved_info_list_result.append(reserved_info_result)
        return reserved_info_list_result
    
    except psycopg2.InterfaceError as e:
        connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
        cur = connection.cursor()
        if (user_id=='undefined'):
            connection.close()
            return {"res":"01:エラーが発生しましたメイン画面に戻ってもう一度ご予約ボタンを押してください"}       
        reserved_view_info_query=reserved_view_info_query_first+user_id+reserved_view_info_query_second
        cur.execute(reserved_view_info_query)
        reserved_view_info_result = cur.fetchall()
        connection.close()
        print(reserved_view_info_result)

        for i in range(len(reserved_view_info_result)):
            #曜日情報を取得
            key=reserved_view_info_result[i][0].weekday()
            days=weekday[str(key)]
            #日時を文字列に変換
            dt_d=reserved_view_info_result[i][0].strftime('%Y/%m/%d')
            dt_t=reserved_view_info_result[i][1].strftime('%H:%M')
            #送信するデータを作成
            reserved_date=dt_d.translate(h2z_digit)+'（'+days+')'+'　'+dt_t.translate(h2z_digit)+'〜'
            reserved_info_result={"reserved_data":reserved_date,"hospital_name":reserved_view_info_result[i][2]}
            reserved_info_list_result.append(reserved_info_result)
        return reserved_info_list_result
    
    except UndefinedColumn as e:
        connection.rollback()
        reserved_info_result={"res":"02:エラーが発生しましたメイン画面に戻ってもう一度ご予約ボタンを押してください"}
        return reserved_info_result
    
    except InFailedSqlTransaction as e:
        connection.rollback()
        reserved_info_result={"res":"03:エラーが発生しましたメイン画面に戻ってもう一度ご予約ボタンを押してください"}
        return reserved_info_result


#------------------------------------------------- 
#予約可能な時間帯のデータをまとめる関数
def reserved_view_adding(reserved_view_adding_list_query,hospital_id):
    reserved_adding_list_result=[]

    connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
    cur = connection.cursor()
    cur.execute(reserved_view_adding_list_query+hospital_id)
    reserved_adding_result=cur.fetchall()
    for i in range(len(reserved_adding_result)):
        adding_result={"open_time":reserved_adding_result[i][0],"close_time":reserved_adding_result[i][1],"running_day":reserved_adding_result[i][2]}
        reserved_adding_list_result.append(adding_result)
    print(reserved_adding_list_result)

    connection.close()
    return reserved_adding_list_result

#予約する日程を追加する関数
def adding_reserved_day_to_list(inserting_day):
    #DBの接続
    connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
    cur = connection.cursor()
    #予約する日付を年,月,日の要素で区切る
    day=re.split('[年,月,日]',inserting_day.day)
    #予約する時間を~で区切る
    time=inserting_day.time.split("~")
    #予約する時間をクエリ文で読み込めるよう加工
    reserved_time="'"+time[0]+"'"
    #予約する月が１桁の場合前に0を加える
    if(len(day[1])==1):
        day[1]="0"+day[1]
     #予約する日が１桁の場合前に0を加える
    if(len(day[2])==1):
        day[2]="0"+day[2]
    #予約する日程をクエリ文で読み込めるよう加工
    reserved_day="'"+day[0]+"-"+day[1]+"-"+day[2]+"'"

    #hospital_reserved_infoのテーブルに予約する情報を挿入するクエリ文
    insert_adding_new_reserved_day="""INSERT INTO hospital_reserved_info VALUES((SELECT MAX(ticket_id)+1 FROM hospital_reserved_info),1,101,"""+reserved_day+""","""+reserved_time +""",false);"""
    #クエリ文を実行
    cur.execute(insert_adding_new_reserved_day)
    connection.commit()
    return 0

#受付を完了させ、最近の受付予約の情報を更新する関数
def complete_reserved_day_to_list(consultation_number):
    connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")
    cur = connection.cursor()
    updatting_reserved_day="""UPDATE hospital_reserved_info SET reserved_check=true WHERE ticket_id="""+consultation_number+""";"""
    cur.execute(updatting_reserved_day)
    connection.commit()
    return 0

#fastapiでの通信プログラム

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class Adding_reserve_day(BaseModel):
    day:str
    time:str

#メイン画面の情報を反映させるため情報を送信
@app.get("/user/user_data")
def read_root():
    main_viewer_info=main_view_info(main_view_info_query,weekday,h2z_digit)
    return main_viewer_info

#予約をQRコードで読み取り完了させる
@app.put("/reserved_data_receive/{consultation_number}")
def reserved_data_receive(consultation_number:str):
    complete_reserved_day_to_list(consultation_number)
    return{"res":"受付が完了しました！"}

#予約可能な時間帯を表示させる
@app.get('/reserved_data/add_list/{hospital_id}')
async def reserved_add_list(hospital_id:str):
    reserved_viewer_adding_list=reserved_view_adding(reserved_view_adding_list_query,hospital_id)
    return reserved_viewer_adding_list


#予約する日程を受信し、データベースに追加する
@app.post('/reserved_data/inserting_day/')
def adding_new_reserve_day(inserting_day:Adding_reserve_day):
    adding_reserved_day_to_list(inserting_day)
    return{"res":"予約を追加しました！"}


#現在の予約状況を送信する
@app.get("/reserved_data/list/{user_id}")
async def read_reserved_info(user_id:str):
    reserved_viewer_info=reserved_view_info(reserved_view_info_query_first,reserved_view_info_query_second,user_id,h2z_digit)
    return reserved_viewer_info


