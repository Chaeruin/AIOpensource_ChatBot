from openai import OpenAI
import telegram

token = "6476668027:AAFB2RPrne7Q9W1RLzYoAtaE2BpPKTVhD8w"
bot = telegram.Bot(token = token)

def chatGPT():

  # client = OpenAI(
  #   api_key = ""
  # )

  # completion = client.chat.completions.create(
  #   model="gpt-3.5-turbo-1106",
  #   messages=[
  #     {"role": "system", "content": "You are a poetic assistant."},
  #     {"role": "user", "content": "겨울에 대한 시를 써줘. json"}
  #   ],
  #   response_format={"type": "json_object"}
  # )

  # print(completion.choices[0].message.content)
  
  public_chat_name = "@chm1231Test"
  text = "hi!"
  bot.send_message(chat_id=public_chat_name, text=text)

chatGPT()