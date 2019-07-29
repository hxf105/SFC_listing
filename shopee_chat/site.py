from shopee_chat.BasicFunction import *

#单击“站点”菜单的展开按钮
findXpath(xpath='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/i').click()
wait1()
#单击“站点管理”菜单
findXpath(xpath='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div/a/li').click()
wait1()
findXpath(xpath='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div/a/li').click()
wait1()
