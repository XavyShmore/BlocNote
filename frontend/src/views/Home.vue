<template>
  <div class="home">
    <PageTitle fontSize="4em" width="75%" class="titleHeader">
      <template v-slot:title>
        {{ user?.name }}
      </template>
    </PageTitle>
  </div>
  <div class="homeContent">
    <div class="bioSection">
      <h2>Bio</h2>
      <el-input 
        v-model="bio"
        type="textarea"
        :rows="3"
        placeholder="Please input your bio"
        class="bioInput"
        @blur="updateBio"
      />
    </div>
    <div class="lists">
      <div class="listsRecent">
        <h2>Recently Edited</h2>
        <ul>
          <li v-for="note in recentNotes.slice(0, 6)" :key="note.id">
            <el-link class="linkText" @click="goToNote(note.id)">{{ note.title }}</el-link>
          </li>
        </ul>
      </div>
      <div class="listsRecent">
        <h2>My Lists</h2>
        <ul>
          <li v-for="list in myLists.slice(0, 5)" :key="list.id">
            <el-link class="linkText" @click="goToNotebook(list.id)">{{ list.title }}</el-link>
          </li>
          <li>
            <el-link type="primary" @click="goToLists()">Voir plus +</el-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/PageHeader/PageTitle.vue'
import { ElInput, ElLink } from 'element-plus'
import { getUserId, getUserProfile, setUserBio, getNotebooks, getRecentNotes } from '@/api'

export default {
  components: {
    PageTitle,
    ElInput,
    ElLink
  },
  data() {
    return {
      recentNotes: [],
      myLists: [],
      user: null,
      bio: '',
      userId: ''
    }
  },
  async created() {
    const userId = getUserId()
    this.userId = userId
    
    const user = await getUserProfile(userId)
    this.user = user
    this.bio = user?.bio

    this.myLists = await getNotebooks(userId)
    this.recentNotes = await getRecentNotes(userId)
    console.log(this.recentNotes)
  },
  methods: {
    goToNote(id) {
      this.$router.push(`/note/${id}`)
    },
    goToNotebook(id) {
      this.$router.push(`/notebook/${id}`)
    },
    goToLists() {
      this.$router.push('/lists')
    },
    async updateBio() {
      await setUserBio(this.userId, this.bio)
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

.lists {
  display: flex;
  margin-top: 5%;
  font-size: 1.5em;
  justify-content: space-evenly;
  width: 100%;
}

.bioSection {
  width: 75%;
  display: flex;
  flex-wrap: wrap;
}

.bioInput {
  width: 100%;
  height: 100%;
}

.listsRecent {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}

.listsRecent h2 {
  margin-bottom: 0;
}

.homeContent {
  height: 70vh;
  margin-top: 1%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.el-link__inner {
  font-size: 1.5em;
}

.el-textarea__inner {
  height: 100%;
}

</style>


