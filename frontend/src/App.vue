<template>
  <div id="app">
    <!-- <div style="display: flex; justify-content: center;">
      <nav>
        <router-link to="/"> Home </router-link>
      </nav>
      <nav>
        <router-link to="/profile/:id"> Profile </router-link>
      </nav>
      <nav>
        <router-link to="/lists/:id"> Lists </router-link>
      </nav>
      <nav>
        <router-link to="/notes/:id"> Notes </router-link>
      </nav>
    </div> -->
    <HeroPage/>
  </div>
</template>

<script>
import HeroPage from '@/components/HeroPage.vue'

export default {
  components: {
    HeroPage
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
