import warnings
warnings.simplefilter('ignore')
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

#
company_folder = 'company/'
file_path = os.path.join(company_folder, '20220805_마.xlsx')
# print(file_path)
df = pd.read_excel(file_path, skiprows=1)

companies = list(df.iloc[:, 0])
# print(len(companies))
# print(companies)


base_url = "https://www.teamblind.com/kr/company/"
# base_url = 'https://www.teamblind.com/kr/company/매스웍스코리아'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

result = []
for company in companies:
    url = urljoin(base_url, company)
    # print('url: ', url)
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        parsed = soup.find('span', 'star')
        # print(parsed)
        print(company, parsed.text[-3:])
        score = float(parsed.text[-3:])

        if score >=4.0:
            result.append(company)

print(result)