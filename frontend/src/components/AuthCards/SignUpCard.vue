<template>
    <el-form
      ref="signupFormRef"
      class="authFrame"
      :model="signupForm"
      :rules="rules"
      size="large"
      label-position="top"
      label-width="100px"
    >
      <el-form-item label="Name" prop="name">
        <el-input v-model="signupForm.name" />
      </el-form-item>
  
      <el-form-item label="Email" prop="email">
        <el-input v-model="signupForm.email" />
      </el-form-item>
  
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="signupForm.password" />
      </el-form-item>
  
      <el-form-item label="Confirm Password" prop="confirmPassword">
        <el-input type="password" v-model="signupForm.confirmPassword" />
      </el-form-item>
  
      <el-form-item>
        <el-button type="primary" @click="submitForm">Sign Up</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script>
  import { reactive, ref } from 'vue';
  import { register } from '@/api';
  import { ElMessage } from 'element-plus';
  
  export default {
    components: {
      ElMessage
    },
    setup() {
      const signupFormRef = ref(null);
      const signupForm = reactive({
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
      });
  
      const validateConfirmPassword = (rule, value, callback) => {
        if (value !== signupForm.password) {
          return callback(new Error('The password confirmation does not match.'));
        }
        callback();
      };
  
      const rules = reactive({
        name: [
          { required: true, message: 'Please input your name', trigger: 'blur' }
        ],
        email: [
          { required: true, message: 'Please input your email address', trigger: 'blur' },
          { type: 'email', message: 'Please input a valid email address', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, message: 'Please input your password', trigger: 'blur' },
          { min: 8, message: 'Password length must be at least 8 characters', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: 'Please confirm your password', trigger: 'blur' },
          { validator: validateConfirmPassword, trigger: 'blur' }
        ],
      });

      const successMessage = () => {
        ElMessage({
          message: 'Sign up successful',
          type: 'success'
        });
      };

      const errorMessage = () => {
        ElMessage({
          message: 'Sign up failed',
          type: 'error'
        });
      };


      const attemptSignUp = async () => {
        const response = await register(signupForm.email, signupForm.password, signupForm.name);
        console.log(response)
        if (response?.success === true) {
          successMessage();
        } else {
          errorMessage();
        }
      };
  
      const submitForm = () => {
        signupFormRef.value.validate((valid) => {
          if (valid) {
            attemptSignUp();
            resetForm();
          }
        });
      };

      const resetForm = () => {
        signupFormRef.value.resetFields();
      };
  
      return {
        signupFormRef,
        signupForm,
        rules,
        submitForm,
      };
    },
  };
  </script>
  
  