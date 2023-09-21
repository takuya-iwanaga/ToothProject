<template>
  <v-app-bar flat>
    <svg-icon type="mdi" :path="mdiMenu" width="40" height="40" class="ml-2"></svg-icon>
    <v-toolbar-title class="text-center ml-n7">{{message}}</v-toolbar-title>
  </v-app-bar>

    
    
  </template>
  
  <script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiMenu } from '@mdi/js';
    
    const message = 'すやま歯科医院'
    
  </script>