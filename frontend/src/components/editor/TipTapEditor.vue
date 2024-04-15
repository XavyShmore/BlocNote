<template>
    <el-tiptap v-if="note" ref="editor" :extensions="extensions"  height="100%" placeholder="Input note here..." v-model:content="note.content"/>
</template>

<script>
import { ElLoading, ElMessage } from 'element-plus';
import { ref } from 'vue';
import { getNote, saveNoteContent, getUserId } from '@/api';
import {
  Doc,
  Text,
  Paragraph,
  Heading,
  Bold,
  Underline,
  Italic,
  Strike,
  BulletList,
  OrderedList,
  Link,
  Image,
  Blockquote,
  ListItem,
  TodoItem,
  TodoList,
  TextAlign,
  Indent,
  HorizontalRule,
  HardBreak,
  History,
  Fullscreen,
} from 'element-tiptap-vue3-fixed';

export default {
    data() {
        return {
            note: { content: "" },
            userId: null,
            editor: ref(null)
        }
    },
    setup() {
        const extensions = [
            Doc,
            Text,
            Paragraph,
            Heading.configure({ level: 5 }),
            Bold.configure({ bubble: true }),
            Underline.configure({ bubble: true, menubar: false }),
            Italic,
            Strike,
            BulletList,
            OrderedList,
            HorizontalRule.configure({ buble: true }),
            Link.configure({ bubble: true }),
            Image,
            Blockquote,
            ListItem,
            TodoItem,
            TodoList,
            TextAlign,
            Indent,
            HardBreak,
            History,
            Fullscreen,
        ];

        return { extensions };
    },
    props: {
        noteId: {
            type: String,
            required: true
        },
    },
    methods: {
        saveContent() {
            saveNoteContent(this.noteId, this.note?.content, this.userId);
        },
        setContent(content) {
            console.log(content);
            this.$refs?.editor?.setContent(content); 
        },
    },
    async created() {
        let loadingInstance = null;
        try {
            loadingInstance = ElLoading.service({
            lock: true,
            text: 'Loading Note Data...',
            background: 'rgba(0, 0, 0, 0.7)'
            });

            this.userId = getUserId();
            try {
                const data = await getNote(this.noteId);
                this.note = data;
                this.$refs?.editor?.setContent(this.note.content); 
            } catch (error) {
                console.error('Error fetching note:', error);
            }

        } catch (error) {
            ElMessage({
                message: 'Failed to load notes data',
                type: 'error'
            });
            console.error('Failed to load notes data:', error);
        } finally {
            if (loadingInstance) {
                loadingInstance.close();
            }
        }
    },

}
</script>

<style>
</style>