# andriod_labeled_traffic
基于Appium的安卓自动化操作代码
# 注意事项
1. 在使用find_element_by_id或by_xpath寻找元素的时候,需要使用Appium自带的Inspector工具. 效果如fig1 所示。
![fig1](https://github.com/jmhIcoding/andriod_labeled_traffic/blob/master/fig1.png) 
2. Appium的pressKeycode不能点击搜索,需要使用driver.tap()函数来模拟点击相应坐标。 其中【搜索】按钮的坐标为（1000,1850）。
# 几大类App,按照大类来分
- 音乐: Spotify
1. 搜索歌曲/歌手
2. 听新音乐

- 即时通讯: Wechat
1. 发文字
2. 发图片
3. 看视频/发视频

- 社交:Tiktok 抖音 
1. 看视频

- 新闻类 News Breaks: Local & Break
1. 看新闻

- 地图类 Google Map 
1. 找地名,放大图
2. 找路径规划
3. 滑动地图

# 流量的纯净性
使用Shadowsocks的绕过功能,设置只有特定的APP可以走代理。
同时设置这些APP不会在后台运行。

在172.16.30.180主机上抓取数据包。其中lo上的socks流量存在 offload的问题，包的大小可能会超出1500。

172.16.30.180 搭建了ssserver,开放6768端口。
移动端使用shadowsock客户端连接172.16.30.180:6768,同时打开只有特定应用才走VPN的设置。

172.16.30.180 使用ssh -D 127.0.0.1:1080 开启ssh隧道。

172.16.30.180 使用proxychains ssserver -c *.json 来把移动端过来的流量全部导入到ssh隧道上面去。

于是在172.16.30.180 监听 lo网卡流量可以拿到纯净的明文流量，而172.16.30.180的出口流量可以拿到ssh隧道加密后的流量。
