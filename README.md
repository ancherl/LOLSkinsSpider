# LOLSkinsSpider
徒手撸一个Spider去爬取LOL所有英雄以及皮肤， 它不香吗?爬完之后，你会有意外惊喜呦~~~

- 对于爬取LOL官网的技术难点就不说了， 属于动态爬虫的一种. HTML中不存在我们想要的东西， 它是通过懒加载技术实现的页面.
- 总的来说一下， 动态爬虫目前而言， 有哪些思路
  - 通过自动化方式模拟浏览器访问来爬取数据(Selenium)
  - 分析页面的请求结构(js)

就我个人而言， 我喜欢第二种方式，研究一下页面的懒加载， 它不香?

![代码截图](https://github.com/ancherl/LOLSkinsSpider/blob/master/images/Capture.png)
