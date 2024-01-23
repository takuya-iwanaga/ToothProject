<template>
  <Header title="QRコード受診"/>
    <div>
    <div class="center stream">
      <qr-stream @decode="onDecode" class="mb">
        <div style="color: red" class="frame"></div>
      </qr-stream>
    </div>
    <div class="result">{{ qrcode_accompletting(qrcodeinfo) }}</div>
  </div>
    </template>


    <script setup>
    import Header from '../Header.vue';
    import {ref} from 'vue';

    import { QrStream } from 'vue3-qr-reader';
    import axios from 'axios';
    import {store}from '../../store/index.js'

    const components={
        QrStream
    }

    const qrcodeinfo=ref([])
    const message=ref([])

    function onDecode(data) {
      qrcodeinfo.value=data     
    }

    function qrcode_accompletting(url){
      if(qrcodeinfo.value!==""){
        
        let consultation_number=store.state.userinfo.reserved_number
      axios.put(url+'/'+consultation_number)
      .then((response) => {message.value=response.data.res})
      .catch((error) => console.log(error.response.data))

      return message.value
      }
      
    }

    </script>

<style scoped>
.stream {
  max-height: 500px;
  max-width: 500px;
  margin: auto;
}
.frame {
  border-style: solid;
  border-width: 2px;
  border-color: red;
  height: 200px;
  width: 200px;
  position: absolute;
  top: 0px;
  bottom: 0px;
  right: 0px;
  left: 0px;
  margin: auto;
}
</style>