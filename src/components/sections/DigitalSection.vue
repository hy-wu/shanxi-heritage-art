<template>
  <section id="digital" class="section">
    <h2>数字展馆</h2>
    <div class="product-showcase" data-aos="fade-up">
      <div class="product-scroll-container">
        <div class="product-card" v-for="product in products" :key="product.id">
          <img :src="product.image" :alt="product.name">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <div class="product-options">
            <label>样式:
              <select v-model="product.selectedStyle" class="custom-select">
                <option v-for="style in product.styles" :key="style" :value="style">{{ style }}</option>
              </select>
            </label>
            <span style="margin-right: 20px;"></span>
            <label>颜色:
              <select v-model="product.selectedColor" class="custom-select">
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
          image: null,
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
          image: null,
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
          image: null,
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
  async created() {
    this.products[0].image = (await import('../../assets/images/leaf-art.png')).default;
    this.products[1].image = (await import('../../assets/images/paper-art.png')).default;
    this.products[2].image = (await import('../../assets/images/traditional-cut.png')).default;
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
.product-showcase {
  font-family: "STKaiti", "华文楷体", serif;
  overflow-x: auto;
  white-space: nowrap;
}

.product-scroll-container {
  display: flex;
  flex-wrap: nowrap;
}

.product-card {
  display: inline-block;
  width: 300px;
  margin-right: 20px;
  white-space: normal;
  border: 1px solid #ccc;
  padding: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.model-viewer img {
    width: 100%;
    height: auto;
}

</style>