<template>
  <div id="app">
    <HeaderBar v-if="showHeader" :title="currentRouteName"/>
    <RouterView/>
  </div>
</template>

<script>
import HeaderBar from '@/components/HeaderBar.vue'

export default {
  computed: {
    showHeader() {
      return !this.$route.meta.hideHeader;
    },
    currentRouteName() {
      return this.$route.name;
    }
  },
  components: {
    HeaderBar
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
