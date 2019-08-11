<template>
<v-container>
    <v-layout>
        <v-flex xs12 text-center>
            <h1>Admin Dashboard</h1>
            <v-tabs
              dark
              v-model="currentTab"
              centered
            >
                <v-tabs-slider></v-tabs-slider>
                <v-tab
                    v-for="tab in tabs"
                    :key="tab.name"
                    :href="`#${tab.name}`"
                >
                    {{ tab.title }}
                </v-tab>
                <v-tab-item
                    v-for="tab in tabs"
                    :key="tab.name"
                    :value="`${tab.name}`"
                >
                    <v-card flat>
                        <v-card-text>
                            {{ tab.name }}
                        </v-card-text>
                    </v-card>
                </v-tab-item>
            </v-tabs>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Admin',
    data() {
        return {
            currentTab: 'users',
            tabs: [
                { name: 'users', title: 'Users', data: [] },
                { name: 'groups', title: 'Groups', data: [] }
            ]
        }
    },
    mounted() {
        this.$http.get(
            '/api/admin/auth', 
            {
                headers: {'Authorization': 'Bearer ' + this.$store.state.auth.user.token}
            }
        ).catch(error => {
            console.log(error)
            this.$router.push('/login')
        }).then(() => {
            this.getGroups()
        })
    },
    methods: {
        getUsers() {
            this.$http.get(

            )
        },
        getGroups() {
            this.$http.get(
                '/api/admin/group',
                {
                    headers: {'Authorization': 'Bearer ' + this.$store.state.auth.user.token}
                }
            ).then(resp => {
                console.log(resp.data)
                this.tabs[1].data = resp.data.groups
            })
        }
    }
}
</script>
