<template>
    <b-container fluid>
        <b-row align-h='center'>
            <b-col cols=4>
                <b-form @submit="handleSubmit">
                    <b-form-group>
                        <h4>Register</h4>
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
                    <b-form-group
                        label="Confirm password"
                        label-for="password-confirm"
                    >
                        <b-form-input
                            id="password-confirm"
                            type='password'
                            v-model='passwordConfirm'
                            required
                        ></b-form-input>
                    </b-form-group>
                    <b-button type="submit" variant="dark">Submit</b-button>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
</template>


<script>
export default {
    name: 'Register',
    props: ['nextUrl'],
    data() {
        return {
            username: '',
            password: '',
            passwordConfirm: ''
        }
    },
    methods: {
        handleSubmit(e) {
            e.preventDefault()
            if (this.password === this.passwordConfirm && this.password.length > 0) {
                const { username, password } = this
                const { dispatch } = this.$store
                dispatch('auth/register', { username, password })
            } else {
                this.password = ''
                this.passwordConfirm = ''
                return alert('Passwords do not match!')
            }
        }
    }
}
</script>