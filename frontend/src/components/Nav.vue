<template>
    <b-navbar toggleable='lg' type='dark' variant='dark'>
        <b-navbar-brand href='/'>Home</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id='nav-collapse' is-nav>
            <b-navbar-nav class='ml-auto'>
                <template v-if="!loggedIn">
                    <b-nav-item to='register'>Register</b-nav-item>
                    <b-nav-item to='login'>Login</b-nav-item>
                </template>
                <template v-else>
                    <b-nav-item to='logout'>Logout</b-nav-item>
                </template>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>


<script>
export default {
    name: 'Nav',
    computed: {
        loggedIn() {
            return this.$store.state.auth.user && this.$store.state.auth.user.username && this.$store.state.auth.user.token
        },
        user() {
            return this.$store.state.auth.user
        }
    }
}
</script>


<style scoped>
.router-link-exact-active {
    color: white
}
.navbar {
    margin-bottom: 15px;
}
</style>