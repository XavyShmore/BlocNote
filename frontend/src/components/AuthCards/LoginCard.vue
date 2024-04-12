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
  import { useRouter } from 'vue-router';
  import { ElForm, ElMessage } from 'element-plus';
  import { login } from '@/api.js';
  
  export default {
    components: {
        ElForm,
        ElMessage
    },
    setup() {
      const router = useRouter();
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

      const errorMessage = () => {
        ElMessage({
          message: 'Login failed',
          type: 'error'
        });
      };

      const attemptLogin = async () => {
        const response = await login(loginForm.email, loginForm.password);
        if (response?.success === true) {
          router.push({ name: 'home' });
        } else {
          errorMessage();
        }
      };

      const submitForm = () => {
      loginFormRef.value.validate((valid) => {
        if (valid) {
          attemptLogin();
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
  