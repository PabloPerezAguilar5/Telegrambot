

**Bot de Cotización de Moneda**
<br>

Este es un bot de Telegram que proporciona cotizaciones de diferentes tipos de moneda, incluyendo el dólar oficial, el dólar blue, el dólar MEP, el real brasileño y el euro. El bot muestra tanto los valores de compra como de venta de cada moneda en tiempo real usando tecnicas de web scraping con la web dolarhoy.com.

Funcionamiento
El bot responde a los siguientes comandos:

/start: Inicia la interacción con el bot y muestra un mensaje de bienvenida junto con un menú de botones para seleccionar el tipo de moneda.
El bot utiliza la librería requests para realizar solicitudes HTTP a las páginas web que contienen las cotizaciones, y BeautifulSoup para analizar el HTML y extraer los datos relevantes.

Uso:
Clona este repositorio a tu máquina local:
git clone https://github.com/PabloPerezAguilar5/Telegrambot.git
Instala las dependencias necesarias:
pip install -r requirements.txt
Configura el token del bot de Telegram en el archivo main.py.

Ejecuta el bot:

python main.py
Interactúa con el bot en tu aplicación de Telegram.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor crea un issue o envía un pull request.

Autor
@PabloPerezAguilar5

---

Currency Quote Bot
This is a Telegram bot that provides quotes for different types of currencies, including the official dollar, the blue dollar, the MEP dollar, the Brazilian real, and the euro. The bot shows both the purchase and sale values of each currency in real time using web scraping techniques from the dolarhoy.com website.

Functioning
The bot responds to the following commands:

/start: Starts the interaction with the bot and displays a welcome message along with a menu of buttons to select the currency type.
The bot uses the requests library to make HTTP requests to the web pages containing the quotes, and BeautifulSoup to parse the HTML and extract the relevant data.

Use:
Clone this repository to your local machine:
git clone https://github.com/PabloPerezAguilar5/Telegrambot.git
Install the necessary dependencies:
pip install -r requirements.txt
Configure the Telegram bot token in the main.py file.

Run the bot:
python main.py
Interact with the bot in your Telegram application.
Contributions
Contributions are welcome. If you encounter any problems or have any suggestions for improvement, please create an issue or submit a pull request.

Author
@pabloperezAguilar5
