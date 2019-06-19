<template>
    <div>
        <h4>Register</h4>
        <form>
            <label for='username'>Username</label>
            <div>
                <input id='username' type='text' v-model='username' required autofocus>
            </div>
            <label for='password'>Password</label>
            <div>
                <input id='password' type='password' v-model='password' required>
            </div>
            <label for='password-confirm'>Confirm password</label>
            <div>
                <input id='password-confirm' type='password' v-model='password_confirm' required>
            </div>
            <div>
                <button type='submit' @click='handleSubmit'>
                    Sign up
                </button>
            </div>
        </form>
    </div>
</template>


<script>
export default {
    name: 'Register',
    props: ['nextUrl'],
    data() {
        return {
            username: '',
            password: '',
            password_confirm: ''
        }
    },
    methods: {
        handleSubmit(e) {
            e.preventDefault()
            if (this.password === this.password_confirm && this.password.length > 0) {
                const { username, password } = this
                const { dispatch } = this.$store
                dispatch('auth/register', { username, password })
            } else {
                this.password = ''
                this.password_confirm = ''
                return alert('Passwords do not match!')
            }
        }
    }
}
</script>