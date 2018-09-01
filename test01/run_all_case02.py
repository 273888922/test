#coding:utf-8
import unittest,time,HTMLTestRunner,smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#这是优化版执行所有用例并发送，分四步
#第一步加载测试用例
#第二步执行测试用例
#第三步获取最新测试报告
#第四步发送邮箱（这一步不想执行的话，可以注释掉最后面的函数就好）
def all_case():
    #定义discover方法的参数
    a=unittest.defaultTestLoader.discover(case_path,
                                          pattern="test*.py",
                                          top_level_dir=None)
    return a
def run_case():
    '''执行所有的测试用例，并把结果写入测试报告'''
    now=time.strftime("%Y_%m_%d %H_%M_%S")
    report_apath=os.path.join(report_path,now+"result.html")
    fp =open(report_apath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title="自动化测试报告，测试结果如下",
                                         description="测试用例执行情况：")
    #调用add_case函数返回值
    runner.run(all_case())
    fp.close()
def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path,fn)))
    print("最新测试生成的报告："+lists[-1])
    #找到最新生成的报告文件
    report_file=os.path.join(report_path,lists[-1])
    return report_file
def send_mail(sender,psw,receiver,smtpserver,report_file,port=465):
    '''发送最新的测试报告内容'''
    #读取测试报告的内容
    with open(report_file,"rb")as f:
        mail_body=f.read()
    #定义邮件内容
    msg=MIMEMultipart()
    body=MIMEText(mail_body,_subtype='html', _charset="utf-8")
    msg["Subject"]= u"自动化测试报告"
    msg["from"]=sender
    msg["to"]=";".join(receiver)
    msg.attach(body)
    #添加附件
    att=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="report.html"'#report.html附件名称
    msg.attach(att)
    try:
        smtp=smtplib.SMTP_SSL(smtpserver,port)#QQ服务器
    except:
        smtp=smtplib.SMTP()#163服务器
        smtp.connect(smtpserver,port)
    smtp.login(sender,psw)#用户名密码
    smtp.sendmail(sender,receiver,msg.as_string())#发送
    smtp.quit()#退出
if __name__ == "__main__":
    case_path=os.path.join(os.getcwd(),"case")#测试用例的路径
    report_path=os.path.join(os.getcwd(),"report")#测试报告的路径
    run_case()#运行测试用例
    report_file=get_report_file(report_path)
    smtpserver="smtp.163.com"
    sender="13588241650@163.com"
    psw="renwenming0"
    receiver=["273888922@qq.com"]
    send_mail(sender,psw,receiver,smtpserver,report_file)#发送
    print("发送成功")
else:
    print("发送失败")