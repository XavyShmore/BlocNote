<template>
  <el-page-header @back="goBack" class="pageHeader">
    <template #content>
      <span class="text-large font-600 mr-3"> {{ capitalizeFirstLetter(title) }} </span>
    </template>
    <template #extra>
        <el-button type="primary" @click="logout">Logout</el-button>
    </template>
    <template>
        <el-divider style="margin-top: 12px;"/>
    </template>
  </el-page-header>
</template>

<script>
import { ElPageHeader, ElDivider, ElButton } from 'element-plus';
import { useRouter } from 'vue-router';
import { debounce } from 'lodash';

export default {
    components: {
        ElPageHeader,
        ElDivider,
        ElButton
    },
    props: {
        title: {
            type: String,
            required: true
        }
    },
    setup() {
        const router = useRouter();

        const goBack = debounce(() => {
            if (window.history.length > 1) {
                router.back();
            } else {
                router.push('/home');
            }
        }, 300);

        function capitalizeFirstLetter(string) {
            return string?.charAt(0)?.toUpperCase() + string?.slice(1);
        }

        const logout = () => {
            localStorage.removeItem('token');
            router.push({ name: 'login' });
        }

        return { goBack, capitalizeFirstLetter, logout }
    }
}

</script>

<style>
    .pageHeader { 
        margin: 1vh 1vw
    }

    .menu {
        display: flex;
        width: 100%
    }

    .side-section {
        width: 25%;
        height: 100%;
        background-color: black;
    }

    .middle-section {
        width: 50%;
        height: 100%;
        background-color: aqua;
    }

</style>