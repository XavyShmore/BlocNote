<template>
    <div class="header">
        <h1 class="title">
            Vive bugs !!!
        </h1>
        <div>
            <el-button class="noteButton">
                Save
            </el-button>
            <el-button class="noteButton">
                Share
            </el-button>
        </div>
    </div>
    <div class="content">
        <TipTapEditor/>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { ElButton } from 'element-plus'
import TipTapEditor from '@/components/Editor/TipTapEditor.vue'

export default defineComponent({
  components: {
    TipTapEditor,
    ElButton
  },
});
</script>

<style>
.header {
    height: 16vh;
    border-bottom: 2px solid black;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
}

.content {
    height: 70vh;
    padding-top: 1%;
}

.title {
    margin: 1vh 1vw;
    font-size: 3em;
}

.noteButton {
    margin: 1vh 0.5vw 1vh 0;
}

.editorClass {
    height: 320px;
}

</style>