<template>
    <el-form :model="form">
        <el-form-item label="Username">
            
        </el-form-item>
        <el-form-item label="Password">
            
        </el-form-item>
    </el-form>
</template>

<script>
import { reactive } from 'vue';
import { ElForm } from 'element-plus';

export default{
    components: {
        ElForm
    },
    setup() {
        const form = reactive({
            username: '',
            password: '',
        })

        const onSubmit = () => {
            console.log('Form submited!')
        }

        return { form, onSubmit };
    }
}

</script>

<style>
</style>