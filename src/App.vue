<template>
  <div id="app">
    <AppHeader />
    <MainNav />
    <MainContent />
    <AppFooter />
    <div class="floating-cart-icon">
      <a href="#cart">🛒</a >
    </div>
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

.floating-cart-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #f44336;
  color: white;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  font-size: 24px;
}
</style>
