<template>
    <div>
        You've been logged out!
    </div>
</template>


<script>
export default {
    name: 'Home',
    created () {
        this.$store.dispatch('auth/logout')
    }
}
</script>


<style scoped>

</style>