<template>
    <div>
        <h4>Results</h4>
        <table class="table">
            <thead>
                <th>URL</th>
                <th>Time Submitted</th>
                <th>Time Finished</th>
                <th>Number of Words</th>
            </thead>
            <tr v-for="res in results" v-bind:key="res._id">
                <td>{{ res.url }}</td>
                <td>{{ res.submitted }}</td>
                <td>{{ res.finished }}</td>
                <td>{{ res.num_words }}</td>
            </tr>
        </table>
    </div>
</template>


<script>
export default {
    name: 'Results',
    data() {
        return {
            results: []
        }
    },
    mounted() {
        this.$http.get(
            '/api/results',
            {
                headers: {
                    'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                }
            }
        )
        .then(resp => {
            this.results = resp.data.results
        })
        .catch(error => {
            alert('Error: '+error)
        })
    }
}
</script>


<style scoped>

</style>