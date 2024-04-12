<template>
  <el-page-header @back="goBack" class="pageHeader">
    <template #content>
      <span class="text-large font-600 mr-3"> Title </span>
    </template>
    <template>
        <el-divider style="margin-top: 12px;"/>
    </template>
  </el-page-header>
</template>

<script>
import { ElPageHeader, ElDivider } from 'element-plus';

export default {
    components: {
        ElPageHeader,
        ElDivider
    },
    setup() {
        const goBack = () => {
            console.log('go back')
        }

        return { goBack }
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