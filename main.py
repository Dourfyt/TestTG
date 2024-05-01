import telebot
import psycopg2



token = '6501489744:AAEVS3aoQG1JsbkJBWRdTWw7__JuWJvF43w'
bot = telebot.TeleBot(token)



conn = psycopg2.connect(dbname='test', user='testuser', 
                        password='test', host='localhost')
cursor = conn.cursor()



def set_task(message):
    cursor.execute('''INSERT INTO tasks (task) VALUES (%s)''', (message.text,))
    conn.commit()
    bot.send_message(message.chat.id, "Запись успешно добавлена!")




def get_tasks(message):
    cursor.execute("""SELECT * FROM tasks""")
    records = cursor.fetchall()
    counter = 1
    text = 'Вот список задач:\n'
    for row in records:
        task_text = row[2]
        text = text + f"\n{counter}. {task_text}\n"
        counter=counter+1
    bot.send_message(message.chat.id, text)
    
    
    
@bot.message_handler(commands=['start','add','tsk'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Данный бот предназначен для занесения и вывода записей в БД Postgres')
    elif message.text == '/add':
        msg = bot.send_message(message.chat.id, 'Введите задачу')
        bot.register_next_step_handler(msg, set_task)
    elif message.text == '/tsk':
        bot.send_message(message.chat.id, 'Вот список задач')
        get_tasks(message)
        
        
        
bot.polling(none_stop=True)