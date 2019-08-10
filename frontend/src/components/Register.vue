<template>
<v-container fluid fill-height>
    <v-layout align-center justify-center text-center>
        <v-flex xs12 sm8 md4>
            <v-card>
                <v-toolbar dark color="#333">
                    <v-toolbar-title>Register</v-toolbar-title>
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
                        <v-text-field
                            prepend-icon="lock"
                            label="Confirm password"
                            type="password"
                            v-model="passwordConfirm"
                            :rules="passwordConfirmRules"
                            required
                        >
                        </v-text-field>
                        <v-btn type="submit" color="#eee">Register</v-btn>
                    </v-form>
                    <div>
                        <small>
                            Already have an account? Login <router-link to="/login">here</router-link>
                        </small>
                    </div>
                    <div>
                        <v-alert :value="!!userStatus.loginFailed" type="error" border="left" colored-border dismissible elevation="2" outlined>
                            {{ userStatus.message }}
                        </v-alert>
                    </div>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Register',
    props: ['nextUrl'],
    data() {
        return {
            username: '',
            password: '',
            passwordConfirm: '',
            usernameRules: [
                v => !!v || 'Username is required',
                v => v.indexOf(' ') < 0 || 'Username cannot contain spaces'
            ],
            passwordRules: [
                v => !!v || 'Password is required',
                v => v.length >= 5 || 'Password must be at least 5 characters long'
            ],
            passwordConfirmRules: [
                v => !!v || 'Please confirm your password',
                v => v === this.password || 'Passwords do not match'
            ],
            loading: false
        }
    },
    computed: {
        userStatus() {
            return this.$store.state.auth.userStatus
        }
    },
    methods: {
        submit(e) {
            if (this.$refs.form.validate()) {
                const { username, password } = this
                const { dispatch } = this.$store
                dispatch('auth/register', { username, password })
            }
        }
    }
}
</script>

<style scoped>

</style>