<template>
    <div>
        URL: <input class="form-control" type="text" v-model="url">
        <button class='btn btn-success' @click="handleSubmit">Submit</button>
        <div v-if="running==false && result.finished">
            The website {{ result.url }} has {{ result.num_words }} words
        </div>
    </div>
</template>


<script>
export default {
    name: 'Count',
    data() {
        return {
            url: '',
            running: false,
            result: {}
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
                    this.result = resp.data.result
                }
                else {
                    setTimeout(this.poll, 1000, _id)
                }
            })
        },
        handleSubmit() {
            this.$http.get(
                '/api/count?url='+this.url,
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
</script>


<style scoped>

</style>