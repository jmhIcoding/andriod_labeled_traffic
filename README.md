# andriod_labeled_traffic
基于Appium的安卓自动化操作代码
# 注意事项
1. 在使用find_element_by_id或by_xpath寻找元素的时候,需要使用Appium自带的Inspector工具. 效果如fig1 所示。
![fig1](https://github.com/jmhIcoding/andriod_labeled_traffic/blob/master/fig1.png) 
2. Appium的pressKeycode不能点击搜索,需要使用driver.tap()函数来模拟点击相应坐标。 其中【搜索】按钮的坐标为（1000,1850）。
# 几大类App,按照大类来分
- 音乐: Spotify
1. 听新音乐

- 即时通讯: Wechat
1. 文字,聊天
使用小冰机器人,可以有回复的那种

- 社交:Tiktok 抖音 
1. 看视频

- 新闻类 News Breaks: Local & Break
1. 看新闻

- 地图类 Google Map 
1. 找地名,放大图
2. 找路径规划
3. 滑动地图


