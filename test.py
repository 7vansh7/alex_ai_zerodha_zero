import requests 
from bs4 import BeautifulSoup
from api.config import genai,safety_settings
import time
# arr = [1,3,3,23,2,2]
# index_file = open('./index_file.txt','r')
# number = index_file.readlines()
# last_line = int(number[-1].strip()) 

# for x in arr[last_line:]:
#     print(x)
# link_list = []
# with open('./final_link_list.txt','r') as f:
#      for line in f:
#         link_list.append(line.strip())
#      f.close()
# file = open('./unclean_data_file.txt','a')
# for index,x in enumerate(link_list[856:]):
#         print(f'index->{link_list.index(x), index}')
#         response = requests.get(x)
#         response.raise_for_status()  

#         data = BeautifulSoup(response.text, 'html.parser').text
#         file.write(f'{data} +\n')
#         print('written')
# file2 = open('new.txt','a')
# data = open('./unclean_data_file.txt','r').read()
# model = genai.GenerativeModel('gemini-1.5-flash-002',safety_settings=safety_settings)
# chat = model.start_chat()
# data_clean_prompt = f'''The following contains data which needs to be cleaned,
#                                 get all the QUESTIONS-ANSWERS in the data and in this format only 
#                                 question - answer, the data is ->
#                                 {data} '''
# res = chat.send_message(data_clean_prompt).text
# file2.write(res)

data = open('./data_file.txt','r').readlines() 
file_to_write = open('./cleaned.txt','a')
# print(len(data))
# print(data[0:500])
model = genai.GenerativeModel('gemini-1.5-flash-002',safety_settings=safety_settings)
chat = model.start_chat()

# x = int(6750)
# for y in range(7000,13993,250):
text = ''
# print(x,y)
for d in data[13750:13993]:
    text += d
data_clean_prompt = f'''The following data contains questions and answers,
                        REMOVE DUPLICATES and QUESTIONS WITH NO ANSWERS, RETURN REST OF THE DATA AS IT IS
                        the data is being sent over multiple requests as it is quite large

                            {text}'''
res = chat.send_message(data_clean_prompt).text
file_to_write.write(res)
print('written')
