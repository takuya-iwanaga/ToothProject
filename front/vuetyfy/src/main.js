/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

import { store } from './store'

import QrReader from 'vue3-qr-reader';





const app = createApp(App)

registerPlugins(app)

app.use(store)

app.use(QrReader);


app.mount('#app')
