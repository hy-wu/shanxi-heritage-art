# 本地构建推送到远程仓库gh-pages分支
import os
os.system('npm run build')
os.chdir('dist')
print(os.getcwd())
os.system('git init')
os.system('git add -A')
os.system('git commit -m "deploy"')
os.system('git push -f git@github.com:hy-wu/shanxi-heritage-art.git main:gh-pages')
os.chdir('..')
