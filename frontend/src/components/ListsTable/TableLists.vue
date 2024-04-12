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
        <el-table-column prop="numNote" label="Number of Notes" sortable></el-table-column>
        <el-table-column fixed="right" label="Action">
            <template #default="{row}">
                <el-button type="primary" @click="handleOpen(row)">Open</el-button>
                <el-button type="danger" @click.prevent="deleteRow(row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-button class="mt-4" style="width: 100%" @click="onAddItem">
        Add Notebook
    </el-button>
</template>

<script>
import { reactive } from 'vue';
import { ElTable } from 'element-plus';
import { Edit } from '@element-plus/icons-vue';

    export default {
        components: {
            ElTable,
            Edit,
            
        },
        setup()  {
            const tableData = reactive([
            {
                name: 'Tom',
                date: '2016-05-03',
                numNote: 3
            },
            {
            name: 'Milo', date: '2018-10-10', numNote: 2, isEditing: false
            },
            {
            name: 'Alice', date: '2016-05-16', numNote: 9, isEditing: false
            },
            {
            name: 'Nora', date: '2018-10-15', numNote: 1, isEditing: false
            },
            {
            name: 'Charlie', date: '2017-11-07', numNote: 2, isEditing: false
            },
            {
            name: 'Hannah', date: '2018-08-16', numNote: 7, isEditing: false
            },
            {
            name: 'Riley', date: '2015-01-23', numNote: 3, isEditing: false
            },
            {
            name: 'Fiona', date: '2015-07-25', numNote: 7, isEditing: false
            },
            {
            name: 'Kevin', date: '2019-05-30', numNote: 8, isEditing: false
            },
            {
            name: 'Oscar', date: '2016-08-08', numNote: 10, isEditing: false
            },
            {
            name: 'Quinn', date: '2018-06-25', numNote: 1, isEditing: false
            },
            {
            name: 'Bob', date: '2019-11-16', numNote: 1, isEditing: false
            },
            {
            name: 'Luna', date: '2018-07-19', numNote: 7, isEditing: false
            },
            {
            name: 'Sam', date: '2017-06-25', numNote: 7, isEditing: false
            },
            {
            name: 'Julia', date: '2019-03-08', numNote: 5, isEditing: false
            }

            ])

            const deleteRow = (objectToDelete) => {
                const index = tableData.indexOf(objectToDelete);
                if (index !== -1) {
                    tableData.splice(index, 1);
                }
            };

            const handleOpen = (row) => {
                console.log(row)
            }

            const editRow = (row) => {
                row.isEditing = true;
            };

            const finishEdit = (row) => {
                row.isEditing = false;
            };

            const onAddItem = () => {
                const today = new Date();
                const formattedDate = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;

                tableData.push({
                    name: 'New Notebook',
                    date: formattedDate,
                    numNote: 0,
                    isEditing: false
                })
            }

            return { tableData, deleteRow, handleOpen, onAddItem, editRow, finishEdit }

        }
    }

</script>

<style>
.tableContent {
  height: 70vh;
}
</style>