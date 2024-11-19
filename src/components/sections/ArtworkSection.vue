<template>
    <section id="artwork" class="section">
        <h2>艺术呈现</h2>
        <div class="art-categories" :key="categoriesKey" data-aos="fade-up">
            <div class="category-tabs">
                <button v-for="category in categories" :key="category" :class="getClass(category)" @click="toggleCategory(category)">{{ category }}</button>
            </div>
            <div class="art-grid">
                <div class="art-item" v-for="artwork in filteredArtworks" :key="artwork.id">
                    <img :src="artwork.image" :alt="artwork.name">
                    <h3>{{ artwork.name }}</h3>
                    <p>{{ artwork.description }}</p>
                    <div class="art-tags">
                        <span v-for="tag in artwork.tags" :key="tag" class="tag">{{ tag }}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'ArtworkSection',
    data() {
        return {
            categoriesKey: 0,
            categories: ['全部', '叶雕艺术', '立体纸雕', '传统剪纸'],
            activeCategories: ['全部', '叶雕艺术', '立体纸雕', '传统剪纸'],
            activeAllCategories: true,
            artworks: [
                // 示例艺术作品数据
                {
                    id: 1,
                    name: '平遥古城印象',
                    image: null,
                    description: '以叶脉勾勒古城轮廓，展现千年古城的沧桑与底蕴。',
                    tags: ['叶雕', '建筑', '文化'],
                    category: '叶雕艺术'
                },
                {
                    id: 2,
                    name: '太原城市风光',
                    image: null,
                    description: '以立体纸雕形式展现太原市的城市风光，展现现代城市的繁华与活力。',
                    tags: ['立体纸雕', '城市', '风光'],
                    category: '立体纸雕'
                },
                {
                    id: 3,
                    name: '传统剪纸艺术',
                    image: null,
                    description: '传统剪纸艺术，展现中国传统文化的独特魅力。',
                    tags: ['剪纸', '传统', '文化'],
                    category: '传统剪纸'
                }
            ]
        };
    },
    async created() {
        for (const artwork of this.artworks) {
            const image = await import(`@/assets/images/${artwork.name}.png`);
            artwork.image = image.default;
        }
    },
    computed: {
        filteredArtworks() {
            return this.artworks.filter(artwork => this.activeCategories.includes(artwork.category));
        }
    },
    methods: {
        toggleCategory(category) {
            if (this.activeCategories.includes(category)) {
                this.activeCategories = this.activeCategories.filter((c) => c !== category && c !== '全部');
                this.activeAllCategories = false;
                this.categoriesKey++;
            } else {
                this.activeCategories.push(category);
            }
            if (category === '全部') {
                if (this.activeAllCategories) {
                    this.activeAllCategories = false;
                } else {
                    this.activeCategories = this.categories;
                    this.activeAllCategories = true;
                    this.categoriesKey++;
                }
            }
        },
        getClass(category) {
            return this.activeCategories.includes(category) ? 'tab-btn active' : 'tab-btn';
        }
    }
};
</script>

<style scoped>
/* 可以在这里添加特定于 ArtworkSection 的样式 */
</style>