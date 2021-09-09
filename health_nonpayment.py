# # 공공데이터 API 호출하기 - 비급여진료비정보서비스
# * https://www.data.go.kr/
# * https://www.data.go.kr/dataset/3050988/openapi.do
#
# 서비스키 발급은 금방 발급이 되나,
# 사용은 1시간 ~ 24시간 이후에 사용가능함. 본인의 경우는 하루가 지나서야 사용가능했음.
# * 공공데이터는 사용 신청 (활용 신청) 은 승인 즉시 사용가능
#

import requests
from bs4 import BeautifulSoup as bs
import xmltodict, json
import re
import pandas as pd
import openpyxl

api_key = "4fw71cT9NmHBLiTdlrZJS5BZ6VaGfRZUdpzpDVssN6OImKE8WcKzLlpRqq1HY7C%2F6Y%2BV1M9mngsqOXYLXJ624w%3D%3D"
URL = 'http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemCodeList?pageNo=1&numOfRows=10&ServiceKey='+api_key

URL_O = 'http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemCodeList'
page_no = str(1)
numofrows = str(10)
PAGE_NO = 'pageNo={}'.format(page_no)
NUMROWS = 'numOfRows=' + numofrows
URL_SK = 'serviceKey='+api_key

URL_ALL = URL_O + '?' + PAGE_NO + '&' + NUMROWS + '&' + URL_SK
URL_ALL1 = URL
req = requests.get(URL_ALL)
soup = bs(req.content, 'html.parser')
# print(soup.prettify())
# print('*'*100)

def define_columns():
    payment_class = {}
    payment_class['divCd1'] = '1차분류코드'
    payment_class['divCd1Nm'] = '1차분류코드명'
    payment_class['divCd1Dsc'] = '1차분류코드설명'
    payment_class['divCd2'] = '2차분류코드'
    payment_class['divCd2Nm'] = '2차분류코드명'
    payment_class['divCd2Dsc'] = '2차분류코드설명'
    payment_class['divCd3'] = '3차분류코드'
    payment_class['divCd3Nm'] = '3차분류코드명'
    payment_class['divCd3Dsc'] = '3차분류코드설명'
    return payment_class

dict = xmltodict.parse(req.content)  # change xml to dict format

nonpay_list = dict['response']['body']['items']['item'] # item를 list형으로 정리

df = pd.DataFrame(nonpay_list)

payment_class = define_columns()  # columns name change
df.rename(columns=payment_class, inplace=True)  # change columns names with dictionary

print(df)

jsonString = json.dumps(dict['response']['body']['items'], ensure_ascii=False)
jsonObj = json.loads(jsonString)
# print(jsonObj)

for item in jsonObj['item']:
    print(item)

df1 = pd.DataFrame(jsonObj['item'])
df1.rename(columns=payment_class, inplace=True)  # change columns names with dictionary
print(df1)

df.to_excel('data/nonpay.xlsx', sheet_name='헬스비급여')
df_nonpay = pd.read_excel('data/nonpay.xlsx', sheet_name='헬스비급여')

# add sheet
df1 = df.copy()
with pd.ExcelWriter('data/nonpay.xlsx', mode='a') as writer:  
    df1.to_excel(writer, sheet_name='헬스비급여_2')
    
print(df_nonpay)

file = open('data/nonpay.json', 'w+')
file.write(json.dumps(jsonObj['item']))
