from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import random

TOKEN = "asd" #obtener el token de BotFather de telegram

chistes = {
    "animales": [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Por qué el león siempre gana al póker? Porque siempre juega con sus garras.",
        "¿Qué hace un pez en una computadora? Nada.",
        "¿Qué le dice una vaca a otra vaca? ¡Muuuy buenas!",
        "¿Cómo se llama un dinosaurio con un gran vocabulario? Un Thesaurus.",
        "¿Qué le dijo el elefante al ratón? Te tengo miedo, ¡pero te comería!",
        "¿Cuál es el colmo de un cangrejo? Ser un poco picado.",
        "¿Por qué el gallo cruzó la carretera? Para llegar al otro lado.",
        "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
        "¿Qué hace una tortuga en una carrera? ¡Cae lento pero seguro!",
        "¿Por qué los koalas nunca usan el teléfono? Porque siempre tienen que dar un abrazo.",
        "¿Qué hace una serpiente en una fiesta? ¡Serpentea!",
        "¿Por qué el perro se sentó en el reloj? Porque quería ser un relojero.",
        "¿Qué le dijo el pez al océano? ¡Nada de nada!",
        "¿Por qué el pájaro está siempre estresado? Porque está en el aire todo el tiempo.",
        "¿Qué le dijo un perro a otro perro? ¡Qué perrón!",
        "¿Por qué las ranas son tan felices? Porque se la pasan saltando de alegría.",
        "¿Cómo se llama el perro que se pelea con el gato? El perro-pollo.",
        "¿Por qué los caballos no pueden usar Twitter? Porque siempre se exceden en los caracteres."
    ],
    "comida": [
        "¿Por qué el tomate nunca pelea? Porque siempre se pone rojo.",
        "¿Qué le dijo un plátano a una gelatina? ¡Todavía no me he hecho a la idea!",
        "¿Qué hace un pepino en una fiesta? Se pone a la moda.",
        "¿Cuál es el colmo de un pan? Ser un panecillo.",
        "¿Por qué las uvas nunca hacen deportes? Porque siempre se aplastan.",
        "¿Qué le dijo una cebolla a un tomate? ¡Te picas mucho!",
        "¿Qué hace una patata en una carrera? ¡Corriendo de miedo!",
        "¿Por qué las hamburguesas siempre están felices? Porque siempre están acompañadas.",
        "¿Cómo se llama el arroz cuando se siente mal? Arroz en febril.",
        "¿Por qué el aguacate nunca se queja? Porque está siempre en su punto.",
        "¿Qué hace una manzana en una biblioteca? Leen un buen libro.",
        "¿Qué le dice un aguacate a un pan? ¡No me toques, estoy en mi punto!",
        "¿Por qué el chocolate nunca se siente triste? Porque siempre tiene una cobertura dulce.",
        "¿Qué hace un pepino cuando se enoja? Se pone verde.",
        "¿Qué le dijo un tomate a una cebolla? No te pongas tan amarga.",
        "¿Qué hace el pan cuando va al gimnasio? Se pone más fuerte.",
        "¿Por qué las frutas nunca mienten? Porque siempre son honestas.",
        "¿Qué hace un huevo cuando le cuentan un chiste? Se ríe mucho.",
        "¿Qué le dijo el café a la leche? ¡Qué café tan bueno eres!",
        "¿Qué hace un arroz cuando está triste? Se convierte en sopa."
    ],
    "tecnologia": [
        "¿Por qué los programadores prefieren oscuridad? Porque la luz atrae los bugs.",
        "¿Cuántos programadores se necesitan para cambiar una bombilla? Ninguno, eso es un problema de hardware.",
        "¿Qué le dijo un algoritmo a otro? ¡Nos vemos en el ciclo!",
        "¿Por qué los hackers no son buenos en el fútbol? Porque siempre se quedan atrapados en las redes.",
        "¿Qué le dice un software a otro? ¡Eres mi código fuente!",
        "¿Por qué los robots nunca cuentan chistes? Porque sus respuestas son siempre predecibles.",
        "¿Qué le dice un programador a su computadora? ¿Por qué no estás compilando?",
        "¿Cuántos programadores se necesitan para hacer un café? Ninguno, hay una API para eso.",
        "¿Qué le dijo un sistema operativo a otro? ¡Te estoy actualizando!",
        "¿Cómo se llama un grupo de programadores? Un 'bug' de trabajo.",
        "¿Qué le dijo el cable USB a la computadora? ¡Conéctame! Necesito tu ayuda.",
        "¿Por qué los teclados nunca se deprimen? Porque siempre están a la altura.",
        "¿Cómo llamas a un sitio web sin conexión? Un '404' perdido.",
        "¿Qué le dijo un router a otro router? Nos vemos en la red.",
        "¿Por qué los antivirus son tan malos para contar chistes? Porque siempre están buscando problemas.",
        "¿Cómo se llama un teléfono que no puede hacer llamadas? Un 'smartphone' inútil.",
        "¿Por qué la computadora se fue al doctor? Porque tenía un virus.",
        "¿Cómo se llama el error que nunca puedes solucionar? Un 'bug' eterno.",
        "¿Qué le dijo la impresora a la computadora? ¡No me hagas repetir las tareas!",
        "¿Por qué los ordenadores nunca tienen calor? Porque siempre están ventilados."
    ]
}

