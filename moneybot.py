import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

def obtener_cotizacion(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        
       
        div_compra = soup.find('div', string='Compra')
        div_venta = soup.find('div', string='Venta')
        
        if div_compra and div_venta:
            
            compra = div_compra.find_next_sibling('div', class_='value').text.strip()
            venta = div_venta.find_next_sibling('div', class_='value').text.strip()
            return {'Compra': compra, 'Venta': venta}
        else:
            return {'Error': 'No se encontraron los valores de compra y venta'}
    
    except requests.RequestException as e:
        return {'Error': f'Error al obtener la cotización: {e}'}


TOKEN = '6736596743:AAFZVoxxwzJ8vXKf_RdHW3rNfJA8G8E0V9I'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy un bot que te proporciona la cotización de diferentes tipos de moneda en Argentina en tiempo real")
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("Dólar Oficial", callback_data='dolar_oficial'),
               types.InlineKeyboardButton("Dólar Blue", callback_data='dolar_blue'),
               types.InlineKeyboardButton("Dólar MEP", callback_data='dolar_mep'))
    markup.row(types.InlineKeyboardButton("Real Brasileño", callback_data='real_brasileno'),
               types.InlineKeyboardButton("Euro", callback_data='euro'))
    bot.send_message(message.chat.id, "Selecciona la moneda:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    
    urls = {
        'dolar_oficial': "https://dolarhoy.com/cotizacion-dolar-oficial",
        'dolar_blue': "https://dolarhoy.com/cotizaciondolarblue",
        'dolar_mep': "https://dolarhoy.com/cotizaciondolarbolsa",
        'real_brasileno': "https://dolarhoy.com/cotizacion-real-brasileno",
        'euro': "https://dolarhoy.com/cotizacion-euro"
    }
    url = urls.get(call.data)
    
   
    cotizacion = obtener_cotizacion(url)
    
   
    if 'Error' in cotizacion:
        bot.send_message(call.message.chat.id, f"Error: {cotizacion['Error']}")
    else:
        compra = cotizacion['Compra']
        venta = cotizacion['Venta']
        bot.send_message(call.message.chat.id, f"El valor del {call.data.replace('_', ' ').title()} hoy es:\nCompra: {compra}\nVenta: {venta}")


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8443))
    bot.polling(none_stop=True, interval=0, timeout=20)
