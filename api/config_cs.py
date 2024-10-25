from config import safety_settings,history,genai

functions = {'function_declarations': [
      {'name': 'call_delivery_partner',
       'description': '''this function when called calls the delivery partner and returns the new time till delivery''',
      },{
       'name': "send_email_customer_service",
    'description': "this function sends an email to the customer service of the company when the issue could not be resolved",
}]}

genai.protos.Tool(functions)

def call_delivery_partner():
    return 'from our call i could infer that the delivery partner will be there in 2 minutes'

def send_email_customer_service():
    answer =  """An email has been sent to our customer service department 
    regarding our conversation here , please wait for an email from our customer service """
    return answer

inital_prompt_customer_service = """You are a human customer service assistant for a broker
called Zerodha, your name is Zero,
Give short and humanlike answers, if you cannot think of a proper solution then email the 
customer support team using a function call
- Initially if not asked a question just greet the customer and answer only when the customer asks a question
"""

information_for_customer_service = ''

model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=inital_prompt_customer_service,
                              tools=[send_email_customer_service])

chat_cs = model.start_chat(history=history,enable_automatic_function_calling=True)
