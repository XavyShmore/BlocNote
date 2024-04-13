<template>
    <div class="header">
        <h1 class="title">
            {{ noteName }}
        </h1>
        <div>
            <el-button class="noteButton" @click="saveNote">
                Save
            </el-button>
            <el-button class="noteButton">
                Share
            </el-button>
        </div>
    </div>
    <div class="noteInfo">
        <el-input readonly v-model="lastModif"/>
        <el-input readonly v-model="lastModifDate"/>
    </div>
    <div class="content">
        <TipTapEditor :noteId="id" ref="tipTapEditor"/>
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { ElButton } from 'element-plus'
import TipTapEditor from '@/components/editor/TipTapEditor.vue'
import { getNote } from '@/api'

export default defineComponent({
  components: {
    TipTapEditor,
    ElButton
  },
  setup() {
    const tipTapEditor = ref(null);

    const saveNote = () => {
        if (tipTapEditor.value) {
            tipTapEditor.value.saveContent()
        }
    }

    return { tipTapEditor, saveNote }
  },
    data() {
        return {
        note: null,
        noteName: '',
        lastModif: 'Last Modification by : ',
        lastModifDate: 'Last Modification Date :'
        }
    },
    computed: {
        id() {
        return this.$route.params.id;
        }
    },
    methods: {
        async getNoteInfo() {
            this.note = await getNote(this.id);
            this.noteName = this.note.title;
            this.lastModif += this.note.user_last_modified;
            this.lastModifDate += this.note.last_modified;
        }
    },
    mounted() {
        this.getNoteInfo();
    }
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
    margin-top: 1%;
}

.title {
    margin: 1vh 1vw;
    font-size: 3em;
}

.noteButton {
    margin: 1vh 0.5vw 1vh 0;
}

.noteInfo {
    display: flex;
    margin: 2vh 0;
    padding-right: 50%;
    justify-content: space-evenly;
}

.noteInfo > * {
    margin: 1vh 1vw;
}

.editorClass {
    height: 320px;
}

</style>