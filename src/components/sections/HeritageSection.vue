<template>
    <section id="heritage" class="section">
        <h2>非遗建筑</h2>
        <div class="heritage-showcase" data-aos="fade-up">
            <div class="heritage-filters">
                <button class="filter-btn active">全部</button>
                <button class="filter-btn">寺庙建筑</button>
                <button class="filter-btn">民居建筑</button>
                <button class="filter-btn">园林建筑</button>
            </div>
            <div class="heritage-grid">
                <div class="heritage-card">
                    <div class="card-content">
                        <h3>大同华严寺</h3>
                        <div class="heritage-info">
                            <p>始建于辽代，是中国现存最大的辽代寺院。</p>
                            <ul class="heritage-features">
                                <li>建筑年代：辽代</li>
                                <li>建筑类型：寺庙</li>
                                <li>保护级别：国家重点文物</li>
                            </ul>
                        </div>
                        <button class="learn-more-btn">了解更多</button>
                    </div>
                </div>
                <!-- 更多建筑卡片... -->
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'HeritageSection'
};
</script>

<style scoped>
/* 可以在这里添加特定于 HeritageSection 的样式 */
</style>