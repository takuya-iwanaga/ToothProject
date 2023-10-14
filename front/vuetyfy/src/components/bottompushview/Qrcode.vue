<template>
    <div>
    <div class="mb">Qr Stream</div>
    <div class="center stream">
      <qr-stream @decode="onDecode" class="mb">
        <div style="color: red" class="frame"></div>
      </qr-stream>
    </div>
    <div class="result">Result: {{ qrcodeinfo }}</div>
  </div>
    </template>


    <script setup>
    import {ref} from 'vue';
    import { QrStream } from 'vue3-qr-reader';

    import axios from 'axios';

    const components={
        QrStream
    }

    const qrcodeinfo=ref([])

    function onDecode(data) {
      qrcodeinfo.value=data;

      
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