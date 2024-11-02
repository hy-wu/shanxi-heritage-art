<template>
  <div id="app">
    <AppHeader />
    <MainNav />
    <MainContent />
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';
import MainNav from './components/MainNav.vue';
import MainContent from './components/MainContent.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  components: {
    AppHeader,
    MainNav,
    MainContent,
    AppFooter
  }
};
</script>

<style>
@import './assets/styles.css';
</style>
