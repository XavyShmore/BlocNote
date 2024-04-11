<template>
    <el-table :data="tableData" row-key="id" class="tableContent">
        <el-table-column prop="name" label="Name"></el-table-column>
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
            {
                name: 'Tom',
                date: '2016-05-03',
                numNote: 3
            },
            {
            name: 'Milo', date: '2018-10-10', numNote: 2
            },
            {
            name: 'Alice', date: '2016-05-16', numNote: 9
            },
            {
            name: 'Nora', date: '2018-10-15', numNote: 1
            },
            {
            name: 'Charlie', date: '2017-11-07', numNote: 2
            },
            {
            name: 'Hannah', date: '2018-08-16', numNote: 7
            },
            {
            name: 'Riley', date: '2015-01-23', numNote: 3
            },
            {
            name: 'Fiona', date: '2015-07-25', numNote: 7
            },
            {
            name: 'Kevin', date: '2019-05-30', numNote: 8
            },
            {
            name: 'Oscar', date: '2016-08-08', numNote: 10
            },
            {
            name: 'Quinn', date: '2018-06-25', numNote: 1
            },
            {
            name: 'Bob', date: '2019-11-16', numNote: 1
            },
            {
            name: 'Luna', date: '2018-07-19', numNote: 7
            },
            {
            name: 'Sam', date: '2017-06-25', numNote: 7
            },
            {
            name: 'Julia', date: '2019-03-08', numNote: 5
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

            const onAddItem = () => {
                tableData.push({
                    name: 'New Item',
                    date: '2021-06-01',
                    numNote: 0
                })
            }

            return { tableData, deleteRow, handleOpen, onAddItem }

        }
    }

</script>

<style>
.tableContent {
  height: 72vh;
}
</style>