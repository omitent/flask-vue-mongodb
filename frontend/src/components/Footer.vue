<template>
    <v-footer app fixed color="#333">
        <v-flex
            text-xs-center
            white--text
        >
            &copy; {{ copyright }}
        </v-flex>
    </v-footer>
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
</style>