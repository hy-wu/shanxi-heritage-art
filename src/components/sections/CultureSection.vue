<template>
    <section id="culture" class="section">
        <h2>文化传承</h2>
        <div class="culture-content" data-aos="fade-up">
            <div class="timeline">
                <div class="timeline-item" v-for="(item, index) in timelineItems" :key="index">
                    <div class="timeline-time">{{ item.time }}</div>
                    <div class="timeline-content">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.description }}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'CultureSection',
    data() {
        return {
            "timelineItems": [
                {
                    "time": "先秦",
                    "title": "建筑雏形与技术初现",
                    "description": "山西在旧石器时代有原始人类居住洞穴，新石器时代可能有类似周边地区的聚居形式。河南偃师二里头宫殿遗址应用的夯土技术或影响山西，为建筑发展奠定基础，当时已现建筑雏形及聚落形态，夯土技术开始应用于建筑相关部分。"
                },
                {
                    "time": "秦汉",
                    "title": "砖瓦与瓦当艺术发展及建筑初兴",
                    "description": "秦代砖瓦烧制使用更普遍，虽山西境内秦代建筑实物少，但为汉代奠定基础。汉代是瓦当艺术鼎盛期，山西地区瓦当题材多样，城市与宫殿建筑也有一定规模发展，如大同在汉代作为重要区域应有相关建筑，虽留存遗址少，但可推测规模布局。"
                },
                {
                    "time": "魏晋",
                    "title": "佛教建筑兴起与风格融合创新",
                    "description": "魏晋时佛教在山西广泛传播，云冈石窟是杰出代表，始建于北魏，依山而凿、规模宏大、雕刻精美。此时期建筑风格融合不同民族元素，在传统汉族建筑基础上吸收少数民族装饰风格等，结构与空间处理也有创新，为隋唐繁荣奠基。"
                },
                {
                    "time": "唐",
                    "title": "建筑艺术的鼎盛时期",
                    "description": "山西在唐代时建筑艺术达到鼎盛，现存有多座极具价值的唐代木构建筑，如佛光寺东大殿，其斗拱、梁架和藻井等展现了晚唐时期的建筑风格，且大殿梁底有‘唐大中十一年’的铭文；南禅寺是中国现存最古老的木构建筑；广仁王庙也是大唐盛世辉煌的见证，这些建筑共同构成了山西唐代建筑艺术的独特风格和深厚底蕴."
                },
                {
                    "time": "宋",
                    "title": "建筑艺术的传承与发展",
                    "description": "山西宋代建筑保有量居全国前列，建筑风格在继承唐代的基础上有所发展，具有鲜明的地域特色。例如晋城二仙庙，创建于宋绍圣四年（1079年），其殿内保存有木雕‘天寓壁藏’楼阁式神龛等罕见的宋代小木作实物及宋代彩塑。其建筑特征如减柱布列的形式、梁架结构、铺作等方面既反映了宋《营造法式》中的布局，又体现了晋东南地区的区域特色."
                },
                {
                    "time": "元",
                    "title": "建筑结构与力学的革新尝试",
                    "description": "元代的山西建筑在继承宋金的基础上进行了大胆革新。一方面有像永乐宫这样选材规整、制作规矩的官式建筑代表，其营建历程漫长，无极门梁枋用材合乎《营造法式》六等材，梁架结构延续金代形制且简练经济；另一方面有洪洞广胜下寺大雄宝殿等选材自然、制作粗糙的民间建筑典范，用材减小，移柱、减柱造并用，构造灵活大胆，独具创新。同时，元代斗拱继承宋制并有所发展，梁枋加工粗糙，斜栿使用普遍."
                },
                {
                    "time": "明",
                    "title": "建筑风格的融合与丰富",
                    "description": "明代山西建筑风格呈现出融合与丰富的特点，如大同的慈云寺，始建于唐，历经修缮至明代，承载着元明风骨，其三进院落错落有致，精致砖雕与琉璃浮雕屋脊巧夺天工，穹庐顶式的钟鼓二楼是山西现存明清钟鼓楼中的孤例，融合了元代建筑风格与北疆民族文化，体现了多元文化的交融."
                },
                {
                    "time": "清",
                    "title": "传统建筑技艺的延续与传承",
                    "description": "清代山西建筑延续了传统的建筑技艺，并在细节和装饰上进一步发展。许多建筑在保留传统木结构和布局的基础上，更加注重雕刻、彩绘等装饰工艺，使建筑更加华丽精美，体现了当时的社会文化和审美情趣，同时也反映了传统建筑技艺的传承和延续。"
                }
            ]
        };
    }
};
</script>

<style scoped>
.section {
    padding: 20px;
}

.culture-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.timeline {
    position: relative;
    padding: 20px 0;
    width: 100%;
}

.timeline::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 2px;
    background: #ccc;
}

.timeline-item {
    position: relative;
    width: 50%;
    padding: 10px 20px;
    box-sizing: border-box;
    margin-bottom: -4rem;
}

.timeline-item:nth-child(odd) {
    left: 0;
}

.timeline-item:nth-child(even) {
    left: 50%;
}

.timeline-time {
    font-weight: bold;
    margin-bottom: 5px;
}

.timeline-content {
    background: #fff;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}
</style>