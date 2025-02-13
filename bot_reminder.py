from telegram import Bot
import schedule
import time

# Reemplaza con tu token del BotFather
TOKEN = "7437071694:AAHLC0efJ-pc9IZIjCCyjyz--8JxaMTi9Xw"
CHAT_ID = "@ReminderGPT_bot"  # Puedes obtenerlo enviándole un mensaje a tu bot y revisando la API de Telegram

bot = Bot(token=TOKEN)

def enviar_recordatorio():
    bot.send_message(chat_id=CHAT_ID, text="¡No olvides tu clase!")

# Configurar el horario (por ejemplo, todos los días a las 8:00 AM)
schedule.every().day.at("15:00").do(enviar_recordatorio)

while True:
    schedule.run_pending()
    time.sleep(60)  # Revisar cada minuto si es hora de enviar el mensaje
