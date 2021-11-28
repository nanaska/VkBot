from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, EMPTY_KEYBOARD
from vkbottle.tools.dev_tools.uploader.photo import PhotoMessageUploader

TOKEN = "b1d1c0417c5354cfb9dfaf361e5d3ba07bae3ea1ec0ed6bd31c0ef298af0e8eb06d000f340d95cb7aeed8"
bot = Bot(token=TOKEN)

@bot.on.message(text="Начать")
async def hi_handler(message: Message):
    
    keyboard = Keyboard(one_time=True, inline=False)  
    keyboard.add(Text("Обучение в автошколе"), color=KeyboardButtonColor.PRIMARY)  # Первая строка (ряд) добавляется автоматически
    keyboard.row()  # Переходим на следующую строку 
    keyboard.add(Text("О нас"), color=KeyboardButtonColor.PRIMARY)
    print(3)
    keyboard.add(Text("Цены"), color=KeyboardButtonColor.PRIMARY)
    
    await message.answer("Автошкола ЗА РУЛЁМ приветствует вас", keyboard=keyboard.get_json() )
@bot.on.message(text="Обучение в автошколе")
async def hi_handler(message: Message):
    
    keyboard = Keyboard(one_time=True, inline=False)  
    keyboard.add(Text("Обучение в автошколе"), color=KeyboardButtonColor.PRIMARY)  # Первая строка (ряд) добавляется автоматически
    keyboard.row()  # Переходим на следующую строку 
    keyboard.add(Text("О нас"), color=KeyboardButtonColor.PRIMARY)
    print(3)
    keyboard.add(Text("Цены"), color=KeyboardButtonColor.PRIMARY)
    
    await message.answer("В нашей автошколе самое лучшее обучение", keyboard=keyboard.get_json(),attachment="photo-209113278_457239018" )    
    
@bot.on.message(text="О нас")
async def hi_handler(message: Message):
    
    keyboard = Keyboard(one_time=True, inline=False)  
    keyboard.add(Text("Обучение в автошколе"), color=KeyboardButtonColor.PRIMARY)  # Первая строка (ряд) добавляется автоматически
    keyboard.row()  # Переходим на следующую строку 
    keyboard.add(Text("О нас"), color=KeyboardButtonColor.PRIMARY)
    print(3)
    keyboard.add(Text("Цены"), color=KeyboardButtonColor.PRIMARY)
    
    await message.answer("Мы самые лучшие", keyboard=keyboard.get_json() )    

@bot.on.message(text="Цены")
async def hi_handler(message: Message):
    
    keyboard = Keyboard(one_time=True, inline=False)  
    keyboard.add(Text("План 1"), color=KeyboardButtonColor.PRIMARY)  # Первая строка (ряд) добавляется автоматически
    
    keyboard.add(Text("План 2"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    
    keyboard.add(Text("Назад"), color=KeyboardButtonColor.PRIMARY)
    
    await message.answer("Выберите план",keyboard=keyboard.get_json() )   
@bot.on.message(text="План 1")
async def hi_handler(message: Message):
    keyboard = Keyboard(one_time=True, inline=False)   
    keyboard.add(Text("Назад"), color=KeyboardButtonColor.PRIMARY) 
    await message.answer("Цена: 5000, \n в эту стоимость входит то и то" ,keyboard=keyboard.get_json() ) 
@bot.on.message(text="План 2")
async def hi_handler(message: Message):
    keyboard = Keyboard(one_time=True, inline=False)   
    keyboard.add(Text("Назад"), color=KeyboardButtonColor.PRIMARY)    
    await message.answer("Цена: 10000 \n в эту стоимость входит то и то" ,keyboard=keyboard.get_json() )  
@bot.on.message(text="Назад")
async def hi_handler(message: Message):
    keyboard = Keyboard(one_time=True, inline=False)  
    keyboard.add(Text("Обучение в автошколе"), color=KeyboardButtonColor.PRIMARY)  # Первая строка (ряд) добавляется автоматически
    keyboard.row()  # Переходим на следующую строку 
    keyboard.add(Text("О нас"), color=KeyboardButtonColor.PRIMARY)
    print(3)
    keyboard.add(Text("Цены"), color=KeyboardButtonColor.PRIMARY)
    
    await message.answer("Автошкола ЗА РУЛЁМ приветствует вас", keyboard=keyboard.get_json() ) 
       
@bot.on.private_message(text="test2")
async def hi_handler(message: Message):
    await message.answer("Ого, я отвечаю в ЛС")

@bot.on.chat_message(text="test3")
async def hi_handler(message: Message):
    await message.answer("Ого, я отвечаю в беседе")

bot.run_forever()