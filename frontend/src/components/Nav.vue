<template>
    <b-navbar toggleable='lg' type='dark' variant='dark'>
        <b-navbar-brand to='/'>
            <i class="fas fa-home"></i>
        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id='nav-collapse' is-nav>
            <b-navbar-nav>
                <b-nav-item to='about'>About</b-nav-item>
                <b-nav-item to='contact'>Contact</b-nav-item>
                <b-nav-item v-if="loggedIn" to='count'>Count</b-nav-item>
                <b-nav-item v-if="loggedIn" to='results'>My Results</b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class='ml-auto'>
                <template v-if="!loggedIn">
                    <b-nav-item to='register'>Register</b-nav-item>
                    <b-nav-item to='login'>Login</b-nav-item>
                </template>
                <template v-else>
                    <b-nav-item to='logout'>Logout</b-nav-item>
                    <b-nav-item to='profile'>
                        <i class="fas fa-user"></i>
                    </b-nav-item>
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
.navbar {
    box-shadow: 1px 1px 2px 2px #c7c7c7 !important;
}

.bg-dark {
    background-color: #272727 !important;
}

.navbar-brand {
    color: rgba(255, 255, 255, 0.5) !important;
}

.nav-link {
    color: rgba(255, 255, 255, 0.5) !important;
}

.router-link-exact-active {
    color: white !important;
}
.navbar {
    margin-bottom: 15px;
}
</style>