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
                <template v-for="(page, i) in pages">
                    <v-list-group v-if="!!page.subgroups"
                     :prepend-icon="page.icon"
                     :key="i"
                    >
                        <template v-slot:activator>
                            <v-list-tile>
                                <v-list-tile-title>
                                    {{ page.title }}
                                </v-list-tile-title>
                            </v-list-tile>
                        </template>
                        <v-list-tile
                         v-for="(subpage, j) in page.subgroups"
                         :key="j"
                         :to="subpage.route"
                        >
                            <v-list-tile-title>
                                {{ subpage.title }}
                            </v-list-tile-title>
                            <v-list-tile-action>
                                <v-icon>{{ subpage.icon }}</v-icon>
                            </v-list-tile-action>
                        </v-list-tile>
                    </v-list-group>
                    <v-list-tile v-else
                     active-class=''
                     :to="page.route"
                     :key="i"
                    >
                        <v-list-tile-action>
                            <v-icon>{{ page.icon }}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-title>
                            {{ page.title }}
                        </v-list-tile-title>
                    </v-list-tile>
                </template>
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
            { title: 'Home', icon: 'home', route: '/' },
            { title: 'About', icon: 'help', route: '/about'},
            { title: 'Group', icon: 'group_work', subgroups: [
                { title: 'Count Words', icon: 'subject', route: '/count' },
                { title: 'Results', icon: 'list', route: '/results' }
            ]}
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