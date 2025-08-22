from uu import encode
import requests  
from bs4 import BeautifulSoup  
  

base_currency = 'USD'  
target_currency = 'HKD'     # 假设你有一个API或网页URL可以获取汇率  
url = f"https://wise.com/zh-cn/currency-converter/{target_currency}-to-{base_currency}-rate?amount=1"  # 替换为实际的URL  
print(url)
response = requests.get(url)  
response.raise_for_status()  # 如果请求失败，抛出异常  


soup = BeautifulSoup(response.text,'lxml')
    # 假设汇率信息在一个id为'exchange-rate-value'的元素中  
obj = soup.find('span',class_='text-success').get_text()
print(obj) 
#print(soup.find_all("p"))