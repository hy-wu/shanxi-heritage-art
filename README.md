# 山西非遗建筑艺术展

基于《黑神话：悟空》游戏元素与山西非物质文化遗产的艺术展示项目。通过叶雕、立体纸雕、剪纸等传统工艺，展现山西古建筑之美。

## 项目特点

- 融合游戏元素与传统文化
- 展示非物质文化遗产
- 数字化展示平台
- 互动式用户反馈

## 技术栈

- HTML5
- CSS3
- vue.js
- GitHub Pages

## 本地开发

1. 配置 Node.js 环境
2. 克隆仓库并进入项目目录
3. `npm install`
4. `npm run serve`
5. 在浏览器中打开终端中的 `local` 地址

### 部署到 GitHub Pages

1. 将 `deploy.py` 第9行修改为 `os.system('git push -f git@github.com:<username>/shanxi-heritage-art.git main:gh-pages')
`, 其中 `<username>` 为 GitHub 用户名 (假设配置了 GitHub SSH Key)
2. `python deploy.py` (假设安装了 Python, 否则可以逐句执行 `deploy.py` 中的命令)
3. 在项目的 `Settings` -> `Pages` -> `Build and deployment` -> `Source` 中选择 `Deploy from a branch`, 并选择 `gh-pages` 分支, `/ (root)` 目录, 点击 `Save`
4. 访问 `https://<username>.github.io/shanxi-heritage-art/`
