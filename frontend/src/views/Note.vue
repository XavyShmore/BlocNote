<template>
    <div class="header">
        <h1 class="title">
            {{ noteName }}
        </h1>
        <div class="noteControl">
            <div class="versionContent">
                <label for="versionSelect" style="margin-right: 8px">Versions </label>
                <el-select v-model="selectedVersion" id="versionSelect" placeholder="Select a version" @change="setContent(selectedVersion)">
                    <el-option
                        v-for="version in versions"
                        :key="version.label"
                        :label="version.label"
                        :value="version.value"
                    >
                    </el-option>
                </el-select>
            </div>
            <el-button class="noteButton" @click="saveNote">
                Save
            </el-button>
            <el-button class="noteButton" @click="shareNote">
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
import { ElButton, ElLoading, ElMessageBox, ElMessage, ElSelect } from 'element-plus'
import TipTapEditor from '@/components/editor/TipTapEditor.vue'
import { addNoteOwner, getNote, getNoteOwners, getNoteVersions, getUserId } from '@/api'

export default defineComponent({
  components: {
    TipTapEditor,
    ElLoading,
    ElButton,
    ElMessageBox,
    ElSelect
  },
  data() {
    return {
    userId: null,
    note: null,
    noteName: '',
    lastModif: 'Last Modification by : ',
    lastModifDate: 'Last Modification Date : ',
    owners: [],
    versions: [],

    }
  },
  setup() {
    const tipTapEditor = ref(null);
    const selectedVersion = ref(null);

    const saveNote = () => {
        if (tipTapEditor.value) {
            tipTapEditor.value.saveContent()
        }
    }

    const setContent = (content) => {
        console.log(content)
        tipTapEditor.value.setContent(content)
    }

    return { tipTapEditor, saveNote, setContent, selectedVersion }
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
        },

        async getOwners() {
            try {
                this.owners = await getNoteOwners(this.id, this.userId);
                console.log(this.owners);
            } catch (error) {
                console.error('Failed to fetch note owners:', error);
            }
            return this.owners;
        },

        async addOwner() {
            let loadingInstance = null;
            try {
                loadingInstance = ElLoading.service({
                lock: true,
                text: 'Adding New Owner...',
                background: 'rgba(0, 0, 0, 0.7)'
                });
                await addNoteOwner(this.id, this.userId);
            
            } catch (error) {
                ElMessage({
                    message: 'Failed to add or fetch notebooks',
                    type: 'error'
                });
                console.error('Failed to add or fetch notebooks:', error);
            } finally {
                if (loadingInstance) {
                    loadingInstance.close();
                }
            }
        },
        
        async shareNote() {
            try {
                let owners = await this.getOwners();
                let formattedOwners = owners.length ? owners.map(owner => owner.name).join(', ') : 'Not Shared Yet';
                
                this.$prompt(`Current Owners: ${formattedOwners}.<br> <br> Enter the email of the person you want to share the note with:`, 'Share Note', {
                    confirmButtonText: 'Share',
                    cancelButtonText: 'Cancel',
                    inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
                    inputErrorMessage: 'Invalid Email',
                    inputPlaceholder: 'Email Address',
                    dangerouslyUseHTMLString: true,
                    inputValue: '',
                }).then(({ value }) => {
                    this.noteShareAttempt(value);
                }).catch(error => {
                    if (error !== 'cancel' && error !== 'close' && error !== 'overlay') {
                        this.$message({
                            type: 'info',
                            message: 'Sharing cancelled'
                        });
                    }
                });
            } catch (error) {
                ElMessage({
                    type: 'error',
                    message: `The note could not be shared: ${error}`,
                })
            }
        },
        async noteShareAttempt(email) {
            try {
                await addNoteOwner(this.id, email);
                ElMessage({
                    type: 'success',
                    message: `The note was shared to : ${email}`,
                })
            }
            catch (error) {
                ElMessage({
                    type: 'error',
                    message: `The note could not be shared: ${error}`,
                })
            }
        },
        async getNoteVersions() {
            try {
                let version = await getNoteVersions(this.id);
                version.sort((a, b) => new Date(a.creation) - new Date(b.creation));
                this.versions = version.map((version, index) => ({
                    label: `Version ${index + 1}`,
                    value: version.content, 
                    creation: version.creation
                }));
            } catch (error) {
                console.error('Failed to fetch note versions:', error);
            }
        }
    },
    mounted() {
        this.userId = getUserId();
        this.getNoteInfo();
        this.getOwners();
        this.getNoteVersions();
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

.versionContent {
    display: flex;
    align-items: center;
    width: 100%;
    margin-right: 1vw;
}

.noteControl {
    display: flex;
    justify-content: flex-end;
    width: 22%;
}

</style>