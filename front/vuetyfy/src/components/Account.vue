
<template>

<!--アカウントの写真と名前、診察券番号の表示-->
<v-row> 
    <v-col cols="2">  
    <v-avatar color="indigo" size="48" class="ml-2">
      <v-icon dark>
        mdi-account-circle
      </v-icon>
    </v-avatar>
    </v-col>
    <v-col >
    <v-list-item-title>
        <font size="+2">{{ name }}</font><font size="-1">様</font>
    </v-list-item-title>
    <v-list-item-subtitle >
        <h4>診察券番号:{{ number }}</h4>
    </v-list-item-subtitle>

    </v-col>
</v-row> 

<!--予約の日付と時間の表示-->
<div class="ml-2"><font size="-1">次回の予約</font></div>
<div class="ml-2">{{ data }}</div>
</template>

<script setup>
const name="岩永　拓也";
const number="　22222"
const data="２０２３/０９/２６（火） １３：３０〜"

</script>