### 客户端已知bug&&需求
[x] bug 1 搜索了新城市 但是点击的是旧城市 稳定crash 可以考虑把旧城市隐藏

[x] bug 2 键盘上移 挡住了

[x] bug 3 编辑状态 不能点击搜索城市

[x] bug 4 有些时候 就没有图片了… 同bug 9 数据问题：

[x] bug 5 大理的PM2.5为啥是-1

[x] bug 6 拿天气的时候 不要拿weather了 太SB了 那预测天气的weather吧

[x] bug 6 唐山市 应该选唐山

[x] 需求 1 做一个一天24小时的aqi折线图 用https://github.com/danielgindi/Charts来实现 

[x] 需求 2 如果数据是0或者-1 显示什么呢？

[x] 需求 3 获取定位之前 都给我加.progess

[x] bug 7 编辑的时候，直接退出了，并没有保存现在的城市

[x] bug 8 最上面的cell1 没有风速

[x] bug 9 发现一个bug 就是搜索凤台 可能因为凤台没有pm2.5 再选择北京之后，凤台的天气和温度和风速没有显示
CommonTool.loadData 的时候，首页凤台没有读取出来 但是第二页凤台读出来了，不知道为什么
知道了 因为凤台是才加进去的 首页没有loadData了 还是原来的Data

[x] bug 10 语言为英语 没有数据啊

[x] bug 11 每次进入都刷新两次 修改了策略，进入后台2个小时后刷新

[x] bug 12 选择城市 出现约束问题 异常

[x] bug 13 增加单位，说明页面μg/m³

[x] bug 14 增加说明页 说明各种参数

[ ] 需求 4 周末把push推送调通吧 可以用leancloud 或者 友盟（暂时废弃）

[ ] bug 15网络差的时候 进度条一直在读取  ??? 没有得到数据 加一个 delay? 取消？

[x] bug 16关掉加载的图片

[x] bug 17看看gjthub上有没有取消刷新

[ ] bug 18 fir上面的图 需要更新

[ ] 需求 5 增加一个预测功能 未来的aqi

[x] bug 19 没有获得数据的时候 分享按钮出错

[x] 需求 6 分享的图片颜色不对…

[ ] bug 20 减少文字阅读

[x] bug 21下方增加文字说明（未来7天天气）

[ ] bug 25天气详情别都用白色
