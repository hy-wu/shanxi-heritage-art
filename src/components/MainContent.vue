<template>
    <main>
        <AboutSection />
        <ArtworkSection />
        <HeritageSection />
        <DigitalSection />
        <CultureSection />
        <FeedbackSection />
        <CartSection />
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
    }
};
</script>

<style scoped>
/* 可以在这里添加特定于 MainContent 的样式 */
</style>