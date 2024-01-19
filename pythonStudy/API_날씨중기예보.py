#파이썬 샘플 코드

import requests
#pip install requests  (라이브러리 다운)
#python API_날씨중기예보.py

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'    #getMidFcst: 사용 함수(불러올 정보)
params ={'serviceKey' : 'f52Z0pl4dINl6+hOeVlqPGQ7p6Nq7tpGyLc8TxlVz1wDEzKyEBQyEAtZPujj5TOJLMblTLiAw0LKH5paWwjCaw==', 
         'pageNo' : '1', 'numOfRows' : '10', 
         'dataType' : 'json', 'stnId' : '133',    #133: 대전
         'tmFc' : '202401110600' }

response = requests.get(url, params=params)
print(response.content)
print(response.encoding)
print(response.text)