# # 공공데이터 API 호출하기 - 부동산 실거래가
# * https://www.data.go.kr/
# * https://www.data.go.kr/dataset/3050988/openapi.do
#
# # API 사용 신청하기
# * 공공데이터는 사용 신청을 해야 사용할 수 있음.
#
# # 시크릿 발급하기
# * 한 입에 웹 크롤링

import requests
from bs4 import BeautifulSoup as bs

URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
api_key = "4fw71cT9NmHBLiTdlrZJS5BZ6VaGfRZUdpzpDVssN6OImKE8WcKzLlpRqq1HY7C%2F6Y%2BV1M9mngsqOXYLXJ624w%3D%3D"
api_key_decode = requests.utils.unquote(api_key)
parameters = {"ServiceKey": api_key, "numOfROws": 10, "pageNo": 1, "LAWD_CD": 11110, "DEAL_YMD": 201512}
req = requests.get(URL, params=parameters)

soup = bs(req.content, 'html.parser')

print(soup.prettify())

