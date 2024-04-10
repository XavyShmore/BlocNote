<template>
    <el-form
      ref="loginFormRef"
      class="authFrame"
      :model="loginForm"
      :rules="rules"
      size="large"
      label-position="top"
      label-width="100px"
    >
      <el-form-item label="Email" prop="email">
        <el-input v-model="loginForm.email"/>
      </el-form-item>
  
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="loginForm.password"/>
      </el-form-item>
  
      <el-form-item>
        <el-button type="primary" @click="submitForm">Login</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script>
  import { reactive, ref } from 'vue';
  import { ElForm } from 'element-plus';
  
  export default {
    components: {
        ElForm
    },
    setup() {
      const loginFormRef = ref(null);
      const loginForm = reactive({
        email: '',
        password: '',
      });
  
      const rules = reactive({
        email: [
          { required: true, message: 'Please input your email address', trigger: 'blur' },
          { type: 'email', message: 'Please input a valid email address', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, message: 'Please input your password', trigger: 'blur' },
          { min: 8, message: 'Password length must be at least 8 characters', trigger: 'blur' }
        ],
      });

      const submitForm = () => {
      loginFormRef.value.validate((valid) => {
        if (valid) {
        //   TODO : implement login success behavior
        //   TODO : implement invalid credentials logic
        //   if (loginSuccess) {
        //   
        //   } 
        //   else {
        //      alert('The email or password is incorrect');
        //   }
        }

      });
    };

    const resetForm = () => {
      loginFormRef.value.resetFields();
    };
  
      return {
        loginFormRef,
        loginForm,
        rules,
        submitForm,
        resetForm,
      };
    },
  };
  </script>
  