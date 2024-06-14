import random

def get_port_number(app_name):
    ports = {
        'dhcp_client': '68',
        'dhcp_server': '67',
        'dns': '53',
        'tftp': '69',
        'ftp_data': '20',
        'ftp_control': '21',
        'smtp': '25',
        'pop3': '110',
        'http': '80'
    }
    return ports.get(app_name.lower(), 'Unknown application')

def get_pseudo_random_app(asked_apps):
    apps = ['dhcp_client', 'dhcp_server', 'dns', 'tftp', 'ftp_data', 'ftp_control', 'smtp', 'pop3', 'http']
    remaining_apps = [app for app in apps if app not in asked_apps]
    if not remaining_apps:
        asked_apps.clear()  # 清空已询问的应用列表
        remaining_apps = apps
    return random.choice(remaining_apps)

asked_apps = []

while True:
    app = get_pseudo_random_app(asked_apps)
    asked_apps.append(app)
    print(f"请输入 {app} 的端口号：")
    user_port = input("端口号: ")
    correct_port = get_port_number(app)
    if user_port == correct_port:
        print("回答正确！")
    else:
        print(f"回答错误。正确答案是：{correct_port}")
    
