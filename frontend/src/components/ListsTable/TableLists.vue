<template>
    <el-table :data="this.tableData" row-key="id" class="tableContent">
        <el-table-column prop="title" label="Title">
            <template #default="{row}">
                <div style="display: flex; justify-content: space-between;">
                    <div v-if="!row.isEditing">
                        {{ row.title }}
                    </div>
                    <el-input v-else v-model="row.title" @blur="finishEdit(row)"/>
                    <el-button v-if="!row.isEditing" @click="editRow(row)">
                        <el-icon>
                            <Edit/>
                        </el-icon>
                    </el-button>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="creation" label="Creation Date" sortable></el-table-column>
        <el-table-column prop="number_of_notes" label="Number of Notes" sortable></el-table-column>
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
        Add Notebook
    </el-button>
</template>

<script>
import { reactive } from 'vue';
import { ElTable, ElLoading, ElMessage } from 'element-plus';
import { Edit, Delete } from '@element-plus/icons-vue';
import { getUserId, getNotebooks, createNotebook, deleteNotebook, renameNotebook } from '@/api.js';

    export default {
        components: {
            ElTable,
            Edit,
            Delete,
            ElMessage
        },
        data() {
            return {
                userId: null,
                tableData: reactive([]),
            }
        },
        methods: {
            async refreshTable() {
                this.tableData = await getNotebooks(this.userId);
            },
            async deleteRow(objectToDelete) {
                let loadingInstance = null;
                try {
                    loadingInstance = ElLoading.service({
                    lock: true,
                    text: 'Deleting Notebook...',
                    background: 'rgba(0, 0, 0, 0.7)'
                    });

                    await deleteNotebook(objectToDelete?.id);
                    this.refreshTable();

                } catch (error) {
                    ElMessage({
                        message: 'Failed to delete or fetch notebooks',
                        type: 'error'
                    });
                    console.error('Failed to delete or fetch notebooks:', error);
                } finally {
                    if (loadingInstance) {
                        loadingInstance.close();
                    }
                }
            },

            handleOpen(row) {
                this.$router.push({ name: 'notebook', params: { id: row.id } });
            },

            editRow(row) {
                row.isEditing = true;
            },

            async finishEdit(row) {
                row.isEditing = false;
                let loadingInstance = null;
                try {
                    loadingInstance = ElLoading.service({
                    lock: true,
                    text: 'Changing Notebook Name...',
                    background: 'rgba(0, 0, 0, 0.7)'
                    });

                    await renameNotebook(row.id, row.title);
                    this.refreshTable();

                } catch (error) {
                    ElMessage({
                        message: 'Failed to change or fetch notebooks names',
                        type: 'error'
                    });
                    console.error('Failed to change or fetch notebooks names:', error);
                } finally {
                    if (loadingInstance) {
                        loadingInstance.close();
                    }
                }
            },

            async onAddItem() {
                let loadingInstance = null;
                try {
                    loadingInstance = ElLoading.service({
                    lock: true,
                    text: 'Adding New Notebook...',
                    background: 'rgba(0, 0, 0, 0.7)'
                    });

                    await createNotebook('New Notebook', this.userId);
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
        async created() {
            let loadingInstance = null;
            try {
                loadingInstance = ElLoading.service({
                lock: true,
                text: 'Adding New Notebooks...',
                background: 'rgba(0, 0, 0, 0.7)'
                });

                this.userId = getUserId();
                this.tableData = await getNotebooks(this.userId)

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
    }

</script>

<style>
.tableContent {
  height: 70vh;
}
</style>