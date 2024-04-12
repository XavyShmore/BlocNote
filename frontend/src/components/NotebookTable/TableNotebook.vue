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
                <el-button type="danger" @click.prevent="deleteRow(row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-button class="mt-4" style="width: 100%" @click="onAddItem">
        Add Note
    </el-button>
</template>

<script>
import { reactive } from 'vue';
import { ElTable } from 'element-plus';

    export default {
        components: {
            ElTable
        },
        setup()  {
            const tableData = reactive([
                { name: 'Alice', date: '2017-01-15', modifDate: '2022-07-20', isEditing: false },
                { name: 'Bob', date: '2015-09-23', modifDate: '2023-03-11', isEditing: false },
                { name: 'Charlie', date: '2018-05-10', modifDate: '2023-01-05', isEditing: false },
                { name: 'Diana', date: '2016-11-30', modifDate: '2022-08-25', isEditing: false },
                { name: 'Eva', date: '2019-04-18', modifDate: '2023-02-19', isEditing: false },
                { name: 'Frank', date: '2015-12-07', modifDate: '2022-12-15', isEditing: false },
                { name: 'Grace', date: '2017-07-21', modifDate: '2022-06-30', isEditing: false },
                { name: 'Henry', date: '2016-03-13', modifDate: '2023-04-22', isEditing: false },
                { name: 'Ivy', date: '2018-08-29', modifDate: '2022-11-04', isEditing: false },
                { name: 'Jack', date: '2019-06-01', modifDate: '2023-05-17', isEditing: false },
                { name: 'Kathy', date: '2015-02-20', modifDate: '2022-09-10', isEditing: false },
                { name: 'Liam', date: '2017-12-15', modifDate: '2022-10-23', isEditing: false },
                { name: 'Mona', date: '2018-01-30', modifDate: '2022-05-29', isEditing: false },
                { name: 'Nolan', date: '2016-06-19', modifDate: '2023-08-21', isEditing: false },
                { name: 'Olivia', date: '2019-03-03', modifDate: '2022-07-07', isEditing: false },
                { name: 'Pete', date: '2015-08-08', modifDate: '2023-03-18', isEditing: false },
                { name: 'Quinn', date: '2017-10-17', modifDate: '2022-04-15', isEditing: false },
                { name: 'Rose', date: '2016-04-05', modifDate: '2023-01-20', isEditing: false },
                { name: 'Steve', date: '2018-09-25', modifDate: '2022-12-12', isEditing: false },
                { name: 'Tina', date: '2019-07-11', modifDate: '2023-06-02', isEditing: false }
            ])

            const editRow = (row) => {
                row.isEditing = true;
            };

            const finishEdit = (row) => {
                row.isEditing = false;
            };

            const deleteRow = (objectToDelete) => {
                const index = tableData.indexOf(objectToDelete);
                if (index !== -1) {
                    tableData.splice(index, 1);
                }
            };

            const handleOpen = (row) => {
                console.log(row)
            }

            const onAddItem = () => {
                const today = new Date();
                const formattedDate = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;

                tableData.push({
                    name: 'New Note',
                    date: formattedDate,
                    modifDate: formattedDate,
                    isEditing: false
                })
            }

            return { tableData, deleteRow, handleOpen, onAddItem, editRow, finishEdit }

        }
    }

</script>

<style>
.tableContent {
  height: 72vh;
}
</style>