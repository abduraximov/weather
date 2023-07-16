from telegram import Update
from weather import result
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

city = ''


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name},'
                                    f'city: {city} ,This bot can help get information about weather')


async def week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global city
    if city:
        data = result(city)
        print(data)
        if 'error' in data:
            await update.message.reply_text(data['error'])
        else:
            for forecast in data['forecast']['forecastday']:
                await update.message.reply_text(f"Day : {forecast['date']} \n"
                                                f"Information: max temp: {forecast['day']['maxtemp_c']},"
                                                f"min temp: {forecast['day']['mintemp_c']}")
    else:
        await update.message.reply_text('Please set a location using /set_location command.')


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global city
    if city:
        data = result(city)
        print(data)
        if 'error' in data:
            await update.message.reply_text(data['error'])
        else:
            print(data)
            await update.message.reply_text(f'Location: {data["location"]["name"]}, {data["location"]["country"]} \n'
                                            f'Information: {data["current"]["last_updated"]},'
                                            f' Now: {data["current"]["temp_c"]}, '
                                            f'feels like: {data["current"]["feelslike_c"]}')
        # await update.message.reply_text(f'')
    else:
        await update.message.reply_text('Please set a location using /set_location command.')


async def set_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global city
    message = " ".join(context.args)
    if message:
        city = message
        await update.message.reply_html(f'You entered <b>{city}</b>')
    # await update.message.reply_text()


app = ApplicationBuilder().token("5368564096:AAFOOYskEIdi_Mt5rSlJ6jBh0DRFd6Da2qQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("set_location", set_location))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler("week", week))

app.run_polling()
