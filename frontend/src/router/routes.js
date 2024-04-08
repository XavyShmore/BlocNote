import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Profile from '@/views/Profile.vue'
import Lists from '@/views/Lists.vue'
import Notes from '@/views/Notes.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/profile/:id',
    name: 'profile',
    component: Profile
  },
  {
    path: '/lists/:id',
    name: 'lists',
    component: Lists
  },
  {
    path: '/notes/:id',
    name: 'notes',
    component: Notes
  },

]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

