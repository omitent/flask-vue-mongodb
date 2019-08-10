<template>
<v-container>
    <v-layout>
        <v-flex xs10 text-center>
            <h1>Admin</h1>
            <div>Welcome {{ username }}</div>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Admin',
    data() {
        return {
            username: ''
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
        })
    },
    methods: {
        
    }
}
</script>
