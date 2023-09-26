<template>
    
    <v-container>
  <!-- QRコードとご予約のボタンの配置-->
  <v-row justify="center">
    <v-btn style="border: solid 3px red" height="118" width="156" class="ma-1 text-capitalize text-red" >
        <v-col>
        <svg-icon color="red" height="60" width="60" type="mdi" :path=mdiQrcode></svg-icon>
        <div>QRコード</div>
        </v-col>
    </v-btn>

    <v-btn style="border: solid 3px blue" height="118" width="156" class="ma-1 text-capitalize text-blue">
        <v-col>
        <svg-icon color="blue" height="60" width="60" type="mdi" :path=mdiCalendarToday></svg-icon>
        <div>ご予約</div>
        </v-col>
    </v-btn>
  </v-row>
  <!-- マイページとお知らせのボタンの配置-->
  <v-row justify="center">
    <v-btn style="border: solid 3px green" height="118" width="156" class="ma-1 text-capitalize text-green" >
        <v-col>
        <svg-icon color="green" height="60" width="60" type="mdi" :path=mdiAccountMultiple></svg-icon>
        <div>マイページ</div>
        </v-col>
    </v-btn>

    <v-btn style="border: solid 3px yellow" height="118" width="156" class="ma-1 text-capitalize text-yellow">
        <v-col>
        <svg-icon color="yellow" height="60" width="60" type="mdi" :path=mdiBell></svg-icon>
        <div>お知らせ</div>
        </v-col>
    </v-btn>
  </v-row>
  <!-- カメラとMedical Boxのボタンの配置-->
  <v-row justify="center">

  <!-- カメラボタンの配置-->
    <div>
    <v-btn style="border: solid 3px gray" height="118" width="156" class="ma-1 text-capitalize text-grey" 
    @click="aaa()">
        <v-col>
        <svg-icon color="grey" height="60" width="60" type="mdi" :path=mdiCamera></svg-icon>
        <div>カメラ</div>
        </v-col>
    </v-btn>

    <v-dialog
    v-model="modal"
    width="auto"
  >
    <v-card>
      <v-card-text>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" block @click="modal = false">Close Dialog</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  </div>



  <!--Medical Boxボタンの配置-->
  <router-link to="/Medical">
    <v-btn style="border: solid 3px lightblue" height="118" width="156" class="ma-1 text-capitalize text-blue-lighten-3"
    >
        <v-col>
        <svg-icon color="lightblue" height="60" width="60" type="mdi" :path=mdiImageMultiple></svg-icon>
        <div>Medical Box</div>
        </v-col>
    </v-btn>
  </router-link>
  </v-row>
  </v-container>


</template>    

<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiQrcode } from '@mdi/js';
import { mdiCalendarToday} from '@mdi/js';
import { mdiAccountMultiple } from '@mdi/js';
import { mdiBell } from '@mdi/js';
import { mdiCamera } from '@mdi/js';
import { mdiImageMultiple } from '@mdi/js';
import {ref } from 'vue';


const modal=ref(false);


function aaa(){
  this.modal=true;
};




</script>