apodos = [
    "El Crack", "La Máquina", "Súper Estrella", "El Rey del Meme",
    "La Leyenda", "Don Risas", "El Master", "Capitán Alegría",
    "El Genio", "La Estrella Fugaz", "Rey del Desastre", "La Roca",
    "El Increíble", "El Panita", "El Sensei", "El Vengador",
    "La Bestia", "El Ingeniero", "El Jefazo", "La Furia",
]

adivinanzas = [
    {"pregunta": "Vuelo de noche, duermo de día y nunca verás plumas en ala mía. ¿Qué soy?", "respuesta": "El murciélago"},
    {"pregunta": "Tiene dientes pero no come, ¿qué es?", "respuesta": "El peine"},
    {"pregunta": "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera. ¿Qué soy?", "respuesta": "El aguacate"},
    {"pregunta": "Me pelan con cuidado, no porque lastime, sino porque lloro. ¿Qué soy?", "respuesta": "La cebolla"},
    {"pregunta": "Oro parece, plata no es. ¿Qué es?", "respuesta": "El plátano"},
    {"pregunta": "Llevo años en la tierra, pero sigo verde. ¿Qué soy?", "respuesta": "El árbol"},
    {"pregunta": "Siempre estoy entre dos montañas pero nunca me muevo. ¿Qué soy?", "respuesta": "El valle"},
    {"pregunta": "Tengo hojas pero no soy árbol, tengo espinas pero no soy rosa. ¿Qué soy?", "respuesta": "El libro"},
    {"pregunta": "Aunque tengo cuatro patas, no sé andar. ¿Qué soy?", "respuesta": "La mesa"},
    {"pregunta": "Voy por el agua, pero no me mojo. ¿Qué soy?", "respuesta": "La sombra"},
    {"pregunta": "Si me nombras, desaparezco. ¿Qué soy?", "respuesta": "El silencio"},
    {"pregunta": "¿Qué cosa cuanto más le quitas más grande es?", "respuesta": "Un agujero"},
    {"pregunta": "Cuando estoy lleno, peso menos. ¿Qué soy?", "respuesta": "El globo"},
    {"pregunta": "Cien amigos tengo, todos en fila, si uno se cae, todos lo imitan. ¿Qué soy?", "respuesta": "El dominó"},
    {"pregunta": "No es cama ni es león y desaparece en cualquier rincón. ¿Qué es?", "respuesta": "El camaleón"},
    {"pregunta": "Es tuyo pero lo usan más los demás. ¿Qué es?", "respuesta": "Tu nombre"},
    {"pregunta": "Tiene orejas pero no puede oír. ¿Qué es?", "respuesta": "La olla"},
    {"pregunta": "Me rompo si me nombras. ¿Qué soy?", "respuesta": "El secreto"},
    {"pregunta": "No tengo pies pero corro, no tengo ojos pero lloro. ¿Qué soy?", "respuesta": "El río"},
    {"pregunta": "Siempre subo pero nunca bajo. ¿Qué soy?", "respuesta": "La edad"},
]

