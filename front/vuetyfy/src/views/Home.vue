<template>
<v-app>
    
    <Sample/>
    
    <v-main>
      <Account/>
    <Bottomselect/>
    </v-main>
    
  </v-app>
</template>    
  
<script setup>
import Sample from "@/components/Sample.vue";
import Account from "@/components/Account.vue";
import Bottomselect from "./Bottomselect.vue";

import{onMounted} from 'vue'
import axios from 'axios'
import {store}from '../store/index.js'


let user_name="岩永"

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


</script>
