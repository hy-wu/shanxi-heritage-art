<template>
    <section id="feedback" class="section">
        <h2>交流互动</h2>
        <div class="feedback-container" data-aos="fade-up">
            <div class="feedback-form">
                <h3>分享您的想法</h3>
                <form id="feedbackForm">
                    <div class="form-group">
                        <label for="name">姓名</label>
                        <input type="text" id="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">邮箱</label>
                        <input type="email" id="email" required>
                    </div>
                    <div class="form-group">
                        <label for="category">关注领域</label>
                        <select id="category">
                            <option value="art">艺术创作</option>
                            <option value="heritage">建筑保护</option>
                            <option value="culture">文化传承</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="message">留言内容</label>
                        <textarea id="message" rows="4" required></textarea>
                    </div>
                    <button type="submit" class="submit-btn">提交反馈</button>
                </form>
            </div>
            <div class="interaction-features">
                <div class="feature-card">
                    <h3>在线讲座</h3>
                    <p>定期举办非遗文化线上讲座，专家在线答疑解惑。</p>
                    <button class="feature-btn">预约参加</button>
                </div>
                <div class="feature-card">
                    <h3>文化论坛</h3>
                    <p>加入我们的文化论坛，与其他爱好者交流讨论。</p>
                    <button class="feature-btn">立即加入</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'FeedbackSection'
};
</script>

<style scoped>
/* 可以在这里添加特定于 FeedbackSection 的样式 */
</style>