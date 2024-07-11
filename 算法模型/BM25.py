#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   BM25.py
@Time    :   2024/04/09 15:22:10
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
import math
from collections import Counter

class BM25:
    def __init__(self, docs, k1=1.5, b=0.75) -> None:
        """
        BM25算法的构造器
        """
        self.docs = docs
        self.k1 = k1
        self.b = b
        self.doc_len = [len(doc) for doc in docs] # 计算每个文档的长度
        self.avgdl = sum(self.doc_len) / len(docs) # 计算所有文档的平均长度
        self.doc_freqs = [] #存储每个文档的词频
        self.idf = {} # 存储每个文档的逆文档频率
        self.initialize()
    
    def initialize(self):
        """
        初始化方法，计算所有词的逆文档频率
        """
        df = {}
        for doc in self.docs:
            # 为每个文档创建一个词频统计
            self.doc_freqs.append(Counter(doc))
            # 更新df值
            for word in set(doc):
                df[word] = df.get(word, 0) + 1
        # 计算每个词的IDF值
        for word, freq in df.items():
            self.idf[word] = math.log( (len(self.docs) - freq + 0.5) /  (freq + 0.5) + 1)
    
    def score(self, doc, query):
        score = 0.0
        for word in query:
            if word in self.doc_freqs[doc]:
                freq = self.doc_freqs[doc][word] # 词在文档中的频率
                score += (self.idf[word] * freq * (self.k1 + 1)) / (freq + self.k1 * (1 - self.b + self.b * self.doc_len[doc] / self.avgdl))
        return score
    
