<template>
<v-container fluid fill-height>
    <v-layout align-content-start justify-center row>
        <v-flex xs12 text-center>
            <h1>
                Queues
                <v-btn 
                  icon
                  @click="load"
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
              :items="workers"
              class="elevation-1"
              dense
            ></v-data-table>
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
                { text: 'Names', value: 'name' },
                { text: 'Busy', value: 'busy' },
                { text: 'available', value: 'available' },
            ],
            workers: []
        }
    },
    mounted() {
        this.load()
    },
    methods: {
        load() {
            this.loading = true
            this.$http.get(
                '/api/status',
                {
                    headers: {
                        'Authorization': 'Bearer ' + this.$store.state.auth.user.token
                    }
                }
            )
            .then(resp => {
                this.workers = resp.data
                this.loading = false
            })
            .catch(error => {
                this.loading = false
                alert('Error: '+error)
            })
        }
    }
}
</script>