<template>
  <v-app>
    
    <Sample/>
    
    <v-main>
      <Account/>
    <router-view/> 
    </v-main>
  </v-app>
  
</template>

<script setup>
import Sample from './components/sample.vue';
import Account from '@/components/Account.vue'

  
</script>
