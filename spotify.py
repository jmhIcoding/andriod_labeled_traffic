__author__ = 'jmh081701'
from util import  app_control
from  random import  randint
import  time
import  threading
import  datetime
class spotify(app_control):
    def __init__(self):
        super(spotify,self).__init__("com.spotify.music",".MainActivity")
        self.songs = []

        #载入歌曲列表
        with open("spotify_songs.txt",encoding='utf8',errors='ignore') as fp:
            lines = fp.readlines()
            for each in lines:
                each = each.strip()
                self.songs.append(each)

    '''
    搜索音乐
    '''
    def search(self):
        #点击"Seach 按钮"
        #el=self.app.by_xpath('//android.widget.ImageView[@content-desc="Search"]')
        #self.app.click(el)

            x,y = 414,1888
            self.app.click(x,y)

            #找到搜索框框

            x,y = 580,580
            self.app.click(x,y)

            keywords = self.songs[randint(0,len(self.songs)-1)]
            self.app.press(keywords)

            #点击“搜索"
            self.app.press_search()
            #等待结果
            while True:
                els=self.app.driver.find_elements_by_id("android:id/text2")
                if len(els)==0:
                    time.sleep(0.1)
                else:
                    for el in els:
                        print(el)
                        text=el.get_attribute("text")
                        if 'Song' in text:
                            el.click()
                            break
                    break
            self.app.scroll_up()
    def run(self,start_time,duration):
        now = time.time()
        time.sleep(start_time-now)
        th = threading.Thread(target=self.search)
        th.start()
        time.sleep(duration)

if __name__ == '__main__':
    spt=spotify()
    base  =  datetime.datetime(2019,10,28,11,22).timestamp()
    spt.run(base,15)