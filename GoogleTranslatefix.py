import socket
from ping3 import ping
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("请以管理员权限运行程序!")
    sys.exit()

print("阅读并同意免责声明:")
print("""免责声明
本程序仅提供用户绕过谷歌限制使用翻译的技术手段，一切操作均由用户自愿进行。
请注意，如果用户的使用侵犯了谷歌的利益，与本程序无关。用户应当自行承担因违反相关法规或谷歌服务条款而可能引起的法律责任和风险。
使用本程序代表您已理解并同意以上免责声明内容。""")

agree = input('如果同意请输入Y:')
if agree.upper() != 'Y':
    print("未确认，未进行修改。")
    sys.exit()

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def check_ping(ip_to_check, timeout=1):
    try:
        result = ping(ip_to_check, timeout=timeout)
        if result is not None:
            print(f"当前IP可以正常使用")
        else:
            print(f"当前IP不能使用")
    except Exception as e:
        print(f"Error while pinging {ip_to_check}: {e}")

def add_to_hosts(ip_address):
    try:
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as hosts_file:
            hosts_file.write(f'{ip_address} translate.googleapis.com\n')
            hosts_file.write(f'{ip_address} translate.google.com\n')
        print(f'Successfully added to hosts file.')
    except Exception as e:
        print(f'Error while adding to hosts file: {e}')

# 替换为你想要检测的域名
domain = "tpc.googlesyndication.com"
ip_address = get_ip_address(domain)

if ip_address:
    print(f"The IP address of {domain} is: {ip_address}")
    check_ping(ip_address)
    add_to_hosts(ip_address)
else:
    print(f"Unable to resolve the IP address for {domain}")
