<template>
    <div class='container'>
        <div class='row justify-content-md-center'>
            <div class='col-4'>
                <form>
                    <div class='form-group'>
                        <h4>Login</h4>
                    </div>
                    <div class='form-group'>
                        <label for='username'>Username</label>
                        <input class='form-control' id='username' type='text' v-model='username' required autofocus>
                    </div>
                    <div class='form-group'>
                        <label for='password'>Password</label>
                        <input class='form-control' id='password' type='password' v-model='password' required>
                    </div>
                    <div>
                        <button class='btn btn-dark' type='submit' @click='handleSubmit'>
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
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