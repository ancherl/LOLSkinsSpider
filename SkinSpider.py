# 1. 爬取LOL所有英雄及其皮肤
# 2. 保存爬取的皮肤到本地文件夹, 并按英雄名分类

# 经过分析， 发现以下特征
# 1. LOL英雄的信息是通过懒加载技术完成的， 不在HTML文本里面
# 2. 经分析， 确定LOL官网是通过/index.js?v=20181228发送的javascript 请求
# 3. 在上诉javascript 文本中，通过 apiUrl: '//game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=' ajax 发送的request
# 4. 确定我们的实际请求url 应为 https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js

# 皮肤的获取　
# 经分析， 皮肤的加载也是通过发送javascript 请求， 返回json 数据， 然后填充html页面
# 发送请求的位置在/info-defail.shtml?id=1 模版中，其中id是hero id (从上诉request请求中获取)
# 通过//game.gtimg.cn/images/lol/act/img/js/hero/1.js' 发送请求获取英雄详细数据， 包括皮肤. 数字1, 需要替换为相应的hero id

import requests

import json

import os

import re

# 指定爬取的主页面
baseUrl = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

# 指定保存的基础路径
basePath = '/Users/daixin/Desktop/LOL'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# 主要获取英雄详细信息, 包含皮肤信息
def pull_hero_detail(heroId):
    baseUrl1 = 'https://game.gtimg.cn/images/lol/act/img/js/hero/' + heroId + '.js'

    res1 = requests.request('GET', baseUrl1, headers=headers)

    hero_detail_info = json.loads(res1.text)

    skin_info(hero_detail_info)

# 单独处理皮肤信息
def skin_info(skin_data):
    for skin in skin_data.get('skins'):
        skin_id = skin.get('skinId')
        mainImg = skin.get('mainImg')
        skin_name = skin.get('name')
        hero_name = skin.get('heroName')
        # print('Hero Name: ' + hero_name + ', ' + 'Skin Name: ' + skin_name + ', ' + 'Image Url: ' + mainImg)

        print('extract......' + hero_name + ', ' + skin_name + ', ' + skin_id)

        if mainImg:
            # 发送请求获取图片二进制信息
            img_response = requests.get(mainImg, headers=headers)

            # 判断英雄名文件夹是否存在
            if os.path.isdir(basePath+'/'+hero_name) == False:
                os.makedirs(basePath+'/'+hero_name)
            with open(basePath+'/'+hero_name+'/'+skin_name.replace('/','') +'.jpg', 'wb') as f:
                f.write(img_response.content)

# 发送请求获取json数据
res = requests.request('GET', baseUrl, headers=headers)

hero_data = json.loads(res.text)

print('爬虫开始......')

for hero in hero_data.get('hero'):
    hero_id = hero.get('heroId')
    pull_hero_detail(hero_id)

print('爬虫结束......')