# Funciones del bot
async def start(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    keyboard = [
        [
            InlineKeyboardButton("📖 Leer Libro", callback_data='libro'),
            InlineKeyboardButton("🎶 Escuchar Música", callback_data='musica')
        ],
        [
            InlineKeyboardButton("📢 Contar Chiste", callback_data='chiste'),
            InlineKeyboardButton("📛 Generar Apodo", callback_data='apodo')
        ],
        [
            InlineKeyboardButton("😂 Ban Gracioso", callback_data='ban'),
            InlineKeyboardButton("🤫 Botón del Silencio", callback_data='silencio'),
        ],
        [
            InlineKeyboardButton("❓ Resolver Adivinanza", callback_data='adivinanza'),
            InlineKeyboardButton("⚙️ Configuración", callback_data='configuracion')
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"¡Hola, {user}! 👋 Soy tu bot de diversión. ¿Qué te gustaría hacer hoy?",
        reply_markup=reply_markup
    )

async def chiste(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🐶 Chistes de Animales", callback_data='chiste_animales')],
        [InlineKeyboardButton("🍔 Chistes de Comida", callback_data='chiste_comida')],
        [InlineKeyboardButton("💻 Chistes de Tecnología", callback_data='chiste_tecnologia')],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        "¡Elige el tipo de chiste que quieres escuchar! 🤡",
        reply_markup=reply_markup
    )

# Función para mostrar un chiste aleatorio de animales
async def chiste_animales(update: Update, context: CallbackContext):
    chiste_aleatorio = random.choice(chistes["animales"])
    keyboard = [
        [InlineKeyboardButton("Otro chiste de Animales", callback_data='chiste_animales')],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        chiste_aleatorio,
        reply_markup=reply_markup
    )

# Función para mostrar un chiste aleatorio de comida
async def chiste_comida(update: Update, context: CallbackContext):
    chiste_aleatorio = random.choice(chistes["comida"])
    keyboard = [
        [InlineKeyboardButton("Otro chiste de Comida", callback_data='chiste_comida')],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        chiste_aleatorio,
        reply_markup=reply_markup
    )

# Función para mostrar un chiste aleatorio de tecnología
async def chiste_tecnologia(update: Update, context: CallbackContext):
    chiste_aleatorio = random.choice(chistes["tecnologia"])
    keyboard = [
        [InlineKeyboardButton("Otro chiste de Tecnología", callback_data='chiste_tecnologia')],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        chiste_aleatorio,
        reply_markup=reply_markup
    )
async def contar_chiste(update: Update, context: CallbackContext):
    tipo = update.callback_query.data.split('_')[1]
    joke = random.choice(chistes[tipo])
    await update.callback_query.edit_message_text(f"😂 Aquí tienes un chiste:\n\n{joke}")

async def apodo(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    nickname = random.choice(apodos)
    await update.callback_query.edit_message_text(f"📛 {user}, Tu nuevo apodo es:\n\n{nickname}")
    await update.callback_query.message.reply_text(
        "¡Que disfrutes tu nuevo apodo! 😎"
    )

async def adivinanza(update: Update, context: CallbackContext):
    riddle = random.choice(adivinanzas)
    question = riddle["pregunta"]
    answer = riddle["respuesta"]
    keyboard = [
        [InlineKeyboardButton("Mostrar Respuesta", callback_data=f'respuesta-{answer}')],
        [InlineKeyboardButton("Otra Adivinanza", callback_data='otra_adivinanza')],
        [InlineKeyboardButton("Volver al menú principal", callback_data='start')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(f"❓ Adivinanza:\n\n{question}", reply_markup=reply_markup)

async def mostrar_respuesta(update: Update, context: CallbackContext):
    answer = update.callback_query.data.split('-')[1]
    await update.callback_query.edit_message_text(f"✅ Respuesta: {answer}")

async def ban_gracioso(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    await update.callback_query.edit_message_text(
        f"😂 {user}, has sido *baneado de mentiritas*. ¡Mejor compórtate! (Es solo una broma).",
        parse_mode='Markdown'
    )

async def boton_silencio(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    await update.callback_query.edit_message_text(f"🤫 {user} activó el botón del silencio. ¡Silencio en el grupo! (shhh...)")
    keyboard = [[InlineKeyboardButton("🔊 Activar Sonido", callback_data='activar_sonido')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "¿Quieres activar el sonido de nuevo? 🔊", reply_markup=reply_markup
    )

async def activar_sonido(update: Update, context: CallbackContext):
    await update.callback_query.edit_message_text("🔊 ¡Sonido activado! 🎶")

async def configuracion(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🔔 Notificaciones", callback_data='notificaciones')],
        [InlineKeyboardButton("📋 Ver mi Perfil", callback_data='perfil')],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text("⚙️ Configuración:", reply_markup=reply_markup)

async def musica(update: Update, context: CallbackContext):
    lista_musica = {
        1: {"nombre": "Alan Walker - Faded", "url": "https://evolucionlcz.s3.us-east-2.amazonaws.com/61d0e75bd22bff.mp3"},
        2: {"nombre": "Alan Walker & Ava Max - Alone. Pt. II", "url": "https://evolucionlcz.s3.us-east-2.amazonaws.com/139cc1e3fbef97.mp3"}
    }
    await update.callback_query.edit_message_text("🎶 Aquí tienes tus canciones favoritas... 🎧")
    
    mensaje = "🎵 Escucha tus canciones favoritas:\n\n"
    
    for musica_id, musica_info in lista_musica.items():
        nombre_cancion = musica_info["nombre"]
        musica_url = musica_info["url"]
        mensaje += f"• *{nombre_cancion}* [Haz clic para escuchar]({musica_url})\n"
    
    await update.callback_query.message.reply_text(mensaje, parse_mode="Markdown")

async def libro(update: Update, context: CallbackContext):
    libro_url = "https://evolucionlcz.s3.us-east-2.amazonaws.com/dc09e6148168be.pdf"
    query = update.callback_query
    await query.edit_message_text(
        f"📖 ¡Ahora te cuento una historia interesante! \n\n"
        f"Haz clic en el siguiente enlace para abrir el libro: [Leer Libro]({libro_url})",
        parse_mode="Markdown",
    )

async def help_command(update: Update, context: CallbackContext):
    help_text = """
    🤖 ¡Soy tu bot de diversión! Aquí están mis comandos:
    - /start: Comienza a interactuar conmigo.
    - 📢 Chistes Aleatorios: ¡Recibe un chiste aleatorio!
    - 📛 Generador de Apodos: ¡Te doy un apodo divertido!
    - ❓ Adivinanzas: Resuelve adivinanzas interesantes.
    - 😂 Ban Gracioso: ¡Hazme un chiste de broma!
    - 📖 Leer Libro: Disfruta de una buena lectura.
    - 🎶 Escuchar Música: Escucha tus canciones favoritas.
    """
    await update.message.reply_text(help_text)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(chiste, pattern='^chiste$'))
    application.add_handler(CallbackQueryHandler(contar_chiste, pattern='^chiste_(.*)$'))
    application.add_handler(CallbackQueryHandler(apodo, pattern='^apodo$'))
    application.add_handler(CallbackQueryHandler(adivinanza, pattern='^adivinanza$'))
    application.add_handler(CallbackQueryHandler(mostrar_respuesta, pattern='^respuesta-'))
    application.add_handler(CallbackQueryHandler(ban_gracioso, pattern='^ban$'))
    application.add_handler(CallbackQueryHandler(boton_silencio, pattern='^silencio$'))
    application.add_handler(CallbackQueryHandler(activar_sonido, pattern='^activar_sonido$'))
    application.add_handler(CallbackQueryHandler(configuracion, pattern='^configuracion$'))
    application.add_handler(CallbackQueryHandler(musica, pattern='^musica$'))
    application.add_handler(CallbackQueryHandler(libro, pattern='^libro$'))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()

if __name__ == '__main__':
    main()
