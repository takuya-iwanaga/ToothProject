<template>
    <Header title="ご予約"/>
    <v-container >
        <v-row justify="center">
             <div class="my">本日の年月日：{{ today }}</div>
       </v-row>
       <v-row justify="center">
             <div class="my-3">予約する病院：{{ store.state.userinfo.hospital_name }}</div>
       </v-row>
  <v-row justify="center">
    <div>予約する月日を選択してください</div>
  </v-row>
    
    <!--ご予約状況の確認-->
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <keep-alive>
    <v-row justify="center">
        <v-col cols="8">
        <div class="my-6"> 
            <v-select
            label="予約する年日時"
            :items="reserve_possible_date_list"
            v-model='store.state.reserving_check_date_info'
            ></v-select>
        </div>
        </v-col>
    </v-row>
    </keep-alive>
    <!--前回の予約の表示-->
     <v-row>
     </v-row>
    <!--定期検診-->

    <v-row justify="center">
        <div class="my-3">予約時間 </div>
    </v-row>
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <v-row justify="center">
        <v-col cols="6" class="d-flex align-center">
            <v-virtual-scroll :items="[1]" :item-height="50" height="150" >
                <v-radio-group v-model='store.state.reserving_check_time_info'>
                <v-radio v-for="i in reserving_time_list_making(store.state.reserving_check_date_info)" :label="i" :value="i">
                </v-radio>
                </v-radio-group>
            </v-virtual-scroll>
        </v-col>
                
        </v-row>
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <v-row>
        <div class="my-6">※ご不明な点などございましたらお電話にてお問い合わせください </div>
    </v-row>
    <!--新たに予約を作成するボタン-->
    <v-row justify="center">
        <router-link to="Checking">
        <v-btn color="blue">
            予約する内容の確認
        </v-btn>
        </router-link>
    </v-row>
</v-container>
<div>{{ date }}</div>
    </template>
    
    <script setup>
    
    import Header from '../Header.vue';
    import {store}from '../../store/index.js'
    import * as holiday_jp from '@holiday-jp/holiday_jp';


    //本日の年月日を取得
    var today_date=new Date()
    //本日の年を取得
    var today_year=today_date.getFullYear();
    //本日の月を取得
    var today_month=today_date.getMonth()+1;
    //本日の曜日を取得
    var today_day=today_date.getDate();
    //本日の日を取得
    var today_week=today_date.getDay();

    //曜日の配列の作成
    var week=new Array("日","月","火","水","木","金","土");
    
    //本日の年月日の表示文字列作成
    var today=today_year+"年"+today_month+"月"+today_day+"日 "+week[today_week]+"曜日"

    //予約できる年月日の配列の初期化
    const reserve_possible_date_list=[];

    var reserve_possible_date=new Date()
  //営業していない曜日の配列
  const no_running_day=[]
  //営業していない曜日の配列の要素を挿入
  store.state.reserved_running_list_info.forEach((runnninng_info) => {
    if(runnninng_info.open_time===null){
        no_running_day.push(runnninng_info.running_day)
    }
  })

    //予約できる年月日の配列にデータを追加
    for (let i = 0; i < 14; i++){
        //日付を翌日にする
        reserve_possible_date.setDate(reserve_possible_date.getDate()+1)

        //本日の曜日を取得
        var reserve_possible_date_week=reserve_possible_date.getDay();
        if (no_running_day.includes((reserve_possible_date_week+6)%7)){
            
        }else{
        
            //祝日の判定値
            var holiday_check= holiday_jp.isHoliday(reserve_possible_date)
            //祝日かどうかのチェック
            if(holiday_check===false){
                //本日の年を取得
                var reserve_possible_date_year=reserve_possible_date.getFullYear();
                //本日の月を取得
                var reserve_possible_date_month=reserve_possible_date.getMonth()+1;
                //本日の日を取得
                var reserve_possible_date_day=reserve_possible_date.getDate();
                //表示する形式に形成
                var reserve_date=reserve_possible_date_year+"年"+reserve_possible_date_month+"月"+reserve_possible_date_day+"日 "+week[reserve_possible_date_week]+"曜日"
                //予約可能なリストに追加する
                reserve_possible_date_list.push(reserve_date)
           }
        }
        
    }
    //---------------------------------------
    const day_number_list={'月曜日':0,'火曜日':1,'水曜日':2,'木曜日':3,'金曜日':4,'土曜日':5,'日曜日':6}
    //曜日に合わせた予約可能な時間帯を表示
    function reserving_time_list_making(reserve_day){
        console.log(reserve_day)
        if(reserve_day.value!==''){
            //予約可能な時間の配列を作成する
            const reserve_possible_time_list=[]
            //1週間の曜日ごとに予約可能な時間帯のリストを作成
            for(const [key, value] of Object.entries(day_number_list)){
                if(reserve_day.indexOf(`${key}`)!== -1){        
                    for(let i=0;i<store.state.reserved_running_list_info.length;i++){
                        if(store.state.reserved_running_list_info[i].running_day===Number(`${value}`)){             
                            let open_time=store.state.reserved_running_list_info[i].open_time
                            let close_time=store.state.reserved_running_list_info[i].close_time            
                            time_list_making(open_time,close_time,30,reserve_possible_time_list)
                        }
                    }
                }
            }
        return reserve_possible_time_list
        }
        return 0
    }

    //----------------------------------------
   

    //営業時間の予約可能リストの長さを算出し、予約可能な時間のリストを作る関数
    function time_list_making(open_time,close_time,interval,reserve_possible_time_list){
        const [open_hours,open_minutes]=open_time.split(':');
        const [close_hours,close_minutes]=close_time.split(':');
        const running_time_minutes=(Number(close_hours)-Number(open_hours)) * 60  + Number(close_minutes) - Number(open_minutes);
        const time_list_count=running_time_minutes/interval;

        for(let i=0;i<time_list_count;i++){
            const reserve_hours=Math.floor((Number(open_hours)*60+Number(open_minutes)+30*i)/60);


            const reserve_mimutes=(Number(open_hours)*60+Number(open_minutes)+30*i)%60;

            var reserve_time=''
            if(reserve_mimutes===0){
                const reserve_mimutes_string='00';
                reserve_time=reserve_hours.toString()+':'+reserve_mimutes_string+'~';
            }else{
                reserve_time=reserve_hours.toString()+':'+reserve_mimutes.toString()+'~';
            }
            reserve_possible_time_list.push(reserve_time);
        }
        return reserve_possible_time_list;
    }

    //-------------------------------------------

  </script>