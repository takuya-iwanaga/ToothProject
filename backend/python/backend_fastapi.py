#fastapiのモジュール
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

#postgreの接続のモジュール
import psycopg2
import traceback  # Just to show the full traceback
from psycopg2 import errors

#エラーの種類
InFailedSqlTransaction = errors.lookup('25P02')

UndefinedColumn=errors.lookup('42703')

connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")

#カーソル生成
cur = connection.cursor()

#メイン画面に表示される情報を取得する
main_view_info_query="""SELECT T1.user_name,T1.user_img,T3.ticket_id,T3.reserved_date ,T3.reserved_time,T4.hospital_name,T1.user_id FROM registrants_info as T1 INNER JOIN visiting_hospital_info as T2 ON T2.hospital_list_id=T1.hospital_list_id INNER JOIN hospital_reserved_info as T3 ON T3.user_id=T1.user_id INNER JOIN hospital_info as T4 ON T4.hospital_id=T2.hospital_id AND T4.hospital_id=T3.hospital_id where T3.reserved_date=(SELECT MIN(T22.reserved_date) FROM hospital_reserved_info as T22) AND T3.reserved_check=false"""
cur.execute(main_view_info_query)
main_view_info_result = cur.fetchall()
cur.close()


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
def main_view_info(main_view_info_result,weekday,h2z_digit):
    #曜日情報を取得
    key=main_view_info_result[0][3].weekday()
    days=weekday[str(key)]

    #日時を文字列に変換
    dt_d=main_view_info_result[0][3].strftime('%Y/%m/%d')
    dt_t=main_view_info_result[0][4].strftime('%H:%M')

    reserved_date=dt_d.translate(h2z_digit)+'（'+days+')'+'　'+dt_t.translate(h2z_digit)+'〜'

    #送信するデータを作成
    main_info_result={"user_name":main_view_info_result[0][0],"user_id":str(main_view_info_result[0][6]),"reserved_number":str(main_view_info_result[0][2]),"reserved_data":reserved_date,"hospital_name":main_view_info_result[0][5]}
    
    return main_info_result

#メイン画面に表示される情報を整理
main_viewer_info=main_view_info(main_view_info_result,weekday,h2z_digit)

#------------------------------------------------------------------------------


##予約情報の画面に表示される情報を整理する関数
def reserved_view_info(reserved_view_info_query_first,reserved_view_info_query_second,user_id,h2z_digit,connection):
    reserved_info_list_result=[]
    #予約情報のSQLの例外処理
    try:
        #user_idを元に予約情報を取得
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


#fastapiでの通信プログラム

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class User(BaseModel):
    user_name:str
    reserved_number:int
    reserved_data:str
    hospital_name:str

user_data={"user_name":"岩永　拓也",
"reserved_number":"4444",
"reserved_data":"２０２３/０９/２６（火） １３：３０〜",
"hospital_name":"すやま歯科医院"}


#メイン画面の情報を反映させるため情報を送信
@app.get("/user/user_data")
def read_root():
    return main_viewer_info

#予約をQRコードで読み取り完了させる
@app.post("/reserved_data_receive")
def reserved_data_receive(user:User):
    return{"res":"受付が完了しました！"}

#予約可能な時間帯を表示させる
@app.get('/reserved_data/add_list/{hospital_id}')
async def reserved_add_list(hospital_id:str):
    reserved_viewer_adding_list=reserved_view_adding(reserved_view_adding_list_query,hospital_id)
    print(reserved_viewer_adding_list)
    return reserved_viewer_adding_list

#現在のその病院の予約済みの時間の情報を送信する

#予約を追加する



#現在の予約状況を送信する
@app.get("/reserved_data/list/{user_id}")
async def read_reserved_info(user_id:str):
    reserved_viewer_info=reserved_view_info(reserved_view_info_query_first,reserved_view_info_query_second,user_id,h2z_digit,connection)
    return reserved_viewer_info



#病院の詳細情報を反映する

