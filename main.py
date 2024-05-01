import telebot
import psycopg2
import config

bot = telebot.TeleBot(config.token)



conn = psycopg2.connect(dbname='test', user='testuser', 
                        password='test', host='localhost')
cursor = conn.cursor()



def set_task(message):
    cursor.execute('''INSERT INTO tasks (task, user_id) VALUES (%s, %s)''', (message.text, message.from_user.id))
    conn.commit()
    bot.send_message(message.chat.id, "Запись успешно добавлена!")



def get_tasks(message):
    cursor.execute("""SELECT * FROM tasks WHERE user_id = '%s'""", (message.from_user.id,))
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
        get_tasks(message)
        
        
        
bot.polling(none_stop=True)