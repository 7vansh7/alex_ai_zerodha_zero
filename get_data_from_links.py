import requests 
from bs4 import BeautifulSoup
from api.config import genai,safety_settings

model = genai.GenerativeModel('gemini-1.5-flash-002',safety_settings=safety_settings)
chat = model.start_chat()
link_list = []
with open('./final_link_list.txt','r') as f:
     for line in f:
        link_list.append(line.strip())
     f.close()

file_to_write = open('./data_file.txt','a')

try:
    for index,x in enumerate(link_list[214:]):
        print(f'index->{index}')
        response = requests.get(x)
        response.raise_for_status()  

        data = BeautifulSoup(response.text, 'html.parser').text
        data_clean_prompt = f'''The following contains data which needs to be cleaned,
                                get all the QUESTIONS-ANSWERS in the data and in this format only 
                                question - answer, the data is ->
                                {data} '''
        res = chat.send_message(data_clean_prompt).text
        file_to_write.write(f'{res}\n')
        print('written\n')

except Exception as e:
    print(x, f'\n{link_list.index(x)}')
    print(e)
