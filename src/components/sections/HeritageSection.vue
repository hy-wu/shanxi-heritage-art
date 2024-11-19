<template>
    <section id="heritage" class="section">
        <h2>非遗建筑</h2>
        <div class="heritage-showcase" data-aos="fade-up">
            <div class="heritage-filters">
                <button :class="getClass(category)" v-for="category in categories" :key="category"
                        @click="toggleCategory(category)">{{ category }}
                </button>
            </div>
            <div class="heritage-slider">
                <div class="heritage-card" v-for="building in filteredHeritageBuildings" :key="building.name">
                    <h3>{{ building.name }}</h3>
                    <div class="heritage-info">
                        <p>{{ building.description }}</p>
                        <ul class="heritage-features">
                            <li v-for="feature in building.features" :key="feature">{{ feature }}</li>
                        </ul>
                    </div>
                    <button class="learn-more-btn" @click="searchBuilding(building.name)">了解更多</button>
                </div>
                <!--                <div class="heritage-card">-->
                <!--                    <div class="card-content">-->
                <!--                        <h3>大同华严寺</h3>-->
                <!--                        <div class="heritage-info">-->
                <!--                            <p>始建于辽代，是中国现存最大的辽代寺院。</p>-->
                <!--                            <ul class="heritage-features">-->
                <!--                                <li>建筑年代：辽代</li>-->
                <!--                                <li>建筑类型：寺庙</li>-->
                <!--                                <li>保护级别：国家重点文物</li>-->
                <!--                            </ul>-->
                <!--                        </div>-->
                <!--                        <button class="learn-more-btn">了解更多</button>-->
                <!--                    </div>-->
                <!--                </div>-->
                <!-- 更多建筑卡片... -->
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'HeritageSection',
    data() {
        return {
            categoriesKey: 0,
            categories: ['全部', '寺庙建筑', '民居建筑', '园林建筑'],
            activeCategories: ['全部', '寺庙建筑', '民居建筑', '园林建筑'],
            activeAllCategories: true,
            heritageBuildings: [
                {
                    name: '大同华严寺',
                    description: '始建于辽代，是中国现存最大的辽代寺院。',
                    features: [
                        '建筑年代：辽代',
                        '建筑类型：寺庙',
                        '保护级别：国家重点文物'
                    ],
                    category: '寺庙建筑'
                },
                {
                    name: '平遥古城',
                    description: '中国现存最完整的古城之一，是中国四大古城之一。',
                    features: [
                        '建筑年代：明清',
                        '建筑类型：民居',
                        '保护级别：世界文化遗产'
                    ],
                    category: '民居建筑'
                },
                {
                    name: '晋祠',
                    description: '中国现存最早的皇家祭祀园林。',
                    features: [
                        '建筑年代：西周',
                        '建筑类型：园林博物馆',
                        '保护级别：国家重点文物'
                    ],
                    category: '园林建筑'
                }
            ]
        };
    },
    computed: {
        filteredHeritageBuildings() {
            return this.heritageBuildings.filter(building => this.activeCategories.includes(building.category));
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
            return this.activeCategories.includes(category) ? 'filter-btn active' : 'filter-btn';
        },
        searchBuilding(buildingName) {
            const query = encodeURIComponent(buildingName);
            const url = `https://www.baidu.com/s?wd=${query}`;
            window.open(url, '_blank');
        }
    }
};
</script>

<style scoped>
/* 可以在这里添加特定于 HeritageSection 的样式 */
</style>