<template>
<v-container fluid grid-list-md>
    <v-layout align-start justify-space-around row wrap text-center>
        <v-flex xs12 tag='h1'>
            This is the homepage
        </v-flex>
        <v-flex xs12 tag='p'>
            This is more content
        </v-flex>
        <v-flex xs12 sm6 md3 text-xs-left mx-3>
            <v-card>
                <v-card-title primary-title class="headline">
                    Title
                </v-card-title>
                <v-card-text>
                    This is some content. Here are some longer sentences so we can see what the card looks like when there is some text.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text>Test</v-btn>
                </v-card-actions>
            </v-card>
        </v-flex>
        <v-flex xs12 sm6 md3 text-xs-left mx-3>
            <v-card>
                <v-card-title primary-title class="headline">
                    Title
                </v-card-title>
                <v-card-text>
                    This is some content. Here are some longer sentences so we can see what the card looks like when there is some text.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text>Test</v-btn>
                </v-card-actions>
            </v-card>
        </v-flex>
        <v-flex xs12 sm6 md3 text-xs-left mx-3>
            <v-card>
                <v-card-title primary-title class="headline">
                    Title
                </v-card-title>
                <v-card-text>
                    This is some content. Here are some longer sentences so we can see what the card looks like when there is some text.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text>Test</v-btn>
                </v-card-actions>
            </v-card>
        </v-flex>
        <v-flex xs12 sm6 md3 text-xs-left mx-3>
            <v-card>
                <v-card-title primary-title class="headline">
                    Title
                </v-card-title>
                <v-card-text>
                    This is some content. Here are some longer sentences so we can see what the card looks like when there is some text.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text>Test</v-btn>
                </v-card-actions>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>


<script>
export default {
    name: 'Home',
    computed: {
        user() {
            return this.$store.state.auth.user
        }
    }
}
</script>


<style scoped>

</style>