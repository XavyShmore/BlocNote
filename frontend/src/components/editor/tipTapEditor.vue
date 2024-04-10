<template>
    <el-tiptap :extensions="extensions" :editorProps="props" height="100%"/>
</template>

<script>
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
  CodeView

} from 'element-tiptap-vue3-fixed';

export default {
    components: {
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
            CodeView,

        ];

        const props = {
            editorProps: {
                attributes:
                {
                    class: "editorBorder"
                }
            }
        }

        return { extensions, props }
  },
}
</script>

<style>
.editorBorder {
    border-color: red;
}

</style>