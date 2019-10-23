__author__ = 'jmh081701'
import copy
desired_launch_caps_template ={}
desired_launch_caps_template['platformName'] = 'Android'
desired_launch_caps_template['platformVersion'] = '8.0.0'
desired_launch_caps_template['deviceName'] = '8346fafe'          #目标机子的name,这个name通过adb devices 来获取
desired_launch_caps_template['appPackage'] = 'com.kingsoft'     #目标应用的包名
desired_launch_caps_template['appActivity']='.Main'             #目标应用的目标activity, package和activity可以通过 top_activity.py获取
desired_launch_caps_template['noReset']=True                    #不会重置app,不会删除app的数据
desired_launch_caps_template['newCommandTimeout']=60000          #设置超时时间为 60000s ,永不超时

desired_wait_caps_template={}
desired_wait_caps_template['platformName'] = 'Android'
desired_wait_caps_template['platformVersion'] = '8.0.0'
desired_wait_caps_template['deviceName'] = '8346fafe'          #目标机子的name,这个name通过adb devices 来获取
desired_wait_caps_template['appWaitPackage'] = 'com.kingsoft'     #目标应用的包名
desired_wait_caps_template['appWaitActivity']='.Main'             #目标应用的目标activity, package和activity可以通过 top_activity.py获取
desired_wait_caps_template['noReset']=True                    #不会重置app,不会删除app的数据
desired_wait_caps_template['newCommandTimeout']=60000          #设置超时时间为 60000s ,永不超时