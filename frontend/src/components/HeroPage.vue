<template>
    <BreadcrumbRoutes/>
</template>

<script>
import BreadcrumbRoutes from './BreadcrumbRoutes.vue';

export default {
    components: {
        BreadcrumbRoutes: BreadcrumbRoutes
    }
}

</script>

<style>
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