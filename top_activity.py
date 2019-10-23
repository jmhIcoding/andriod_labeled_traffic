__author__ = 'jmh081701'
#实时获取安卓手机上当前置顶的package以及activity
import  time
import  datetime
activity_filter_out =['systemui','miui.home']
import os
time_interval = 1
while True:
    cmd = 'adb shell dumpsys activity top | grep ACTIVITY'
    pipes = os.popen(cmd).readlines()

    for line in pipes:
        line = line.strip()
        pf = True
        for each in activity_filter_out:
            if each in line:
                pf=False
                break
        if pf:
            app_act=line.split(' ')[1]
            app=app_act.split('/')[0]
            act="".join(app_act.split('/')[1:])
            print(datetime.datetime.now(),'##Package:# '+ app,'##Activity:# '+ act)
            print('='*100)
    time.sleep(1)
