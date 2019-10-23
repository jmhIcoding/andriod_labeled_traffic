# andriod_labeled_traffic
基于Appium的安卓自动化操作代码
# 注意事项
1. 在使用find_element_by_id或by_xpath寻找元素的时候,需要使用Appium自带的Inspector工具. 效果如fig1 
![https://github.com/jmhIcoding/andriod_labeled_traffic/blob/master/fig1.png](fig1) 所示。
2. Appium的pressKeycode不能点击搜索,需要使用driver.tap()函数来模拟点击相应坐标。 其中【搜索】按钮的坐标为（1000,1850）。

