<template>
    <nav>
        <v-navigation-drawer
            v-model="drawer"
            app
        >
            <v-list dense nav>
                <v-list-item>
                    <v-list-item-action @click="drawer = !drawer">
                        <v-btn icon>
                            <v-icon>arrow_back</v-icon>
                        </v-btn>
                    </v-list-item-action>
                    <v-list-item-title>
                        Navigation
                    </v-list-item-title>
                </v-list-item>
                <template v-for="(page, i) in pages">
                    <v-list-group v-if="!!page.subgroups"
                     :prepend-icon="page.icon"
                     :key="i"
                    >
                        <template v-slot:activator>
                            <v-list-item-title>
                                {{ page.title }}
                            </v-list-item-title>
                        </template>
                        <v-list-item
                         v-for="(subpage, j) in page.subgroups"
                         :key="j"
                         :to="subpage.route"
                        >
                            <v-list-item-title>
                                {{ subpage.title }}
                            </v-list-item-title>
                            <v-list-item-action>
                                <v-icon>{{ subpage.icon }}</v-icon>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list-group>
                    <v-list-item v-else
                     active-class=''
                     :to="page.route"
                     :key="i"
                    >
                        <v-list-item-action>
                            <v-icon>{{ page.icon }}</v-icon>
                        </v-list-item-action>
                        <v-list-item-title>
                            {{ page.title }}
                        </v-list-item-title>
                    </v-list-item>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar 
            app
            fixed
            dark color="#333"
        >
            <v-app-bar-nav-icon 
                @click.stop="drawer = !drawer"
            ></v-app-bar-nav-icon>
            <v-btn to='/' icon>
                <v-icon>home</v-icon>
            </v-btn>
            <v-btn to='/modules' icon>
                <v-icon>apps</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn icon v-on='on'>
                        <v-icon>account_circle</v-icon>
                    </v-btn>
                </template>
                <v-list v-if="loggedIn">
                    <v-list-item to='/profile'>
                        <v-list-item-title>Profile</v-list-item-title>
                    </v-list-item>
                    <v-list-item to='/logout'>
                        <v-list-item-title>Logout</v-list-item-title>
                    </v-list-item>
                </v-list>
                <v-list v-else>
                    <v-list-item to='/register'>
                        <v-list-item-title>Register</v-list-item-title>
                    </v-list-item>
                    <v-list-item to='/login'>
                        <v-list-item-title>Login</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-app-bar>
    </nav>
</template>


<script>
export default {
    name: 'Nav',
    data: () => ({
        drawer: false,
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