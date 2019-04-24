# -*- coding: utf-8 -*-

# gmail
GMAIL_SERVER = "smtp.gmail.com"
GMAIL_PORT = 465
GMAIL_USE_SSL = True
GMAIL_USERNAME = "<your_gmail>@gmail"
GMAIL_PASSWORD = ""

# outlook
OUTLOOK_SERVER = "smtp-mail.outlook.com"
OUTLOOK_PORT = 587
OUTLOOK_USE_SSL = True
OUTLOOK_USERNAME = "<your_outlook>outlook.com"
OUTLOOK_PASSWORD = ""

# 163
NETEASE_SERVER = "smtp.163.com"
NETEASE_PORT = 465
NETEASE_USE_SSL = True
NETEASE_USERNAME = "<your_163>@163.com"
NETEASE_PASSWORD = "需要登入信箱後，在「設置」選擇「客戶端授權密碼」獲取授權碼"

# yahoo
YAHOO_SERVER = "smtp.mail.yahoo.com"
YAHOO_PORT = 465 # or 587
YAHOO_USE_SSL = True
YAHOO_USERNAME = "<your_yahoo>@yahoo.com"
YAHOO_PASSWORD = ""


try:
    # store your email and password in local_settings
    from src.local_settings import * 
except ImportError:
    pass

# choose one
MAIL_SERVER = NETEASE_SERVER
MAIL_PORT = NETEASE_PORT
MAIL_USE_SSL = NETEASE_USE_SSL
MAIL_USERNAME = NETEASE_USERNAME
MAIL_PASSWORD = NETEASE_PASSWORD
