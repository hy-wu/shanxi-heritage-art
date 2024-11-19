# npm run build
# echo build
# cd dist
# echo cd_dist
# git init
# echo git_init
# git add -A
# git commit -m 'deploy'
# git push -f git@github.com:hy-wu/shanxi-heritage-art.git main:gh-pages
# cd -
import os
os.system('npm run build')
os.system('cd dist')
os.system('git init')
os.system('git add -A')
os.system('git commit -m "deploy"')
os.system('git push -f git@github.com:hy-wu/shanxi-heritage-art.git main:gh-pages')
os.system('cd -')
