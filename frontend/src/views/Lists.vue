<template>
    <div class="Lists">
      <PageTitle fontSize="4em">
        <template v-slot:title>
          Lists
        </template>
      </PageTitle>
      <TableLists/>
    </div>
</template>

<script>
import TableLists from '@/components/ListsTable/TableLists.vue'
import PageTitle from '@/components/PageHeader/PageTitle.vue';

export default {
  components: {
    TableLists,
    PageTitle
  }
}

</script>

<style>

</style>