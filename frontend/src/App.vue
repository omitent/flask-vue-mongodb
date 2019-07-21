<template>
  <v-app id="app">
    <Nav></Nav>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'

export default {
  name: 'app',
  components: {
    Nav,
    Footer
  }
}
</script>

<style>

</style>
