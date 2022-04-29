# 此脚本只适用于无验证码情况
# 运行此脚本须搭建必要环境
# Chrome 100.0.4896.127, Python 3.9.12, selenium 4.1.0
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(
    'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 请读者思考：为什么不是driver.get("https://qzone.qq.com/")
driver.get("https://user.qzone.qq.com")
time.sleep(2)
print(driver.title)

# 提交表单并模拟点击
driver.switch_to.frame('login_frame')
driver.find_element(By.ID, 'switcher_plogin').click()
time.sleep(2)
driver.find_element(By.ID, 'u').clear()
time.sleep(2)
driver.find_element(By.ID, 'u').send_keys('3511706170')  # 此处改为自己的QQ号
time.sleep(2)
driver.find_element(By.ID, 'p').clear()
time.sleep(2)
driver.find_element(By.ID, 'p').send_keys('')  # 此处键入密码
time.sleep(5)
driver.find_element(By.ID, 'login_button').click()
time.sleep(5)
driver.find_element(By.ID, 'aMainPage').click()
time.sleep(3)

# 必须先switch到frame，才能使用绝对路径定位元素
driver.get("https://user.qzone.qq.com/3511706170/main")  # 需根据自己的QQ号修改url
driver.switch_to.frame('QM_Feeds_Iframe')
n = 1
while 1:
    target_time = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[1]/div[4]/div[2]/span' % n)
    if not target_time:
        break
    for i in target_time:
        print(i.text)

    target_like = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[3]/div[3]/div[2]/span' % n)
    if not target_like:
        break
    for j in target_like:
        print("赞：" + j.text)
    n = n + 1
