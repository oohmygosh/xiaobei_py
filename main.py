import sqlite3
from datetime import date

import requests

loginUrl = "https://xiaobei.yinghuaonline.com/xiaobei-api/login"
healthReport = "https://xiaobei.yinghuaonline.com/xiaobei-api/student/health"
healthSearch = "https://xiaobei.yinghuaonline.com/xiaobei-api/student/health/list"
header = {
    "authorization": "",
    "Content-Type": "application/json",
    "Host": "xiaobei.yinghuaonline.com",
    "Connection": "Keep-Alive",
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; vmos Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0) "
}
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mydb = sqlite3.connect("identifier.sqlite")
    cursor = mydb.cursor()
    cursor.execute("select * from user")
    fetchall = cursor.fetchall()
    for user in fetchall:
        login = requests.post(loginUrl, json={"username": user[1],
                                              "password": user[2],
                                              "uuid": "",
                                              "code": "CODE",
                                              "token": ""
                                              })
        json = login.json()
        if json['msg'] == "操作成功":
            header["authorization"] = json['token']
            search = requests.get(url=healthSearch, headers=header,
                                  params={"params": '{"beginCreateTime": "' + str(
                                      date.today()) + '", "endCreateTime": "' + str(
                                      date.today()) + '"}'})
            if not search.json()['rows']:
                requests.post(url=healthReport, json={
                    "temperature": "36",
                    "coordinates": "中国-广西壮族自治区-桂林市-雁山区",
                    "location": "110.31354181310095,25.279068116904657",
                    "health_state": "1",
                    "dangerous_region": "2",
                    "dangerous_region_remark": "",
                    "contact_situation": "2",
                    "go_out": "1",
                    "go_out_remark": "",
                    "remark": "无",
                    "family_situation": "1"
                }, headers=header)
                print(str(user[1]) + " 打卡成功!")
            else:
                print(str(user[1]) + " 今日已打卡!")
        else:
            print(str(user[1]) + " 登陆失败!")