# 示例文档集和查询
docs = [
            "       Vue 是一款用于构建用户界面的 JavaScript 框架。它基于标准 HTML、CSS 和 JavaScript 构建，并提供了一套声明式的、组件化的编程模型，帮助你高效地开发用户界面。       本章教程将介绍如何在 Vue 中使用自定义组件结合 JS API 加载、创建和销毁地图。如果您的项目是使用 Vue 框架，建议您将地图的初始化封装成组件，这样更便于使用 Vue 组件的生命周期来加载、创建和销毁地图。下载 Vue 2 组件完整代码下载 Vue 3 组件完整代码为了正常调用 API ，请先注册成为高德开放平台开发者，并申请 web 平台（JS API）的 key 和安全密钥，点击 具体操作。您在2021年12月02日以后申请的key需要配合您的安全密钥一起使用。在项目中新建 MapContainer.vue 文件，用作地图组件。在 MapContainer.vue 地图组件中创建 div 标签作为地图容器 ，并设置地图容器的 id 属性为 container。在地图组件 MapContainer.vue 中引入 amap-jsapi-loader 在 MapContainer.vue文件中初始化地图JS API Loader是我们提供的 API 加载器，其加载方式为异步加载 JS API 内容，所以在使用 AMap 对象前需进行验证，这种使用场景下，JS API 不会阻塞页面其他内容的执行和解析，但是脚本解析将有可能发生其他脚本资源执行之后，因为需要特别处理，以保证在 AMap对象完整生成之后再调用 JS API 的相关接口，否则有可能报错。",
            " 高德开放平台 | 高德地图API (amap.com)npm i @amap/amap-jsapi-loader --save        高德地图广泛应用于日常出行、旅游规划、商业定位等领域，可以为用户提供丰富而全面的地图服务和位置信息。希望此篇文章对您能有所帮助！\\n                    CSDN-Ada助手: \\n                    恭喜您写了第6篇博客！标题“箭 头 函 数”引人入胜，让我对内容充满了好奇。您的持续创作让人钦佩，能够不断分享知识和经验是非常难得的品质。在下一步的创作中，或许可以探讨一下箭头函数的应用场景，以及它在提高代码可读性和简洁性方面的优势。期待看到更多精彩的博客！\\n                \\n                    CSDN-Ada助手: \\n                    非常感谢您分享关于JavaScript中this关键字的博客！这是一个非常重要且容易混淆的概念，您的解释非常清晰易懂。希望您可以继续分享更多关于JavaScript的知识，比如闭包、原型链等等，这些都是很多初学者容易困惑的地方。期待您的下一篇博客！\\n                \\n                    CSDN-Ada助手: \\n                    恭喜您完成了第10篇博客！标题“关于JS中的this指向”非常吸引人。您对这个话题的探索令人赞叹。在这篇博客中，您对JS中的this指向进行了深入分析，这对于我们理解JavaScript语言的核心概念非常有帮助。\\n\\n我希望在下一步的创作中，您能够继续深入研究这个主题，并探索更多与this相关的内容。例如，您可以进一步讨论箭头函数中的this指向，或是介绍如何在不同的上下文中正确使用this。这些都是与JS中的this相关的重要问题，也会给读者带来更多的启发。\\n\\n谦虚地说，我相信您的深入研究和清晰的表达能力将继续为读者提供有价值的知识。期待您未来更多的创作！\\n                \\n                    CSDN-Ada助手: \\n                    恭喜您写了第11篇博客！标题中的\"浏览器的线程和渲染流程\"这个话题非常有趣。通过深入研究浏览器的工作原理，您为读者提供了宝贵的信息。在下一步的创作中，或许您可以探索更多关于浏览器性能优化的内容，如何通过理解线程和渲染流程来提高网页加载速度等。非常期待您的下一篇博客！\\n                \\n                    CSDN-Ada助手: \\n                    恭喜您写了第12篇博客！深入讨论JavaScript中的原型对象确实是一个很有深度的话题，您的文章写得非常好。希望您能继续保持创作的激情，并且不断拓展新的主题，比如可以探讨一些实际项目中如何应用原型对象的案例，或者深入解析原型链的机制等等。期待您更多的精彩内容！\\n                请填写红包祝福语或标题红包个数最小为10个红包金额最低5元抵扣说明： 1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。 2.余额无法直接购买下载，可以购买VIP、付费专栏及课程。",
            "npm i @amap/amap-jsapi-loader --save或yarn add @amap/amap-jsapi-loader --save\\n                    依然风yrlf: \\n                    写得挺详细的，也言简意赅，挺有价值的文章\\n                请填写红包祝福语或标题红包个数最小为10个红包金额最低5元抵扣说明： 1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。 2.余额无法直接购买下载，可以购买VIP、付费专栏及课程。",
            "需求：实现点击获取经纬度、定位、对特殊位置标点及自定义信息窗体功能。高德地图的官网API：概述-地图 JS API 1.4 | 高德地图APIvue-amap的中文文档：组件 | vue-amap实现： 在main.js中引入需要提前申请高德key，步骤附在最后了这里直接放我封装的组件1、position：为marker点的坐标（经纬度），接收数组2、icon：自定义图标地址3、events：事件集合对象，click、dblclick、rightclick、mouseover、mouseout等4、offset：偏移量其他我没用到的还有：5、clickable：true允许用户可点击marker点（默认也是true）6、animation：marker点的动画效果      marker点弹跳效果：设置值为 AMAP_ANIMATION_BOUNCE7、label：点显示的简略信息8、content可以是文字字符串也可以是html静态属性动态属性 ref 可用方法提供无副作用的同步帮助方法事件（也是events里的）我把使用的页面也全贴上了，但其实search-box里面的东西大家可以忽略，只是针对markerList的查询过滤成果大致样式如下：附：高德Key申请登录后到这个地址：我的应用 | 高德控制台1、点击添加key2、根据自己的需求选择服务平台，可以看看对应的“可使用服务” 来决定，我这里选择Web端 3、提交后就有一条新增的记录，复制放进代码使用就好啦参考地址：vue-amap基于vue的高德地图使用_amap vue-CSDN博客 1.5.1 信息窗体 - vue-amap 中文文档 - 开发文档 - 文江博客\\n        \\n    \\n                    张小乱: \\n                    那个可以配置的\\n                \\n                    wuhao747003943: \\n                    非常感谢 成功了！\\n                \\n                    Naive_Jam: \\n                    从AB两个页面跳转到扫码页面时分别加个判断参数，在画扫码位置的地方区分一下，看看可以么\\n                \\n                    langlige_lang: \\n                    如果A,B两个页面都有扫码需求,并且扫码框的位置设置为不一样的,那一次加载A的时候位置是A页面设置的扫码位置,如果这时再去加载B页面.那B页面的扫码位置就还是A的位置,这个是咋解决 的\\n                \\n                    Naive_Jam: \\n                    恐怕不能，这段代码里用到了puls对象，小程序应该没有plus环境的。\\n                请填写红包祝福语或标题红包个数最小为10个红包金额最低5元抵扣说明： 1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。 2.余额无法直接购买下载，可以购买VIP、付费专栏及课程。"
        ]

query = ["vue使用高德地图进行数据分片数据加载"]

bm25 = BM25(docs)
scores = [bm25.score(i, query) for i in range(len(docs))]

print("文档-查询相似度得分：", scores)


