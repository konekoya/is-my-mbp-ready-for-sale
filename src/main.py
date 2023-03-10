import os

import requests
from dotenv import load_dotenv

from mailer import send_email

load_dotenv()

url = "https://www.apple.com/tw/shop/configUpdate/MNWA3TA/A?node=home%2Fshop_mac%2Ffamily%2Fmacbook_pro%2Fconfig&option.memory_aos_phantom_z176=065-CDP2&option.hard_drive_solid_state_drive_aos_phantom_z176=065-CDP6&option.keyboard_and_documentation_z176=TA065-CDTM&option.sw_final_cut_pro_z176=065-CDTW&option.sw_logic_pro_z176=065-CDTY&bfil=0"


to_email = os.environ.get('TO_EMAIL')

headers = {
    'authority': 'www.apple.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    'cookie': 'dssid2=e8f782da-7b9a-4d96-8f4b-c4504265b9f8; dssf=1; as_pcts=m+Cxs7ntTMBAXfQCGVf5fpUGU_nELy5L+0K_UQR+0kGTppPkwZkKo8AgvI7sAsBjB8M4NzoQJtWr614hCCdreBtbxmZQP9J7; as_dc=ucp1; as_sfa=Mnx0d3x0d3x8emhfVFd8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=TW; s_fid=7BE8DCB0DB4D43D4-0D9662F55EA3CC8E; s_cc=true; as_gloc=a7ffaa6f167f49c9abaeed38702b6a0a044d451736f4f05737f7e70218ee425af13b14560a55c2d8f239ce777b74b37ba1c2fcf15792260d51224401165d62dda839addf8e8cd9e19597b06db3b25fee6ee7b88af88751901e093d4a178f9280; as_atb=1.0|MjAyMy0wMy0wNyAxMjo1OTo0NQ|50018e95cacbe2717e1113201cb9caff05d11e56; as_dc=ucp1; dssf=1; dssid2=e8f782da-7b9a-4d96-8f4b-c4504265b9f8',
    'if-modified-since': 'Tue, 07 Mar 2023 08:55:34 GMT',
    'if-none-match': '"91a4a46876c05410e853324f09299855"',
    'referer': 'https://www.apple.com/tw/shop/buy-mac/macbook-pro/16-%E5%90%8B-%E5%A4%AA%E7%A9%BA%E7%81%B0%E8%89%B2-apple-m2-max-%E9%85%8D%E5%82%99-12-%E6%A0%B8%E5%BF%83-cpu-%E8%88%87-38-%E6%A0%B8%E5%BF%83-gpu-1tb',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
data = r.json()

shipping_date = data['body']['replace']['summary']['shipping']

if '暫未發售' in shipping_date:
    print('Not ready to sell yet')
    send_email(to=to_email,
               subject=f"Your MackBook Pro 16 is not ready for sell yet 😢😢😢")
else:
    print('Quick, MBP 16 is ready for sell. Go grab your one!')
    send_email(to=to_email,
               subject="Hurry, MBP 16 is ready for sell. Go crab your one!")
