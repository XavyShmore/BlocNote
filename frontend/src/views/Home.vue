<template>
  <div class="home">
    <PageTitle fontSize="4em" width="75%" class="titleHeader">
      <template v-slot:title>
        Home
      </template>
    </PageTitle>
  </div>
  <div class="content">
    <div class="recentlyEdited">
      <h2>Recently Edited</h2>
      <ul>
        <li><a href="/notes/id">Link 1</a></li>
        <li><a href="/notes/id">Link 2</a></li>
        <li><a href="/notes/id">Link 3</a></li>
        <li><a href="/notes/id">Link 4</a></li>
        <li><a href="/notes/id">Link 5</a></li>
        <li><a href="/notes/id">Voir plus +</a></li>
      </ul>
    </div>
    <div class="myLists">
      <h2>My Lists</h2>
      <ul>
        <li><a href="/notebook/id">Link 1</a></li>
        <li><a href="/notebook/id">Link 2</a></li>
        <li><a href="/notebook/id">Link 3</a></li>
        <li><a href="/notebook/id">Link 4</a></li>
        <li><a href="/notebook/id">Link 5</a></li>
        <li><a href="/notebook/id">Voir plus +</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/PageHeader/PageTitle.vue'

export default {
  components: {
    PageTitle
  }
}
</script>

<style>
.home {
  display: flex;
  justify-content: center;
}

.titleHeader {
  justify-content: center;
}

.content {
  display: flex;
  margin-top: 5%;
  font-size: 1.5em;
  justify-content: space-evenly;
}


</style>


