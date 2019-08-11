<template>
<v-container fluid fill-height>
    <v-layout align-center justify-center text-center>
        <v-flex xs12 sm8 md4>
            <v-card>
                <v-toolbar dark color="#333">
                    <v-toolbar-title>Login</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                    <v-form ref='form' @submit.prevent="submit">
                        <v-text-field
                            prepend-icon="person"
                            label="Username"
                            v-model="username"
                            :rules="usernameRules"
                            required autofocus
                        >
                        </v-text-field>
                        <v-text-field
                            prepend-icon="lock"
                            label="Password"
                            type="password"
                            v-model="password"
                            :rules="passwordRules"
                            required
                        >
                        </v-text-field>
                        <v-btn :loading='userStatus.loggingIn' type='submit' color="#eee">Login</v-btn>
                    </v-form>
                    <div>
                        <small>
                            Don't have an account? Sign up <router-link to="/register">here</router-link>
                        </small>
                    </div>
                    <v-snackbar :value="!!userStatus.loginFailed" bottom color='error'>
                        {{ userStatus.message }}
                    </v-snackbar>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
    export default {
        name: 'Login',
        data() {
            return {
                username: '',
                password: '',
                usernameRules: [
                    v => !!v || 'Username is required'
                ],
                passwordRules: [
                    v => !!v || 'Password is required'
                ]
            }
        },
        computed: {
            userStatus() {
                return this.$store.state.auth.userStatus
            }
        },
        methods: {
            submit(e) {
                this.loading = true
                const { username, password } = this
                const { dispatch } = this.$store
                if (this.$refs.form.validate()) {
                    dispatch('auth/login', { username, password })
                }
            }
        }
    }
</script>