<template>

  <!--サイドバーの表示-->
  <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class=""
        >
        <img src='@/assets/suyamasika.jpg'
        >

        <div>
        <svg-icon type="mdi" :path="mdiInformation"></svg-icon>
        医院情報
        </div>
        <div>
        <svg-icon type="mdi" :path="mdiPhone"></svg-icon>
        電話をかける
        </div>
        <div>
        <svg-icon type="mdi" :path="mdiFileDocumentOutline"></svg-icon>
        利用規約
        </div>
        <div>
        <svg-icon type="mdi" :path="mdiShield"></svg-icon>
        プライバシーポリシー
        </div>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar flat>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title class="text-center ml-n7">{{message}}</v-toolbar-title>

  </v-app-bar>

    
  </template>
  
  <script setup>
  //アイコンの使用
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiInformation } from '@mdi/js';
    import { mdiPhone } from '@mdi/js';
    import { mdiFileDocumentOutline } from '@mdi/js';
    import { mdiShield } from '@mdi/js';

    import { ref, watch } from 'vue'

    const message = 'すやま歯科医院'

    const drawer = ref(false)
  const group = ref(null)

  watch(group, () => {
    drawer.value = false
  })
  

    
    
  </script>