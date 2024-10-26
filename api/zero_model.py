from config import genai,safety_settings
import yfinance as yf
# <<<<<<<- Questions ->>>>>>>
# Should i invest in EV company stocks 
# What are my holdings 
# Add 30TCS shares to my holdings 
# How was the market today 
# Can my shares be transferred to my child who is a minor 
# What is Zerodha coin
# How to freeze/unfreeze stocks in my demat 
#    <<<<<<<- End ->>>>>>>

file = open('../txt_files/final_cleaned_data.txt','r')
zerodha_info_data = file.read()

account_info = {
    "Name":"Ansh Makhija",
    "Holdings":"10HCL, 50TCS, 100TATA"
}

functions = {'function_declarations': [{
       'name': "send_email_customer_service",
    'description': "this function sends an email to the customer service of the company when the issue could not be resolved",
},{
       'name': " zerodha_customer_service_answers_data",
    'description': "This contains question answer data about Zerodha that could be useful answer user queries ",
    'parameters': {'type_': 'OBJECT',
       'properties': {
         'a': {'type_': 'STRING'},
       },
       'required': ['a']}
},{
       'name': "get_account_info",
    'description': "This could be used to get the user's account information like holdings, name, etc ",
},{
       'name': "market_info",
    'description': "When the user requires basic market information ",
},{
       'name': "place_stock_order",
    'description': "When the user asks to place a order of stock, requires the stock name and quantity",
    'parameters': {'type_': 'OBJECT',
       'properties': {
         'a': {'type_': 'STRING'},
         'b': {'type_':'INTEGER'}
       },
       'required': ['a','b']}
}]}
genai.protos.Tool(functions)

def place_stock_order(stock_name:str,quantity:int):
    return f"Your order was placed for {quantity} {stock_name} shares "

def market_info():
    return "Today NIFT50 Dipped by 0.50%, investors are bearish"
    
def get_account_info():
    return f'This is the customer account info -> {account_info}'

def  zerodha_customer_service_answers_data(question:str):
    prompt = f'''You are provided with Zerodha customer service data, answer based on the data
                    {zerodha_info_data}'''
    model2 = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=prompt)
    chat2 = model2.start_chat(history=[])
    res = chat2.send_message(f'Question-> {question}').text
    return res

def send_email_customer_service():
    answer =  """An email has been sent to our customer service department 
    regarding our conversation here , please wait for an email from our customer service """
    return answer

def stocl_info(stock_name:str):
    pass


initiation_prompt = f"""You are a HUMAN ASSISTANT for a broker
called Zerodha, your name is Zero, GIVE INVESTMENT ADVICE, answer stock market questions,
HELP IN RESEARCH
Give short and humanlike answers, if you cannot think of a proper solution then email the 
customer support using a function call
- Initially if not asked a question just Greet the customer with your name
- Use function calling for placing stock order, getting market updates, getting account info 
- If asked a question about Zerodha, use the zerodha_customer_service_answers_data function
"""
# - The following is the data which can be used to clear user queries {zerodha_info_data}, use it when required otherwise 
# not 

history = []
model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=initiation_prompt,tools=[place_stock_order,
                                                                          market_info,send_email_customer_service,
                                                                           zerodha_customer_service_answers_data,get_account_info])
print('Model Initiated')
zero_chat = model.start_chat(history=history,enable_automatic_function_calling=True)
# print('Sending Data Prompt')
# print(chat.send_message('hello').text)

# while True:
#     text = input('Ask- ')
#     res = chat.send_message(text,stream=False)
#     print(res.text)
