from seleniumwire import webdriver
from datetime import datetime
import time
import re
def sanitize_filename(filename):
    # Định nghĩa một biểu thức chính quy để tìm các ký tự không hợp lệ
    invalid_chars = r'[\/:*?"<>|]'
    # Thay thế các ký tự không hợp lệ bằng dấu gạch ngang
    sanitized_filename = re.sub(invalid_chars, '-', filename)
    return sanitized_filename
n = 0
d = {}
def response_interceptor(request, response):
    # if 'ebank.tpb.vn' in request.url:
        current_time = datetime.now()

        formatted_time = current_time.strftime("%d-%m-%y %H-%M-%S")
        global n
        s = ''
        s = '=============request==============\n' + f'{request.method} : {request.url}\n{request.headers}'
        if request.method == 'POST':
                s = s + f'\n{request.body}'
        if request.response.status_code == 200:
            if request.url.endswith('.js') or request.url.endswith('.css'):
                 pass
            else:
                response_body = request.response.body 
                s = s + '\n=============Response==============\n' f"{response_body}"
        name = sanitize_filename(request.url.replace('https://',''))
        if len(name) ==0:
            name= 'trangkhac'

        if name in d:
            d[name] = d[name] + 1    
            with  open(f'text\\{n}_{name}____{d[name]}____{formatted_time}_.txt','w',encoding='utf8') as f:
                    f.write(s)
        else:
            d[name] = 0  
            with  open(f'text\\{n}_{name}____{d[name]}____{formatted_time}_.txt','w',encoding='utf8') as f:
                    f.write(s)  
        n =n+1
options = webdriver.ChromeOptions()
options.add_argument("log-level=3") # disable logs
driver = webdriver.Chrome(options=options)
driver.response_interceptor = response_interceptor
driver.get("https://ebank.tpb.vn")
n = 0

while True:
     pass
