<template>

  <v-app-bar flat>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title class="text-center ml-n7">{{message}}</v-toolbar-title>

  </v-app-bar>

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
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    
  </template>
  
  <script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiMenu } from '@mdi/js';
    import { ref, watch } from 'vue'

    const message = 'すやま歯科医院'

    const drawer = ref(false)
  const group = ref(null)

  watch(group, () => {
    drawer.value = false
  })
  

    
    
  </script>