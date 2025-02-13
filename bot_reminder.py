from telegram import Bot
import schedule
import time

TOKEN = "7437071694:AAHLC0efJ-pc9IZIjCCyjyz--8JxaMTi9Xw"
CHAT_ID = "7896128849"

bot = Bot(token=TOKEN)

def enviar_recordatorio():
    print("Enviando recordatorio...")  # <-- Nueva línea para ver en logs
    bot.send_message(chat_id=CHAT_ID, text="¡No olvides tu clase!")

print("Bot iniciado...")  # <-- Nueva línea para ver en logs

schedule.every().day.at("08:00").do(enviar_recordatorio)

while True:
    schedule.run_pending()
    print("Esperando siguiente tarea...")  # <-- Nueva línea para ver en logs
    time.sleep(60)
