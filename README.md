# xiaobei_py

小北同学自动打卡

# 使用

```powershell
# 连接sqlite
sqlite3 identifier.sqlite
# 插入自己的账号密码（密码需要base64加密）
insert into user values(1,"你的账号","你的密码");
```
然后丢服务器上面加个定时任务每天定时运行就ok了
```powershell
# 后台运行
nohup python ./main.py &
```
