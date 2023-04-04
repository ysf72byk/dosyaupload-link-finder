import requests
import re
import random
import string
import os

hit=0


print(f"""

                         ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▀▀▄   
                        ▐ ▄▀   █ █   █  █  █         
                          █▄▄▄▀  ▐   █  ▐  █    ▀▄▄  
                          █   █      █     █     █ █ 
                         ▄▀▄▄▄▀   ▄▀▀▀▀▀▄  ▐▀▄▄▄▄▀ ▐ 
                        █    ▐   █       █ ▐         
                        ▐        ▐       ▐        DC:BiG#0627
                        """)






def start(key):
    a = ""
    global hit
    for i in range(200):
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=int(key)))
        a += "https://www.dosyaupload.com/" + random_string + "\r\n"



    data = {
        'file_urls': a,
        'submitme': '1',
        'submit': '',
    }


    r = requests.post('https://www.dosyaupload.com/link_checker.html',data=data)
    html_content = r.text
    pattern = r'<td>(https://www.dosyaupload.com/\w+)</td>\s+<td style="text-align: center; width: 120px;">\s+<span style="color: (green|red);">(Active|Disabled)</span>'
    match_list = re.findall(pattern, html_content)
    lst = [(match[0], match[2]) for match in match_list]
    #print(links_and_statuses)
    result = list(filter(lambda x: x[1] == 'Active', lst))
    linkss = [x[0] for x in result]
        
        
    



    for i in linkss:
        r = requests.get(i).text.split('<title>')[1].split('</title>')[0]
        with open('hits.txt', 'a') as f:
            f.write(str(i)+"  ---> "+str(r)+'\n')
            print(str(i)+"  ---> "+str(r))
            hit+=1



while 1:
    key=input("kaç haneli link bulsun(4 veya 5 girin ) :")
    if key==4 or key==5:
        break
    else:
        print("lütfen 4 veya 5 girin (önerilen 4 [5 ler geç bulunur ve yeni upload edilenlerdir ]) ")



c=0
while 1:
    tab_name = f"title dosyaupload.com Link Finder by BiG - Denendi: [{c}] - Hit: [{hit}]"
    os.system(tab_name)
    start(key)
    c+=200
