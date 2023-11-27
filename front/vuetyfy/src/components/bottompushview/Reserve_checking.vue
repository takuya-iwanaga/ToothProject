<template>
<Header title="ご予約"/>
    <v-container >
        <v-row justify="center">
             <div class="my-3">予約内容確認</div>
       </v-row>
        <v-row justify="center">
             <div class="my-6">本日の年月日：{{ today }}</div>
       </v-row>
       <v-row>
    <v-divider></v-divider>
    </v-row>
       <v-row justify="center">
             <div class="my-3">予約する病院：{{ store.state.userinfo.hospital_name }}</div>
       </v-row>
      
  
    <!--ご予約状況の確認-->
    <div v-if="store.state.reserving_check_date_info!=='' && store.state.reserving_check_time_info!==''">
        <v-row justify="center">
        <div class="my-3">予約する月日：{{ store.state.reserving_check_date_info }}</div>
        </v-row>
        <v-row justify="center">
        <div class="my-3">予約時間： {{ store.state.reserving_check_time_info }}</div>
        </v-row>
    </div>
    <div v-if="store.state.reserving_check_date_info==='' || store.state.reserving_check_time_info===''">
        <v-row justify="center">
        <div class="my-3">正しく予約情報が入力されていません。「予約内容を変更する」ボタンを押して予約情報を入力してください。</div>
        </v-row>
    </div>
    
    
   
    
    <!--新たに予約を作成するボタン-->
    <v-row justify="center">

        <router-link to="Add">
        <v-btn color="blue">
            予約内容を変更する
        </v-btn>
        </router-link>

        <router-link to="Reserve">
        <v-btn color="blue" @click="fastapi_reserved_add('http://127.0.0.1:4050/reserved_data/add/')">
            予約を確定する
        </v-btn>
        </router-link>       
    </v-row>

</v-container>
</template>
<script setup>
import Header from '../Header.vue';

    import{onMounted} from 'vue'
    import axios from 'axios'
    import {store}from '../../store/index.js'

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

    //入力した予約日時の内容をデータベースに追加する
    function fastapi_reserved_add(url){
        onMounted(()=>{
            axios
            .post(url,{reserved_adding_date:store.state.reserving_check_date_info,reserved_adding_time:store.state.reserving_check_time_info})

            .then((response) => {alert(response+'予約を受け付けました！！')})

            .catch((error) => console.log(error))
        
        })

    }



</script>