<template>
    <Header title="マイページ"/>
    <div><font size="+2">fff</font>様のマイページ</div>
    <v-container>
    <v-row >
        <v-btn style="border: solid 3px green" class="ma-1 text-capitalize " height="80" width="280">
        <svg-icon size="50" type="mdi" :path="mdiHumanMaleFemaleChild" class="text-green "></svg-icon>
        <v-col>
            <div class="text-h6 text-left">
                ご家族登録をする
        </div>
        <div class="text-caption">
            ご家族の登録設定はこちらから
        </div>
        </v-col>
        <svg-icon type="mdi" :path="mdiChevronRight" class="text-green "></svg-icon>

    </v-btn>
    
</v-row>
<v-row  >
    
    <v-btn style="border: solid 3px green" class="ma-1 text-capitalize " height="80" width="280">
        <svg-icon size="50" type="mdi" :path="mdiFileDocumentOutline" class="text-green "></svg-icon>
        <v-col >
            <div class="text-h6 text-left">
            通院の履歴
        </div>
        <div class="text-caption">
            過去の通院に関する情報
        </div>
        </v-col>
        <svg-icon type="mdi" :path="mdiChevronRight" class="text-green ml-10"></svg-icon>

    </v-btn>
    
</v-row>
<v-row >
     
    <v-btn style="border: solid 3px green" class="ma-1 text-capitalize" height="80" width="280">
        <svg-icon size="50" type="mdi" :path="mdiToothbrushPaste" class="text-green"></svg-icon>
        <v-col>
            <div class="text-h6 text-left">
            当院からの提案
        </div>
        <div class="text-caption">
            おすすめのオーラルケア製品
        </div>
        </v-col>
        <svg-icon type="mdi" :path="mdiChevronRight" class="text-green ml-4"></svg-icon>
    </v-btn>   
</v-row>
    </v-container>
    </template>
    <script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiHumanMaleFemaleChild } from '@mdi/js';
    import { mdiFileDocumentOutline } from '@mdi/js';
    import { mdiToothbrushPaste } from '@mdi/js';
    import { mdiChevronRight } from '@mdi/js';

    import Header from '../Header.vue';
    
    </script>