<template>
    <div class="header" :style="{ width: width }">
        <h1 class="title" :style="{ fontSize: fontSize }">
            <slot name="title"></slot>
        </h1>
    </div>
</template>

<script>

export default {
    name: 'PageTitle',
    props: {
        fontSize: {
            type: String,
            default: '3em'
        },
        width: {
            type: String,
            default: '100%'
        }
    },
}

</script>

<style>
.header {
    height: 16vh;
    border-bottom: 2px solid black;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
}

.title {
    margin: 1vh 1vw;
}
</style>