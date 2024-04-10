<template>
    <div class="card flex justify-content-center">
        <Breadcrumb :model="breadcrumbItems"></Breadcrumb>
        <RouterView></RouterView>
    </div>
</template>

<script>
import { defineComponent, reactive, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Breadcrumb from 'primevue/breadcrumb';


export default defineComponent({
  name: "BreadcrumbRoutes",
  components: {
    Breadcrumb 
  },
  setup() {
    const route = useRoute();
    const router =  useRouter();
    const breadcrumbItems = reactive([]);

    const fetchBreadcrumbData = async (pathSegment) => {
      return pathSegment.charAt(0).toUpperCase() + pathSegment.slice(1);
    };

    const updateBreadcrumb = async () => {
      breadcrumbItems.length = 0;
      breadcrumbItems.push({ label: 'Home', command: () => { router.push('/'); } });

      let pathAccumulator = '';
      const pathSegments = route.path.split('/').filter(p => p);
      
      for (const segment of pathSegments) {
        pathAccumulator += `/${segment}`;
        const label = await fetchBreadcrumbData(segment);

        breadcrumbItems.push({
          label: label,
          command: () => { router.push(pathAccumulator); }
        });
      }
    };

    watch(() => route.path, updateBreadcrumb, { immediate: true });

    onMounted(updateBreadcrumb);

    return {
      breadcrumbItems
    };
  }
});
</script>

<style>
    .header {
        width: 100%;
        position: relative;
        top: 0;
        left: 0;
        z-index: var(--z-fixed);
        background-color: var(--body-color);
    }
    .nav.container {
        height: 2rem;
        margin-top: 1.5rem;
        display: flex;
        justify-content: space-between;
    }
</style>