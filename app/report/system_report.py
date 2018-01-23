import subprocess
from app.report.mailer import send_mail


def send():
    html_data_encoded = subprocess.check_output(["lshw", "-html"])
    html_str = html_data_encoded.decode('utf-8')
    send_mail('support@mail.cyces.co', (
        'kandhan.kuhan@gmail.com',
        'ananthakumar.akr@gmail.com',
        'thecorptechteam@gmail.com',
        'vidushi.meenu@gmail.com',
        'rootat1306@gmail.com',
    ), 'System Report', html_str)
    # send_mail('support@mail.cyces.co', (
    #     'kandhan.kuhan@gmail.com',
    # ), 'System Report', html_str)