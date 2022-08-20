from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
print(driver.title)

# <iframe allowfullscreen title="主人动态内容区">
driver.switch_to.frame('QM_Feeds_Iframe')
n = 1
while 1:
    # <span class=" ui-mr8 state">
    target_time = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[1]/div[4]/div[2]/span' % n)
    if not target_time:
        break
    for i in target_time:
        print(i.text)

    # <div class="f-info">
    target_text = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[2]/div/div[1]' % n)
    if not target_text:
        break
    for j in target_text:
        print("文本：" + j.text)

    # <a href="javascrpt:;">
    target_view = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[3]/div[1]/a' % n)
    if not target_view:
        break
    for k in target_view:
        print(k.text)

    # <span class="f-like-cnt">
    target_like = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[3]/div[3]/div[2]/span' % n)
    if not target_like:
        break
    for l in target_like:
        print("赞：" + l.text)

    # <div class="user-list">
    target_user = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/ul/li[%s]/div[3]/div[3]/div[2]' % n)
    if not target_user:
        break
    for m in target_user:
        print("点赞的人：" + m.text)
    print("____________")
    n = n + 1
