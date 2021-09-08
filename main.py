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

import requests
from bs4 import BeautifulSoup as bs

api_key = "4fw71cT9NmHBLiTdlrZJS5BZ6VaGfRZUdpzpDVssN6OImKE8WcKzLlpRqq1HY7C%2F6Y%2BV1M9mngsqOXYLXJ624w%3D%3D"
URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11110&DEAL_YMD=201512&serviceKey='+api_key

URL_O = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
land_code=str(11110)
deal_date = str(201512)
page_no = str(2)
numofrows = str(20)
LAND_CODE = '?LAWD_CD=' + land_code
DEAL_DATE = '&DEAL_YMD=' + deal_date
PAGE_NO = '&pageNo=' + page_no
NUMROWS = '&numOfRows=' + numofrows
URL_SK = '&serviceKey='+api_key

URL_ALL = URL_O + LAND_CODE + DEAL_DATE + PAGE_NO + NUMROWS + URL_SK
URL_ALL1 = URL
req = requests.get(URL_ALL)

soup = bs(req.content, 'html.parser')
print(soup.prettify())
print('*'*100)

land = soup.find_all('item')

for trade in land:
    for t in trade.contents:
        print(t, end=', ')
    print("")