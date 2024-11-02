<template>
    <section id="cart" class="section">
        <h2>购物车</h2>
        <div class="cart-container" data-aos="fade-up">
            <div v-if="cart.length === 0">
                <p>您的购物车是空的。</p>
            </div>
            <div v-else>
                <div class="cart-item" v-for="item in cart" :key="item.id">
                    <h3>{{ item.name }}</h3>
                    <p>样式: {{ item.selectedStyle }}, 颜色: {{ item.selectedColor }}</p>
                    <p>价格: ¥{{ calculatePrice(item) }}</p>
                    <button class="remove-btn" @click="removeFromCart(item)">移除</button>
                </div>
                <div class="cart-summary">
                    <h3>总价: ¥{{ totalPrice }}</h3>
                    <button class="checkout-btn" @click="checkout">下单</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'CartSection',
    data() {
        return {
            cart: []
        };
    },
    computed: {
        totalPrice() {
            return this.cart.reduce((total, item) => total + this.calculatePrice(item), 0);
        }
    },
    methods: {
        calculatePrice(item) {
            return item.price;
        },
        removeFromCart(item) {
            const index = this.cart.indexOf(item);
            if (index > -1) {
                this.cart.splice(index, 1);
            }
        },
        checkout() {
            alert('订单已提交！');
            this.cart = [];
        }
    }
};
</script>

<style scoped>
/* 可以在这里添加特定于 CartSection 的样式 */
</style>