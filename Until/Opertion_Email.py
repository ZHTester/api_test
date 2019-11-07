# encoding: utf-8

"""
# @Time    : 28/10/2019 11:09 上午
# @Author  : Function
# @FileName    : Opertion_Email.py
# @Software: PyCharm

邮件发送
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from  Config.setting import *
from Until.Other_Function import OtherFunction


class SEmail:

    def Email_UiTest(self,send_message, out_file, out_filename):
        """
        :param send_message:  邮件主题信息
        :param out_file:  发送文件路径
        :param out_filename:  发送文件名称
        :return:
        """
        # 相关变量读取配置文件
        mail_host= MAIL_HOST
        mail_user= MAIL_USER
        mail_pass= MAIL_PASS
        port = PORT
        sender = SENDER
        receivers = RECEIVERS

        # 定义邮件格式
        message = MIMEMultipart()
        message['From'] = Header(sender)
        message['To'] = Header(','.join(receivers))
        subject = SUBJECT
        message['Subject'] = Header(subject, 'utf-8')

        # 构造邮件主题内容
        text = send_message
        body = MIMEText(text,'plain','utf-8')
        message.attach(body)

        # 上传文件附件 测试case用例集合
        att1 = MIMEText(open(out_file, 'rb').read(), 'base64', 'Unicode')
        att1["Content-Disposition"] = 'attachment; filename='+out_filename
        message.attach(att1)

        # 连接邮箱Server
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,port)
        except smtplib.SMTPException:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("------------邮件发送成功------------")


if __name__ == '__main__':
    send = SEmail()
    s = OtherFunction(0)
    message = s.pass_fail_number(444.0, 11.0)
    s = SEmail()
    s.Email_UiTest(message, path_excle, OUT_FILENAME)