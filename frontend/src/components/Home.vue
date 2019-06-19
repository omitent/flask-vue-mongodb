<template>
    <div>
        This is the homepage {{ user.username }}
    </div>
</template>


<script>
export default {
    name: 'Home',
    computed: {
        user() {
            return this.$store.state.auth.user
        }
    }
}
</script>


<style scoped>

</style>