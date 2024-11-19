<template>
    <main>
        <AboutSection />
        <ArtworkSection />
        <HeritageSection />
        <DigitalSection @add-to-cart="handleAddToCart" />
        <CultureSection />
        <FeedbackSection />
        <CartSection :cart="cart" @remove-from-cart="handleRemoveFromCart" @checkout="handleCheckout" />
    </main>
</template>

<script>
import AboutSection from './sections/AboutSection.vue';
import ArtworkSection from './sections/ArtworkSection.vue';
import HeritageSection from './sections/HeritageSection.vue';
import DigitalSection from './sections/DigitalSection.vue';
import CultureSection from './sections/CultureSection.vue';
import FeedbackSection from './sections/FeedbackSection.vue';
import CartSection from './sections/CartSection.vue';

export default {
    components: {
        AboutSection,
        ArtworkSection,
        HeritageSection,
        DigitalSection,
        CultureSection,
        FeedbackSection,
        CartSection
    },
    data() {
        return {
            cart: []
        };
    },
    methods: {
        handleAddToCart(product) {
            this.cart.push(product);
        },
        handleRemoveFromCart(product) {
            const index = this.cart.indexOf(product);
            if (index > -1) {
                this.cart.splice(index, 1);
            }
        },
        handleCheckout() {
            alert('订单已提交！\n此功能未实现！');
            this.cart = [];
        },
        toggleCartSection() {
            this.$emit('toggle-cart');
        }
    }
};
</script>

<style scoped>
/* 可以在这里添加特定于 MainContent 的样式 */
</style>