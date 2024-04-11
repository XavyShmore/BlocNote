<template>
  <div>
    <PageTitle fontSize="4em">
      <template v-slot:title>
        Notebook
      </template>
    </PageTitle>
    <TableNotebook class="tableContent"/>
  </div>
</template>

<script>
import PageTitle from '@/components/PageHeader/PageTitle.vue'
import TableNotebook from '@/components/NotebookTable/TableNotebook.vue'

export default {
  components: {
    PageTitle,
    TableNotebook
  }
}

</script>

<style>

</style>