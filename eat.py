# -*- coding: utf-8 -*-
import urllib.request
import json
import time
import random


resp = urllib.request.urlopen('https://free-api.heweather.com/s6/weather/now?location=CN101031000&key=c04b75ee275846d395369743e923b8a8').read()
#将JSON转化为Python的数据结构
json_data = json.loads(resp)
city_data=json_data['HeWeather6'][0]
print(u'-------------------------啦啦啦啦会唱歌的分割线----------------------------')
print(u'天气更新时间：' + city_data['update']['loc'])
city = city_data['basic']['parent_city'] + city_data['basic']['location']
print(u'城市：' + city)
fl = city_data['now']['fl']
print(u'体感温度：' + fl)
print(u'温度：' + city_data['now']['tmp'])

resp = urllib.request.urlopen('https://free-api.heweather.com/s6/air/now?location=%E5%A4%A9%E6%B4%A5&key=c04b75ee275846d395369743e923b8a8').read()
#将JSON转化为Python的数据结构
json_data = json.loads(resp)
city_data=json_data['HeWeather6'][0]
aqi = city_data['air_now_city']['aqi']
print(u'AQI指数：' + aqi)
pm25 = city_data['air_now_city']['pm25']
print(u'PM2.5指数：' + pm25)

resp = urllib.request.urlopen('https://free-api.heweather.com/s6/weather/lifestyle?location=CN101031000&key=c04b75ee275846d395369743e923b8a8').read()
#将JSON转化为Python的数据结构
json_data = json.loads(resp)
city_data=json_data['HeWeather6'][0]
#print(u'穿衣指数：' + city_data['lifestyle'][1]['txt'])
wear = city_data['lifestyle'][1]['txt']
print(u'穿衣指数：' + wear)
sport = city_data['lifestyle'][3]['txt']
print(u'运动指数：' + sport)
uv = city_data['lifestyle'][5]['txt']
print(u'防晒指数：' + uv)
print(u'-------------------------啦啦啦啦会唱歌的分割线----------------------------')

print(u'我猜你现在在' + city +'，现在外面感觉有' + fl + '度，你确定现在要去食堂吃饭嘛？= =#')
choice = input('请输入Y OR N      ')
if choice == 'Y' or choice == 'y':
    time.sleep(0.5)
    print('正在进入高端的程序。。。')
    time.sleep(0.5)
    print('★★★★★★★★★')
    time.sleep(0.5)
    print('★★★★★★★★★★★★★★★★★★★★★')
    time.sleep(0.5)
    print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
    time.sleep(0.5)
    print('呦西，那王小帅帮你选食堂。')
    hp = input('请输入当前HP值（0-100）（0表示身体被掏空，100表示满血状态）：')
    if int(hp) >= 50:
        time.sleep(1)
        print('真是元气满满的少女呢！')
        if int(aqi) < 70:
            time.sleep(1)
            print('今天空气棒棒哒，我觉得。。。（光速计算中。。。）')
            time.sleep(0.5)
            print('拯救选择困难症，正在思考怎样回答。。。')
            time.sleep(0.5)
            print('★★★★★★★★★')
            time.sleep(0.5)
            print('★★★★★★★★★★★★★★★★★★★★★')
            time.sleep(0.5)
            print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
            time.sleep(0.5)
            mail = '勇敢的少女啊出发吧，' + random.choice ( ['学三食堂！', '学五食堂！', '学四食堂！', '学一食堂！', '留园食堂！'] )
            
            print(mail)
        elif int(aqi) < 150:
            print('今天空气不太好呢。。。要戴口罩呀，我认为你应该去。。。（光速计算中。。。）')
            time.sleep(0.5)
            print(random.choice ( ['学一食堂！', '留园食堂！','清真食堂！'] ))
        else:
            print('今天空气太糟糕了。。。回宿舍点外卖吧。。。')
    elif int(hp) >= 40:
        pass
    else:
        print('可怜的孩纸，根据当前HP值计算，我认为你应该回宿舍点外卖。')

else:
    print('= =对手指。。')
