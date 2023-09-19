<template>
  
    
    <v-app-bar flat>
      
        <svg-icon type="mdi" :path="mdiMenu"></svg-icon>
        <v-toolbar-title class="text-center">{{message}}</v-toolbar-title>
      
    </v-app-bar>
    
    
  </template>
  
  <script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiMenu } from '@mdi/js';
    
    const message = 'すやま歯科医院'
    
  </script>