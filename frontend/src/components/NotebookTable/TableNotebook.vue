<template>
    <el-table :data="tableData" row-key="id" class="tableContent">
        <el-table-column prop="name" label="Name">
        <template #default="{row}">
                <div style="display: flex; justify-content: space-between;">
                    <div v-if="!row.isEditing">
                        {{ row.name }}
                    </div>
                    <el-input v-else v-model="row.name" @blur="finishEdit(row)"/>
                    <el-button v-if="!row.isEditing" @click="editRow(row)">
                        <el-icon>
                            <Edit/>
                        </el-icon>
                    </el-button>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="date" label="Creation Date" sortable></el-table-column>
        <el-table-column prop="modifDate" label="Last Modification" sortable></el-table-column>
        <el-table-column fixed="right" label="Action">
            <template #default="{row}">
                <el-button type="primary" @click="handleOpen(row)">Open</el-button>
                <el-button type="danger" @click.prevent="deleteRow(row)">
                    <el-icon>
                        <Delete/>
                    </el-icon>
                </el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-button class="mt-4" style="width: 100%" @click="onAddItem">
        Add Note
    </el-button>
</template>

<script>
import { Edit, Delete } from '@element-plus/icons-vue';
import { ElTable, ElLoading, ElMessage } from 'element-plus';
import { getNotebook, getNotesFromNotebook, getUserId, deleteNote, createNote, addNoteToNotebook } from '@/api';

export default {
  components: {
    ElTable,
    Edit,
    Delete
  },
  props: {
    notebookId: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      userId: null,
      notebook: null,
      tableData: [
        { name: 'Alice', date: '2017-01-15', modifDate: '2022-07-20', isEditing: false },
        { name: 'Bob', date: '2015-09-23', modifDate: '2023-03-11', isEditing: false },
      ]
    };
  },
  async created() {
    this.userId = getUserId();
    this.tableData = await getNotesFromNotebook(this.notebookId);
  },
  methods: {
    async refreshTable() {
      this.tableData = await getNotesFromNotebook(this.notebookId);
    },
    async getNotebookInfo() {
      try {
        this.notebook = await getNotebook(this.notebookId);
      } catch (error) {
        console.error('Failed to fetch notebook:', error);
      }
    },
    async deleteRow(objectToDelete) {
        let loadingInstance = null;
        try {
            loadingInstance = ElLoading.service({
            lock: true,
            text: 'Adding New Notebook...',
            background: 'rgba(0, 0, 0, 0.7)'
            });

            await deleteNote(objectToDelete?.id);
            this.refreshTable();

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
    },
    editRow(row) {
      row.isEditing = true;
    },
    finishEdit(row) {
      row.isEditing = false;
    },
    handleOpen(row) {
      console.log('Opening row:', row);
    },
    async onAddItem() {
        let loadingInstance = null;
        try {
            loadingInstance = ElLoading.service({
            lock: true,
            text: 'Adding New Notebook...',
            background: 'rgba(0, 0, 0, 0.7)'
            });

            const res = await createNote('New Note', this.userId);
            await addNoteToNotebook(this.notebookId, res.note_id);
            this.refreshTable();

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
  mounted() {
    this.getNotebookInfo();
  }
}
</script>

<style>
.tableContent {
  height: 72vh;
}
</style>