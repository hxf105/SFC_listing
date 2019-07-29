from shopee_chat.BasicFunction import *
shopee_chat()   #打开链接
shopee_chat_login1()    #登入操作

#验证文本是否符合预期
def welcom(self):
  t = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/span')
  self.assertEqual(t.text,'欢迎登录shopee运营管理系统')
  #print('登录成功后首页会显示:'.format(t.text))
  print('登录成功后首页会显示:',t.text)
'''
断言
t = self.driver.find_element_by_xpath('//*[@id="mainmenu"]/ul/li[1]/a/span')
print('登录成功后首页会显示：{}'.format(t.text))
self.assertEqual(t.text, u'我的地盘')
验证
try:
self.assertEqual(u"1234_百度搜索", driver.title)
except AssertionError as e:
print u"找不到这个标题"
'''

#单击“用户”菜单的展开按钮
findXpath(xpath='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/i').click()
wait1()
#单击“用户管理”按钮
findXpath(xpath='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div/a/li').click()
wait1()

#【用户查无】
#输入“账号”查询条件
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input').clear()
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input').send_keys('account')
wait1()
#单击“查询”按钮
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[4]/div/button[1]').click()
wait1()

#【添加用户】
#单击“添加用户”按钮，打开添加弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/button').click()
wait1()
#单击“取消”按钮，关闭弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[3]/div/button[1]').click()
wait1()
#重新打开“添加用户”弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/button').click()
wait1()
#空数据单击“确认”按钮提交
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[3]/div/button[2]').click()
wait1()
#输入账号数据查询并选择账号
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[2]/form/div/div/div/div/input').clear()
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[2]/form/div/div/div/div/input').send_keys('lijianting')
wait3()
#单击选中筛选结果用户账号数据   --------功能不可用，路径修改
findXpath(xpath='//*[@id="el-autocomplete-5343-item-0"]').click()
wait1()

#配置账号权限
#单击“编辑权限”按钮，打开编辑权限弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[2]/div[2]/button').click()
wait1()
#单击“关闭”按钮关闭弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/div/div[1]/button').click()
wait1()
#重新打开账号配置弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[2]/div[2]/button').click()
wait1()

#查询账号-查无
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/div/div[2]/div[1]/input').clear()
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/div/div[2]/div[1]/input').send_keys('account')
wait1()
#账号配置 --------待功能可用后补充脚本
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/div/div[2]/div[1]/input').send_keys('account')

#单击确定按钮，提交配置
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/div/div[3]/div/button').click()
wait1()
#单击“添加用户”的确定按钮，提交
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div/div[3]/div/button[2]').click()
wait1()

#查询上一步添加的数据
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input').clear()
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input').send_keys('lijianting')
wait1()
#单击“查询”按钮
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[4]/div/button[1]').click()
wait2()
#-------添加断言，验证查询结果

#【编辑用户权限配置】
#单击“编辑权限”按钮，打开编辑权限弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]').click()
wait1()
#单击“关闭”按钮，关闭弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[1]/button').click()
wait1()
#重新打开弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]').click()
wait1()
#-----编辑权限配置
#单击站点的展开按钮，展开站点下的账号数据   -----第一个站点的展开
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/div[2]/div[1]/div[1]/span[1]').click()
wait1()
#选中某一账号-----待补充脚本
#取消选中另一账号------待补充脚本
#单击“确定”按钮，提交编辑
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button').click()
wait1()
#再次打开编辑弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]').click()
wait1()
#验证上一次编辑的结果是否存储正确 -----待补充脚本

#验证完毕，关闭编辑弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[1]/button').click()
wait1()

#【修改用户状态】
#验证用户状态
#t = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/span')
#assertEqueal(t.text,'启用')

#验证修改状态按钮文字 -----待补充脚本

#修改账号状态，单击操作列的修改状态按钮,打开确认修改弹窗  ---第一行元素
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]').click()
wait1()
#验证弹窗提示语文本是否符合预期 -----待补充脚本

#单击确认窗口的关闭按钮，取消修改状态操作
findXpath(xpath='/html/body/div[3]/div/div[3]/button[1]').click()
wait1()
#重新打开修改状态确认弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]').click()
wait1()

#单击“确定”按钮，确认修改状态为禁用
findXpath(xpath='/html/body/div[3]/div/div[3]/button[2]').click()
wait1()

#验证修改状态是否成功----验证状态栏位文字、按钮文字

#重新修改状态为启用

#【删除】
#单击“删除”按钮，打开确认弹窗
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]').click()
wait1()
#验证删除确认弹窗文本 ------待补充脚本

#单击确认弹窗的“取消”按钮，取消删除操作
findXpath(xpath='/html/body/div[3]/div/div[3]/button[1]').click()
wait1()
#重新单击“删除”按钮，执行删除操作
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]').click()
wait1()
#单击“确认”按钮，确认删除
findXpath(xpath='/html/body/div[3]/div/div[3]/button[2]').click()
wait1()
#删除后查无
#查询
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input').send_keys('account')
wait1()
#单击“查询”按钮
findXpath(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[4]/div/button[1]').click()
wait1()
#验证查无数据 ------待补充脚本

#重新添加该账号，验证“删除状态的账号可以重新添加”
#然后再次删除，形成闭环，不影响下次脚本执行










