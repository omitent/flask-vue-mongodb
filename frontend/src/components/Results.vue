<template>
<v-container fluid fill-height>
    <v-layout justify-center row>
        <v-flex xs12 text-center>
            <h1>
                Results
                <v-btn 
                  icon
                  @click="loadResults"
                  :loading="loading"
                >
                    <v-icon>refresh</v-icon>
                </v-btn>
            </h1>
            
        </v-flex>
        <v-flex xs10>
            <v-data-table
              :loading="loading"
              :headers="headers"
              :items="results"
              class="elevation-1"
              dense
            >
                <template v-slot:item.delete="{ item }">
                    <v-icon
                      small
                      @click="deleteItem(item)"
                    >delete</v-icon>
                </template>
            </v-data-table>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Results',
    data() {
        return {
            loading: true,
            headers: [
                { text: 'URL', value: 'url' },
                { text: 'Number of Words', value: 'num_words' },
                { text: 'Time Submitted', value: 'submitted' },
                { text: 'Time Finished', value: 'finished' },
                { text: 'Delete', value: 'delete', sortable: false, align: 'center' },
            ],
            results: []
        }
    },
    mounted() {
        this.loadResults()
    },
    methods: {
        loadResults() {
            this.loading = true
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
                this.loading = false
            })
            .catch(error => {
                this.loading = false
                alert('Error: '+error)
            })
        },
        deleteItem(item) {
            const index = this.results.indexOf(item)
            if (confirm('Are you sure you want to delete this result?')) {
                this.$http.delete(
                    '/api/results', {
                        params: { '_id': item['_id'] },
                        headers: {
                            'Content-Type': 'applicatation/json',
                            'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                        }
                    }
                )
                .then(resp => {
                    if (resp.data.ok) {
                        this.results.splice(index, 1)
                    }
                })
                .catch(error => {
                    alert('Delete failed')
                })
            }
        }
    }
}
</script>


<style scoped>

</style>