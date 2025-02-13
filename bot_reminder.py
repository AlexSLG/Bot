import time
import schedule
from telegram import Bot

TOKEN = "7437071694:AAHLC0efJ-pc9IZIjCCyjyz--8JxaMTi9Xw"
CHAT_ID = 7896128849  # Asegúrate de que esté correcto

bot = Bot(token=TOKEN)

def enviar_recordatorio():
    print("Enviando recordatorio...")
    bot.send_message(chat_id=CHAT_ID, text="¡No olvides tu clase!")

def iniciar_bot():
    print("Bot iniciado...")

    # Define el horario del recordatorio
    schedule.every().day.at("08:00").do(enviar_recordatorio)
    
    # Ejecutar el planificador
    while True:
        schedule.run_pending()
        time.sleep(60)  # Espera 1 minuto antes de volver a ejecutar el código

if __name__ == "__main__":
    iniciar_bot()
