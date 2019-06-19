<template>
    <b-container fluid>
        <b-row align-h='center'>
            <b-col cols=4>
                <b-form @submit='handleSubmit'>
                    <b-form-group>
                        <h4>Login</h4>
                    </b-form-group>
                    <b-form-group
                        label="Username"
                        label-for="username"
                    >
                        <b-form-input
                            id="username"
                            type='text'
                            v-model='username'
                            required autofocus
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group
                        label="Password"
                        label-for="password"
                    >
                        <b-form-input
                            id="password"
                            type='password'
                            v-model='password'
                            required
                        ></b-form-input>
                    </b-form-group>
                    <b-button type='submit' variant='dark'>Submit</b-button>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
</template>


<script>
    export default {
        name: 'Login',
        data() {
            return {
                username: '',
                password: '',
                submitted: false
            }
        },
        computed: {
            loggingIn () {
                return this.$store.state.auth.status.loggingIn
            }
        },
        methods: {
            handleSubmit(e) {
                e.preventDefault()
                this.submitted = true
                const { username, password } = this
                const { dispatch } = this.$store
                if (username && password ) {
                    dispatch('auth/login', { username, password })
                }
            }
        }
    }
</script>