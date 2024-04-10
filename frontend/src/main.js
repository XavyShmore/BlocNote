import { createApp } from 'vue'
import { router } from './router/routes'
import App from './App.vue'
import PrimeVue from "primevue/config"
import axios from "axios"
import VueAxios from "vue-axios"
import "./App.css"

import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

import Breadcrumb from 'primevue/breadcrumb'

import ElementPlus from 'element-plus';
import ElementTiptapPlugin from 'element-tiptap-vue3-fixed';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import 'element-tiptap-vue3-fixed/lib/style.css';
import 'element-plus/dist/index.css'

const app = createApp(App);

app.use(VueAxios, axios);
app.use(router);

app.use(PrimeVue, {ripple: true});
app.use(ElementPlus);
app.use(ElementTiptapPlugin)

app.component('Breadcrumb', Breadcrumb);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.mount("#app")