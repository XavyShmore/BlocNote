<template>
    <el-table>
        <el-table-column prop="name" label="Name"></el-table-column>
        <el-table-column prop="date" label="Creation Date"></el-table-column>
    </el-table>
</template>

<script>
import { ElTable } from 'element-plus';

    export default {
        components: {
            ElTable
        },
        setup()  {
    
        }
    }

</script>

<style>

</style>