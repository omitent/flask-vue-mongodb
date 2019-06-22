<template>
    <div>
        <h1>User Profile</h1>
        <div>Welcome {{ username }}</div>
        <button class='btn btn-danger' @click='deleteAccount'>
            Delete account
        </button>
    </div>
</template>


<script>
export default {
    name: 'Profile',
    data() {
        return {
            username: ''
        }
    },
    mounted() {
        this.$http.get(
            '/api/user', 
            {
                headers: {'Authorization': 'Bearer ' + this.$store.state.auth.user.token}
            }
        ).then(resp => {
            this.username = resp.data.username
        }).catch(error => {
            console.log(error)
            this.$router.push('/')
        })
    },
    methods: {
        deleteAccount() {
            this.$http.delete(
                '/api/user',
                {
                    headers: {
                        'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                    }
                }
            ).then(resp => {
                console.log(resp.data)
                alert('account deleted successfully')
                this.$store.dispatch('auth/logout')
                this.$router.push('/')
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
