<template>
    <nav>
        <v-navigation-drawer
            v-model="drawer.open"
            app
        >
            <v-list>
                <v-list-tile>
                    <v-list-tile-action @click="toggleDrawer">
                        <v-btn icon>
                            <v-icon>arrow_back</v-icon>
                        </v-btn>
                    </v-list-tile-action>
                </v-list-tile>
                <v-list-tile
                    active-class=''
                    v-for="page in pages"
                    :key="page.title"
                    :to="page.route"
                >
                    <v-list-tile-content>
                        <v-list-tile-title>{{ page.title }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar 
            app
            fixed
            dark color="#333"
        >
            <v-toolbar-side-icon 
                @click.stop="toggleDrawer"
            ></v-toolbar-side-icon>
            <v-btn to='/' icon active-class=''>
                <v-icon>home</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn icon active-class='' v-on='on'>
                        <v-icon>account_circle</v-icon>
                    </v-btn>
                </template>
                <v-list v-if="loggedIn">
                    <v-list-tile to='/profile' active-class=''>
                        <v-list-tile-title>Profile</v-list-tile-title>
                    </v-list-tile>
                    <v-list-tile to='/logout' active-class=''>
                        <v-list-tile-title>Logout</v-list-tile-title>
                    </v-list-tile>
                </v-list>
                <v-list v-else>
                    <v-list-tile to='/register' active-class=''>
                        <v-list-tile-title>Register</v-list-tile-title>
                    </v-list-tile>
                    <v-list-tile to='/login' active-class=''>
                        <v-list-tile-title>Login</v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-menu>
        </v-toolbar>
    </nav>
</template>


<script>
export default {
    name: 'Nav',
    data: () => ({
        drawer: {
            open: false
        },
        pages: [
            { title: 'Home', route: '/' },
            { title: 'About', route:'/about'}
        ]
    }),
    methods: {
        toggleDrawer () {
            this.drawer.open = !this.drawer.open
        }
    },
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
</style>