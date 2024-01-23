# ToothProject
歯科医院の診察アプリ

### 使用技術
- python 3.8.5
- vue@3.3.4
- PostgreSQL(16.1)
- FastAPI

### 使用した画像
- https://job-medley.com/facility/149069/

### PostgreSQLの設定
1. PostgreSQLはdockerで動かしているため、下記の記事を参考にDBを設定する。
- https://book.st-hakky.com/hakky/try-postgres-on-docker/

2. 使用するデータベースはrootとしてToothProject/backendのパスにあるSQL.txtを参考にテーブル作成及びデータを挿入する。

### アプリの主な操作
- 予約の仕方
1. メイン画面の青いボタン「ご予約」を押す。
2. 下にある「新たに予約を作成する」を押す。
3. 「予約する年月日」、「予約時間」で予約する日程を選択する。
4. 予約を確定する場合は「予約を確定する」ボタンを押す。予約する日程を変更したい場合は「予約内容を変更する」ボタンを押す。

- 受診日程の受付の仕方
1. メイン画面の赤いボタン「QRコード」を押す。
2. 使用している端末のカメラにQRコードをかざす。
3. カメラの写っている画面の下に「受付が完了しました！」のメッセージが表示する。
4. メッセージの表示が確認できたら受付は完了です。

### 受付で使用するQRコード
![受付のQRコード](IMG_1833.png)
