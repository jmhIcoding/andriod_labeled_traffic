__author__ = 'jmh081701'
#安卓远程控制的基础类
from copy import  deepcopy
from appium import  webdriver
from  appium.webdriver.common.touch_action import TouchAction
import time
from  config import desired_launch_caps_template
from  PressEvent import  keycode
class automation_util:
    def __init__(self,package,activity,time_interval =0.1,url='http://localhost:4723/wd/hub'):
        self.desired_caps = deepcopy(desired_launch_caps_template)
        self.desired_caps['appPackage'] = package
        self.desired_caps['appActivity'] = activity
        self.driver = webdriver.Remote(url,self.desired_caps)
        self.time_interval = time_interval
        self.last_element = None
    def by_id(self,id):
        el = self.driver.find_elements_by_id(id)
        time.sleep(self.time_interval)
        if len(el)!= 1:
            self.last_element = None
            raise Exception("elements with id=%s exists %d entities"%(id,len(el)))

        self.last_element = el[0]
        return el[0]

    def by_xpath(self,xpath):
        el = self.driver.find_elements_by_xpath(xpath)
        time.sleep(self.time_interval)
        if len(el)!=1:
            self.last_element =None
            raise Exception("elements with id=%s exists %d entities"%(xpath,len(el)))
        self.last_element = el[0]
        return el[0]

    def click(self,el=None,count=1,duration=None):
        time.sleep(self.time_interval)
        if el==None:
            el = self.last_element
        for i in range(count):
            el.click()
            if duration:
                time.sleep(duration)

    def sendkeys(self,el,text,duration=0.1):
        time.sleep(self.time_interval)

    def press_search(self):
        self.driver.tap([(1000,1850)])
        time.sleep(self.time_interval)
    def scroll_down(self):
        actions = TouchAction(self.driver)
        actions.press(x=560,y=300)
        actions.move_to(x=560,y=1600)
        actions.release()
    def scroll_up(self):
        actions = TouchAction(self.driver)
        actions.press(x=560,y=1600)
        actions.move_to(x=560,y=300)
        actions.release()
    def click(self,x,y,count=2):
        while count>0:
            print("【click】")
            self.driver.tap(positions=[(x,y)])
            time.sleep(self.time_interval)
            count -=1
    def press(self,text):
        text = text.upper()
        for each in text:
            self.driver.press_keycode(keycode.get(each,62))
            time.sleep(self.time_interval*0.1)

'''
各个App控制的基类
需要实现 run(start_time,duration)虚函数
表述从start_time开始执行，持续时间为duration
'''
class app_control:
    def __init__(self,package,activity,time_interval =0.1,url='http://localhost:4723/wd/hub'):
        self.app = automation_util(package,activity,time_interval,url)

    def run(self,start_time,duration):
        pass
