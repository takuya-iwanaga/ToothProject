<template>
<v-app>
    
    <Sample/>
    
    <v-main>
      <Account/>
    <Bottomselect v-bind:name="name"/>
    </v-main>
  </v-app>
</template>    
  
<script setup>
import Sample from "@/components/sample.vue";
import Account from "@/components/Account.vue";
import Bottomselect from "./Bottomselect.vue";

const name="岩永　拓也"

</script>