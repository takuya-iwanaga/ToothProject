<template>

    <!--ヘッダーの表示の表示-->
    <v-row> 
        <v-col cols="1">
            <router-link to="/">
                <svg-icon size="40" type="mdi" :path=mdiChevronLeft></svg-icon>
            </router-link>
        </v-col >
        <v-col >
            <h3>{{ title }}</h3>
        </v-col>
    </v-row> 
    
    </template>
    
    <script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiChevronLeft } from '@mdi/js';

    defineProps(["title"])
    </script>