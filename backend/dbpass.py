import psycopg2
import datetime
import mojimoji
connection = psycopg2.connect("host=127.0.0.1 port=5430 dbname=root user=root password=root")

cur = connection.cursor()

main_view_info_query="""SELECT T1.user_name,T1.user_img,T3.ticket_id,T3.reserved_date ,T3.reserved_time,T4.hospital_name FROM registrants_info as T1 INNER JOIN visiting_hospital_info as T2 ON T2.hospital_list_id=T1.hospital_list_id INNER JOIN hospital_reserved_info as T3 ON T3.user_id=T1.user_id INNER JOIN hospital_info as T4 ON T4.hospital_id=T2.hospital_id AND T4.hospital_id=T3.hospital_id where T3.reserved_date=(SELECT MIN(T22.reserved_date) FROM hospital_reserved_info as T22) AND T3.reserved_check=false"""
cur.execute(main_view_info_query)
main_view_info_result = cur.fetchall()

print(main_view_info_result)

#曜日の辞書を定義
keys = [ '0','1', '2','3', '4', '5','6']
values = ['月','火','水','木','金','土','日']
weekday = dict(zip(keys, values))

key=main_view_info_result[0][3].weekday()

#曜日を表示
print(weekday[str(key)])

#日時を文字列に変換
dt_d=main_view_info_result[0][3].strftime('%Y/%m/%d')

dt_t=main_view_info_result[0][4].strftime('%H:%M')


#数字を半角から全角に変換する
z_digit = '１２３４５６７８９０'
h_digit = '1234567890'

h2z_digit = str.maketrans(h_digit, z_digit)

#全角にした数字を出力
print(dt_d.translate(h2z_digit))