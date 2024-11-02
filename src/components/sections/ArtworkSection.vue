<template>
    <section id="artwork" class="section">
        <h2>艺术呈现</h2>
        <div class="art-categories" data-aos="fade-up">
            <div class="category-tabs">
                <button class="tab-btn active">叶雕艺术</button>
                <button class="tab-btn">立体纸雕</button>
                <button class="tab-btn">传统剪纸</button>
            </div>
            <div class="art-grid">
                <div class="art-item">
                    <div class="art-content">
                        <h3>平遥古城印象</h3>
                        <p class="art-description">以叶脉勾勒古城轮廓，展现千年古城的沧桑与底蕴。</p>
                        <div class="art-tags">
                            <span class="tag">叶雕</span>
                            <span class="tag">建筑</span>
                            <span class="tag">文化</span>
                        </div>
                    </div>
                </div>
                <!-- 更多艺术作品... -->
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'ArtworkSection'
};
</script>

<style scoped>
/* 可以在这里添加特定于 ArtworkSection 的样式 */
</style>