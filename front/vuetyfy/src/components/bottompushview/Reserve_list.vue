<template>
    <Header title="ご予約"/>
    <v-container>
  <v-row>
    <svg-icon type="mdi" :path="mdiCalendarMonth" ></svg-icon>
    <div >ご予約状況</div>
  </v-row>
    
    <!--ご予約状況の確認-->
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <!--前回の予約の表示-->
    <v-table class="my-6" fixed-header height="300px" >
      <thead>
      <tr>
        <th class="text-left">
          予約年月日
        </th>
        <th class="text-left">
          予約した病院名
        </th>
      </tr>
    </thead>
      <tbody><tr class="my-6" v-for="reserved_list of store.state.reservedinfo" 
       v-if="!store.state.reservedinfo.res">
      <td class="text-left">{{ reserved_list.reserved_data }}</td>
      <td class="text-left">{{ reserved_list.hospital_name }}</td>
    </tr>
  </tbody>
</v-table>
       <v-row>
       <div v-for="res of store.state.reservedinfo.res" v-if="!store.state.reservedinfo.reserved_data" class="my-6">{{ res }}</div>
       </v-row>
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <!--定期検診-->

    <v-row>
        <div class="my-6">2024年04月定期検診 </div>
    </v-row>
    <v-row>
        <svg-icon type="mdi" :path="mdiFilePhone"></svg-icon>
        <div>ご予約の場合はお電話ください</div>
    </v-row>
    <v-row>
    <v-divider></v-divider>
    </v-row>
    <v-row>
        <div class="my-6">※ご不明な点などございましたらお電話にてお問い合わせください </div>
    </v-row>
    <!--新たに予約を作成するボタン-->
    <v-row justify="center">

    <router-link to='Add'>
        <v-btn color="blue">
            新たに予約を作成する
        </v-btn>
    </router-link>

    </v-row>

</v-container>
    </template>
    <script setup>
    import Header from '../Header.vue';
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiCalendarMonth } from '@mdi/js';
    import { mdiFilePhone } from '@mdi/js';



    import{onMounted} from 'vue'
    import axios from 'axios'
    import {store}from '../../store/index.js'


    //apiの通信の処理
  function fastapi_reservedinfo_connect(url){
    onMounted(()=>{
      axios
        .get(url)

        .then((response) => {store.commit('change_reservedinfo',response.data)})

        .catch((error) => console.log(error))
        
    })

  }

  const url="http://127.0.0.1:4050/reserved_data/list/"
  fastapi_reservedinfo_connect(url+store.state.userinfo.user_id)


    </script>