<template>
<v-container fluid fill-height>
    <v-layout row align-center justify-center text-center>
        <v-flex xs12 sm8 md4>
            <v-card>
                <v-toolbar dark color="#333">
                    <v-toolbar-title>Count words</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                    <v-form ref='form' @submit.prevent="submit">
                        <v-text-field 
                          label="URL"
                          v-model="url"
                          :loading='running==true'
                          prefix="https://"
                          clearable
                          placeholder="google.com"
                          :rules="urlRules"
                          required autofocus
                        ></v-text-field>
                        <v-btn 
                          type='submit' 
                          color="#eee"
                          :loading='running==true'
                        >Submit</v-btn>
                    </v-form>
                </v-card-text>
                <v-card-text v-if="running==false && result.finished">
                    The website {{ result.url }} has {{ result.num_words }} words
                </v-card-text>
                <v-alert
                  v-if="!!error"
                  type="error"
                >
                    {{ this.error }}
                </v-alert>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Count',
    data() {
        return {
            url: '',
            running: false,
            result: {},
            error: '',
            urlRules: [
                v => !!v || "Please enter url",
                v => !v.startsWith('https://') || "Leave out the https://",
                v => !v.startsWith('http://') || "Leave out the http://",
                v => !v.includes(' ') || "URL cannot include spaces"
            ]
        }
    },
    methods: {
        poll(_id) {
            this.$http.get(
                '/api/results/poll/'+_id,
                {
                    headers: {
                        'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                    }
                }
            )
            .then(resp => {
                if (resp.data.ok && resp.data.finished) {
                    this.running = false
                    if (resp.data.error) {
                        this.error = resp.data.error
                        setTimeout(() => this.error='', 3000)
                    }
                    else {
                        this.result = resp.data.result
                    }
                }
                else {
                    setTimeout(this.poll, 1000, _id)
                }
            })
        },
        submit() {
            this.result = {}
            if (this.$refs.form.validate()) {
                this.$http.get(
                    '/api/count?url=https://'+this.url,
                    {
                        headers: {
                            'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                        }
                    }
                )
                .then(resp => {
                    if (resp.data.ok == true) {
                        this.running= true
                        this.poll(resp.data._id)
                    }
                    else {
                        alert('Error submitting task!')
                    }
                })
            }
        }
    }
}
</script>


<style scoped>

</style>