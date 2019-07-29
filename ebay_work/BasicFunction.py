from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()

# driver.set_window_size(1366,768)   #设置窗口大小
import time as t
def wait1():
    t.sleep(1)
def wait2():
    t.sleep(2)
def wait3():
    t.sleep(3)
def wait5():
    t.sleep(5)
def wait7():
    t.sleep(7)
def wait10():
    t.sleep(10)
def wait15():
    t.sleep(15)
def wait20():
    t.sleep(20)
# driver.implicitly_wait(10)

def findID(id):
    global driver
    d=driver.find_element_by_id(id)
    return d
def findName(name):
    global driver
    d=driver.find_element_by_name(name)
    return d
def findClassName(name):
    global driver
    d=driver.find_element_by_class_name(name)
    return d
def findTagName(name):
    global driver
    d=driver.find_element_by_tag_name(name)
    return d
def findLinkText(text):
    global driver
    d=driver.find_element_by_link_text(text)
    return d
def findPLinkText(text):
    global driver
    d=driver.find_element_by_partial_link_text(text)
    return d
def findXpath(xpath):
    # global driver
    global driver
    d=driver.find_element_by_xpath(xpath)
    return d
def findCss(css):
    global driver
    d=driver.find_element_by_css_selector(css)
    return d

def ebay_work():
    global driver
    driver.get('http://work.ebay.sfc.com/login')
    wait3()
def advt():
    global driver
    driver.get('http://ms.advt.sfc.com/login')
    wait3()
def shopee_chat():
    global driver
    driver.get('http://chat.shopee.com/#/login?redirect=%2Fdashboard')
    wait3()
# 问题记录：如何打开一个新的标签页？

# ebay
def ebay_work_login(username,password):
    findName(name='username').clear()
    findName(name='username').send_keys(username)
    findName(name='password').clear()
    findName(name='password').send_keys(password)
    wait1()
    findXpath(xpath='//*[@id="app"]/div/form/div[3]/div/button').click()  # 单击登录按钮
    wait3()
def ebay_work_login1():
    return ebay_work_login(username='houxiaofeng',password='123456')
def ebay_work_login2():
    return ebay_work_login(username='cuichunyan',password='123456')
def ebay_work_login3():
    return ebay_work_login(username='zhuhailaing',password='123456')
def ebay_work_login4():
    return ebay_work_login(username='chengyanbao',password='123456')

# advt
def advt_login(username,password):
    findName(name='username').clear()
    findName(name='username').send_keys(username)
    findName(name='password').clear()
    findName(name='password').send_keys(password)
    wait1()
    findXpath(xpath='//*[@id="app"]/div/form/div[3]/div/button').click()
    wait3()

def advt_login1():
    return advt_login(username='houxiaofeng',password='123456')

# shopee_chat
def shopee_chat_login(username,password):
    findName(name='username').clear()
    findName(name='username').send_keys(username)
    findName(name='password').clear()
    findName(name='password').send_keys(password)
    wait1()
    findXpath(xpath='//*[@id="app"]/div/form/div[3]/div/button').click()
    wait3()
def shopee_chat_login1():
    return shopee_chat_login(username='houxiaofeng',password='123456')

# 下拉菜单
def dropDownx(xpath,val):
    findXpath(xpath=xpath).find_element_by_xpath("//option[@value="+val+"]")
def dropDowni(id,val):
    findID(id=id).find_element_by_xpath("//option[@value="+val+"]")

# 删除readonly属性
def js():
    js = "$('input[id=select-date-dom]').removeAttr('readonly')"  # 2.jQuery，移除属性       【成功】
    driver.execute_script(js)

# 退出登入
def quit():
    return findXpath(xpath='//*[@id="menber-menu-list"]/div[2]/span[1]').click()
    wait3()
