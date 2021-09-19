# # 공공데이터 API 호출하기 - 부동산 실거래가
# * https://www.data.go.kr/
# * https://www.data.go.kr/dataset/3050988/openapi.do
#
# # API 사용 신청하기
# * 공공데이터는 사용 신청을 해야 사용할 수 있음.
# 서비스키 발급은 금방 발급이 되나,
# 사용은 1시간 ~ 24시간 이후에 사용가능함. 본인의 경우는 하루가 지나서야 사용가능했음.
#
# # 시크릿 발급하기
# * 한 입에 웹 크롤링

import os
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# api_key 숨김방법
api_key = os.environ['DATA_GO_API_KEY']  # win10 환경변수 설정 후 사용 고급시스템, 환경변수, 시스템변수, 콜론없이 string만 입력
URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11110&DEAL_YMD=201512&serviceKey='+api_key

URL_O = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
land_code=str(11110)
deal_date = str(201512)
page_no = str(1)
numofrows = str(1000)
LAND_CODE = '?LAWD_CD=' + land_code
DEAL_DATE = '&DEAL_YMD=' + deal_date
PAGE_NO = '&pageNo=' + page_no
NUMROWS = '&numOfRows=' + numofrows
URL_SK = '&serviceKey='+api_key

URL_ALL = URL_O + LAND_CODE + DEAL_DATE + PAGE_NO + NUMROWS + URL_SK
URL_ALL1 = URL
req = requests.get(URL_ALL)

soup = bs(req.content, 'html.parser')
# print(soup.prettify())
# print('*'*100)

land = soup.find_all('item')

def get_name_value(lv):
    l_sp = re.split(r'[>]\s*', lv)  # make character for splitting using regular expression
    name = re.sub('[<>]','',l_sp[0])
    # name = l_sp[0].replace('<','').replace('>','')
    value = l_sp[-1]
    return name, value

land_list = []
for trade in land:
    tr_dict = {}
    for tr in trade.contents[::2]:
        name, value = get_name_value(tr)
        tr_dict[name] = value
        # print('name: {}, value: {}'.format(name,value))
    land_list.append(tr_dict)

df = pd.DataFrame(land_list)

print(df)