import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Lists from '@/views/Lists.vue'
import Notebook from '@/views/Notebook.vue'
import Note from '@/views/Note.vue'
import Login from '@/views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {  
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/lists',
    name: 'lists',
    component: Lists
  },
  {
    path: '/notebook/:',
    name: 'notebook',
    component: Notebook
  },
  {
    path: '/notes/:noteId',
    name: 'note',
    component: Note
  },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

