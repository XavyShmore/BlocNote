import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Profile from '@/views/Profile.vue'
import Lists from '@/views/Lists.vue'
import Note from '@/views/Note.vue'
import Login from '@/views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/profile/:userId',
    name: 'profile',
    component: Profile
  },
  {
    path: '/lists/:listId',
    name: 'lists',
    component: Lists
  },
  {
    path: '/notes/:noteId',
    name: 'note',
    component: Note
  },
  {
    path: '/',
    name: 'login',
    component: Login
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

