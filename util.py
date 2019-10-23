__author__ = 'jmh081701'
#安卓远程控制的基础类
from copy import  deepcopy
from appium import  webdriver
import time
from  config import desired_launch_caps_template
class automation_util:
    def __init__(self,package,activity,time_interval =0.1,url='http://localhost:4723/wd/hub'):
        self.desired_caps = deepcopy(desired_launch_caps_template)
        self.desired_caps['appPackage'] = package
        self.desired_caps['appActivity'] = activity
        self.driver = webdriver.Remote(url,self.desired_caps)
        self.time_interval = time_interval

    def by_id(self,id):
        el = self.driver.find_elements_by_id(id)
        time.sleep(self.time_interval)
        if len(el)!= 0:
            raise Exception("elements with id=%s exists %d entities"%(id,len(el)))
        return el[0]

    def by_xpath(self,xpath):
        el = self.driver.find_elements_by_xpath(xpath)
        time.sleep(self.time_interval)
        if len(el)!=0:
            raise Exception("elements with id=%s exists %d entities"%(xpath,len(el)))
        return el[0]

    def click(self,el,count=1,duration=None):
        time.sleep(self.time_interval)

    def sendkeys(self,el,text,duration=0.1):
        time.sleep(self.time_interval)

    def press_search(self):
        self.driver.tap([(1000,1850)])
        time.sleep(self.time_interval)