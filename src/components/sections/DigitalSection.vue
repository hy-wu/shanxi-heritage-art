<template>
  <section id="digital" class="section">
    <h2>数字展馆</h2>
    <div class="product-showcase" data-aos="fade-up">
      <div class="product-grid">
        <div class="product-card" v-for="product in products" :key="product.id">
          <img :src="product.image" :alt="product.name">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <div class="product-options">
            <label>样式:
              <select v-model="product.selectedStyle">
                <option v-for="style in product.styles" :key="style" :value="style">{{ style }}</option>
              </select>
            </label>
            <label>颜色:
              <select v-model="product.selectedColor">
                <option v-for="color in product.colors" :key="color" :value="color">{{ color }}</option>
              </select>
            </label>
          </div>
          <p>价格: ¥{{ calculatePrice(product) }}</p>
          <button class="add-to-cart-btn" @click="addToCart(product)">加入购物车</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'DigitalSection',
  data() {
    return {
      products: [
        // 示例产品数据
        {
          id: 1,
          name: '叶雕艺术',
          image: 'images/leaf-art.jpg',
          description: '精美的叶雕艺术品，展现自然之美。',
          styles: ['简约', '复古', '现代'],
          colors: ['红色', '绿色', '蓝色'],
          basePrice: 100,
          selectedStyle: '简约',
          selectedColor: '红色'
        },
        {
          id: 2,
          name: '立体纸雕',
          image: 'images/paper-art.jpg',
          description: '立体纸雕，层次分明，栩栩如生。',
          styles: ['传统', '现代'],
          colors: ['白色', '黑色'],
          basePrice: 150,
          selectedStyle: '传统',
          selectedColor: '白色'
        },
        {
          id: 3,
          name: '传统剪纸',
          image: 'images/cut-paper.jpg',
          description: '传统剪纸，手工艺的精华。',
          styles: ['经典', '创新'],
          colors: ['红色', '黄色'],
          basePrice: 80,
          selectedStyle: '经典',
          selectedColor: '红色'
        }
        // 可以添加更多产品
      ]
    };
  },
  methods: {
    calculatePrice(product) {
      return product.basePrice;
    },
    addToCart(product) {
      // 假设有一个全局的购物车对象
      this.$emit('add-to-cart', product);
    }
  }
};
</script>

<style scoped>
/* 可以在这里添加特定于 DigitalSection 的样式 */
</style>