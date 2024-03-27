import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

# Función para obtener las cotizaciones de las páginas web
def obtener_cotizaciones():
    urls = ["https://dolarhoy.com/cotizaciondolarblue", "https://dolarhoy.com/cotizacion-dolar-oficial",
            "https://dolarhoy.com/cotizaciondolarbolsa","https://dolarhoy.com/cotizacion-real-brasileno",
            "https://dolarhoy.com/cotizacion-euro"]

    valores = {'Compra': [], 'Venta': []}

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        divs_compra = soup.find_all('div', {'class': 'value'})
        divs_venta = soup.find_all('div', {'class': 'topic'}, string='Venta')

        
        # Obtener valores de compra
        for div in divs_compra:
            valor = div.text
            valores['Compra'].append(valor)
        
        # Obtener valores de venta
        for div in divs_venta:
            venta_div = div.find_next_sibling('div', {'class': 'value'})
            valor_venta = venta_div.text
            valores['Venta'].append(valor_venta)

    return valores

#token bot de Telegram
TOKEN = '6736596743:AAFZVoxxwzJ8vXKf_RdHW3rNfJA8G8E0V9I'
bot = telebot.TeleBot(TOKEN)

# comando /start
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

#botones
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    cotizaciones = obtener_cotizaciones()
    
    if call.data == 'dolar_oficial':
        compra = cotizaciones['Compra'][1]
        venta = cotizaciones['Venta'][1]
        bot.send_message(call.message.chat.id, f"El valor del Dólar oficial hoy es:\nCompra: {compra}\nVenta: {venta}")
    elif call.data == 'dolar_blue':
        compra = cotizaciones['Compra'][0]
        venta = cotizaciones['Venta'][0]
        bot.send_message(call.message.chat.id, f"El valor del Dólar Blue hoy es:\nCompra: {compra}\nVenta: {venta}")
    elif call.data == 'dolar_mep':
        compra = cotizaciones['Compra'][2]
        venta = cotizaciones['Venta'][2]
        bot.send_message(call.message.chat.id, f"El valor del Dólar MEP hoy es:: {compra}\nVenta: {venta}")
    elif call.data == 'real_brasileno':
        compra = cotizaciones['Compra'][3]
        venta = cotizaciones['Venta'][3]
        bot.send_message(call.message.chat.id, f"El valor del Real brasileño hoy es:\nCompra: {compra}\nVenta: {venta}")
    elif call.data == 'euro':
        compra = cotizaciones['Compra'][4]
        venta = cotizaciones['Venta'][4]
        bot.send_message(call.message.chat.id, f"El valor del Euro hoy es:\nCompra: {compra}\nVenta: {venta}")

# Función para ejecutar el bot
def ejecutar_bot():
    bot.polling()

# Inicia el bot en un bucle infinito
if __name__ == "__main__":
    while True:
        try:
            ejecutar_bot()
        except Exception as e:
            print(f"Se produjo un error: {e}")
