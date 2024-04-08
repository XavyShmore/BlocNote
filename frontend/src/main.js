import { createApp } from 'vue'
import { router } from './router/routes'
import App from './App.vue'
import PrimeVue from "primevue/config"
import axios from "axios"
import VueAxios from "vue-axios"
import "./App.css"

import 'primevue/resources/themes/aura-light-green/theme.css'

import Tooltip from 'primevue/tooltip'
import BadgeDirective from 'primevue/badgedirective'
import Ripple from 'primevue/ripple'
import StyleClass from 'primevue/styleclass'
import FocusTrap from 'primevue/focustrap'
import AnimateOnScroll from 'primevue/animateonscroll'
import Menubar from 'primevue/menubar'

const app = createApp(App);

app.use(VueAxios, axios);
app.use(router);

app.use(PrimeVue, {ripple: true});

app.directive('tooltip', Tooltip);
app.directive('badge', BadgeDirective);
app.directive('ripple', Ripple);
app.directive('styleclass', StyleClass);
app.directive('focustrap', FocusTrap);
app.directive('animateonscroll', AnimateOnScroll);

app.component('menubar', Menubar)

app.mount("#app")