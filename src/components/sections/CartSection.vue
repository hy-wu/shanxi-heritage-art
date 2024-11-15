<template>
    <section id="cart" class="section">
        <h2>购物车</h2>
        <div class="cart-container" data-aos="fade-up">
            <div v-if="cart.length === 0">
                <p>您的购物车是空的。</p>
            </div>
            <div v-else>
                <div class="cart-item" v-for="item in cart" :key="item.id">
                    <img :src="item.image" :alt="item.name">
                    <h3>{{ item.name }}</h3>
                    <p>样式: <span style="font-family: 'Microsoft YaHei', sans-serif;">{{ item.selectedStyle }}</span>, 颜色: <span style="font-family: 'Microsoft YaHei', sans-serif;">{{ item.selectedColor }}</span></p>
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
    props: {
        cart: {
            type: Array,
            required: true
        }
    },
    computed: {
        totalPrice() {
            return this.cart.reduce((total, item) => total + this.calculatePrice(item), 0);
        }
    },
    methods: {
        calculatePrice(item) {
            return item.basePrice;
        },
        removeFromCart(item) {
            this.$emit('remove-from-cart', item);
        },
        checkout() {
            alert('订单已提交！');
            this.$emit('checkout');
        }
    }
};
</script>

<style scoped>
.section {
    padding: 20px;
}

.cart-container {
    font-family: "STKaiti", "华文楷体", serif;
}

.cart-item {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #ccc;
    padding: 10px 0;
}

.cart-item img {
    width: 50px;
    height: 50px;
    margin-right: 10px;
}

.cart-item h3 {
    margin: 0;
    font-size: 1.2rem;
}

.cart-item p {
    margin: 0;
    font-size: 1rem;
}

.cart-summary {
    margin-top: 20px;
}

.remove-btn, .checkout-btn {
    margin-top: 10px;
    padding: 5px 10px;
    background-color: #f44336;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.checkout-btn {
    background-color: #4CAF50;
}
</style>