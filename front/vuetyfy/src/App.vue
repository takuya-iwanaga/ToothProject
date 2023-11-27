<template>
    <router-view></router-view> 
      
</template>

<script setup>
import{onMounted} from 'vue'
import axios from 'axios'
import {store}from './store/index.js'




//ユーザー情報の読み込み

const url='http://127.0.0.1:4050/user/user_data'

//apiの通信の処理
  function fastapi_connect(url){
    
    onMounted(()=>{
      axios
        .get(url)

        .then((response) => {store.commit('change_userinfo',response.data)})

        .catch((error) => console.log(error))
        
    })

  }
  const info=fastapi_connect(url);


//apiの通信の処理→予約できる日時を取得する関数(Reserved_adding.vueで使用)
     function fastapi_reserved_running_info(url){
    onMounted(()=>{
      axios
        .get(add_url)

        .then((response) => {store.commit('change_reserved_running_list_info',response.data)})

        .catch((error) => console.log(error))
    })

  }
  //病院のコード
  const hospital_id="101"
  //病院の営業時間、曜日をget通信するURL
  const add_url="http://127.0.0.1:4050/reserved_data/add_list/"+hospital_id

  //apiの通信の処理→予約できる日時を取得
  fastapi_reserved_running_info(add_url); 

  
</script>
