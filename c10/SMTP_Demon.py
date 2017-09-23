#coding: utf-8
import smtplib
import os
import psutil
from email.mime.text import MIMEText    #导入MIMEText类
ip = os.popen("ifconfig |grep -v 127 |grep inet |awk '{print $2}'|cut -d: -f2").read().strip()     #获取IP地址
hostname  = os.popen("hostname").read().strip()   #获取主机名
cpu = psutil.cpu_count()  #获取CPU线程
mem = os.popen("free -m |grep Mem |awk '{print $2}'").read().strip()+"M"  #获取内存总量
disk = os.popen("fdisk -l |grep -E Disk |awk '{print $3}'").read().strip()+"G" #获取硬盘总大小
HOST = "smtp.163.com"      #指定使用网易163邮箱
SUBJECT = u"服务器硬件信息"   #邮件标题
TO = "351174197@qq.com"   #收件人
FROM = "www223c@163.com"    #发件人
msg = MIMEText("""
                               <table color="CCCC33" width="800" border="1" cellspacing="0" cellpadding="5" text-align="center">
                                       <tr>
                                               <td text-align="center">name</td>
                                               <td text-align="center">network</td>
                                               <td>CPU</td>
                                               <td>Mem</td>
                                               <td>Disk</td>
                                       </tr>   
                                       <tr>   
                                               <td text-align="center">%s </td>
                                               <td>%s </td>
                                               <td>%s </td>
                                               <td>%s </td>
                                               <td>%s </td>
                                       </tr>
                               </table>""" % (hostname,ip,cpu,mem,disk),"HTML","uft-8")
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
print u'as_string : {}'.format(msg.as_string())
try:
    server = smtplib.SMTP()      #创建一个SMTP对象
    server.connect(HOST,"25")      #通过connect方法链接到smtp主机
    server.starttls()             #启动安全传输模式
    server.login("www223c@163.com","chen351174197")  # 登录163邮箱 校验用户，密码
    server.sendmail(FROM, [TO], msg.as_string())   #发送邮件  
    server.quit()
    print "邮件发送成功 %s %s %s %s %s" % (hostname,ip,cpu,mem,disk)  #发送成功并打印
except Exception, e:
    print "邮件发送失败："+str(e)

