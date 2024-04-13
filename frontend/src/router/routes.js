import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Lists from '@/views/Lists.vue'
import Notebook from '@/views/Notebook.vue'
import Note from '@/views/Note.vue'
import Login from '@/views/Login.vue'

const routes = [
  {
    path: '/',
    redirect: () => {
      return { name: 'home' };
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      isAuth: false,
      hideHeader: true
    }
  },
  {  
    path: '/home',
    name: 'home',
    component: Home,
    meta: {
      isAuth: true,
      hideHeader: false
    }
  },
  {
    path: '/lists',
    name: 'lists',
    component: Lists,
    meta: {
      isAuth: true,
      hideHeader: false
    }
  },
  {
    path: '/notebook/:id',
    name: 'notebook',
    component: Notebook,
    meta: {
      isAuth: true,
      hideHeader: false
    }
  },
  {
    path: '/note/:id',
    name: 'note',
    component: Note,
    meta: {
      isAuth: true,
      hideHeader: false
    }
  },
]

export const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.isAuth)) {
    const token = localStorage.getItem('token');
    if (!token) {
      next({ name: 'login' });
    } else {
      next();
    }
  } else {
    next();
  }
});




