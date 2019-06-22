<template>
    <footer>&copy; {{ copyright }}</footer>
</template>


<script>
export default {
    name: 'Footer',
    computed:{
        copyright() {
            let date = new Date()
            return date.getFullYear()
        }
    }
}
</script>


<style scoped>
footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    color: #ffffff;
    background-color: #272727;
    font-size: 10px;
    line-height: 20px;
    box-shadow: 1px 1px 2px 2px #c7c7c7;
}
</style>