<template>
  <Menubar :model="items"></Menubar>
  <div id="app">
    <div style="display: flex; justify-content: center;">
    <nav>
      <router-link to="/">Home</router-link>
    </nav>
    <nav>
      <router-link to="/profile/73647">Profile</router-link>
    </nav>
    <nav>
      <router-link to="/lists/99273">Lists</router-link>
    </nav>
    <nav>
      <router-link to="/notes/73927">Notes</router-link>
    </nav>
  </div>
    <router-view/>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import MenuBar from 'primevue/menubar';

export default defineComponent({
  components: {
    MenuBar 
  },
  data() {
    return {
      items: [
        {
          label: 'File',
          items: [
            {label: 'New', icon: 'pi pi-fw pi-plus'},
            {label: 'Open', icon: 'pi pi-fw pi-download'}
          ]
        },
        {
          label: 'Edit',
          items: [
            {label: 'Undo', icon: 'pi pi-fw pi-undo'},
            {label: 'Redo', icon: 'pi pi-fw pi-redo'}
          ]
        }
        // Add more items as needed
      ]
    };
  }
});

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
