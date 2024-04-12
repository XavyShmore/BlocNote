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
        <li v-for="note in recentNotes.slice(0, 6)" :key="note.id">
          <a href="/notes/id">{{ note.title }}</a>
        </li>
      </ul>
    </div>
    <div class="myLists">
      <h2>My Lists</h2>
      <ul>
        <li v-for="list in myLists.slice(0, 5)" :key="list.id">
          <a href="/notebook/id">{{ list.title }}</a>
        </li>
        <li><a href="/lists">Voir plus +</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/PageHeader/PageTitle.vue'
import { getUserId, getUserProfile } from '@/api'

export default {
  components: {
    PageTitle
  },
  data() {
    return {
      recentNotes: [],
      myLists: []
    }
  },
  created() {
    const userId = getUserId()
    const user = getUserProfile(userId)
    console.log(user)
    this.recentNotes = [
      { id: 1, title: 'Note 1' },
      { id: 2, title: 'Note 2' },
    ]

    this.myLists = [
      { id: 1, title: 'List 1' },
      { id: 2, title: 'List 2' },
      { id: 3, title: 'List 3' },
      { id: 4, title: 'List 4' },
      { id: 5, title: 'List 5' },
      { id: 6, title: 'List 6' },
      { id: 7, title: 'List 7' },
      { id: 8, title: 'List 8' },
      { id: 9, title: 'List 9' },
      { id: 10, title: 'List 10' }
    ]
  },
  methods: {
    goToNote(id) {
      this.$router.push(`/notes/${id}`)
    },
    goToNotebook(id) {
      this.$router.push(`/notebook/${id}`)
    },
    goToLists() {
      this.$router.push('/lists')
    }
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


