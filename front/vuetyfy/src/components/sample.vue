<template>

  <!--サイドバーの表示-->
  <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
      :width="300"
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class=""
        >
        <img src='@/assets/suyamasika.jpg'>

        <div class="text-center font-weight-bold text-caption" >{{ $store.state.userinfo.hospital_name}}</div>
        <v-list>
          <v-list-item prepend-icon="mdi-information" title="医療情報" value="home"></v-list-item>
          <v-list-item prepend-icon="mdi-phone" title="電話をかける" value="home"></v-list-item>
        </v-list>
       
          <v-divider></v-divider>
        
        <v-list>
          <v-list-item prepend-icon="mdi-file-document-outline" title="利用規約" value="home"></v-list-item>
          <v-list-item prepend-icon="mdi-shield" title="プライバシーポリシー" value="home"></v-list-item>
        
       </v-list>


        </v-list-item-group>
      </v-list>
      <template v-slot:append>
        <div class="pa-2">
          <v-divider></v-divider>
          <div class="text-center">{{ version }}</div>
          </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar flat>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title class="text-center ml-n7">{{$store.state.userinfo.hospital_name}}</v-toolbar-title>

  </v-app-bar>

    
  </template>
  
  <script setup>
  //アイコンの使用

    import { ref, watch } from 'vue'

    const version='Version 1.11.2'

    const drawer = ref(false)
  const group = ref(null)

  watch(group, () => {
    drawer.value = false
  })
  

    
    
  </script>