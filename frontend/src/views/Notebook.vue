<template>
  <div>
    <PageTitle fontSize="4em">
      <template v-slot:title>
        {{ notebook?.title }}
      </template>
    </PageTitle>
    <TableNotebook :notebookId="id" class="tableContent"/>
  </div>
</template>

<script>
import PageTitle from '@/components/PageHeader/PageTitle.vue'
import TableNotebook from '@/components/NotebookTable/TableNotebook.vue'
import { ElLoading, ElMessage } from 'element-plus';
import { getNotebook } from '@/api';

export default {
  components: {
    PageTitle,
    TableNotebook
  },
  computed: {
    id() {
      return this.$route.params.id;
    }
  },
  data() {
    return {
      notebook: null
    }
  },
  methods: {
    async getNotebookInfo() {
        let loadingInstance = null;
        try {
            loadingInstance = ElLoading.service({
            lock: true,
            text: 'Adding New Notebook...',
            background: 'rgba(0, 0, 0, 0.7)'
            });

            this.notebook = await getNotebook(this.id);

        } catch (error) {
            ElMessage({
                message: 'Failed to add or fetch notebooks',
                type: 'error'
            });
            console.error('Failed to add or fetch notebooks:', error);
        } finally {
            if (loadingInstance) {
                loadingInstance.close();
            }
        }
    }
  },
  created() {
    this.getNotebookInfo();
  },
}

</script>

<style>

</style>