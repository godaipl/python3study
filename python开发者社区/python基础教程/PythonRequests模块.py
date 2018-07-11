import requests

base_url = 'http://www.pythontab.com'

response1 = requests.get(base_url)  # 生成response对象
print(response1.status_code)
print(response1.headers)
print(response1.encoding)
print(response1.content)

# 传递参数
params = {'version': 'python3', 'keywords': 'pythontab'}
response2 = requests.get(base_url, params)

print(response2.status_code)

# 原始响应内容
response3 = requests.get(base_url, stream=True)
print(response3.raw.read(10))

# 定制请求头
headers = {'content-type': 'application/json'}
response4 = requests.post(base_url, data=params, headers=headers)

print(response4.status_code)
print(response4.content)
