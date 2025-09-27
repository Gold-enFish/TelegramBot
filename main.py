from telegram import Update, ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, PollAnswerHandler, filters
import asyncio


TOKEN = "8313337149:AAEkr4xruY0CNwDMnL-7gW7mHMfKQx83KzM"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text("Yo! Gue bot lo. Cobain /remind <waktu> <pesan>")
    


# async def hoki(upd:Update, ctx:ContextTypes.DEFAULT_TYPE):
#     import numpy as np

saklarEko = 'off'
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #seorangUser = upd.message.from_user.id
    global saklarEko
    msgnyaUser = update.message.text.strip().lower()

    if msgnyaUser.startswith('/eko'):
        if msgnyaUser.split()[1] == 'on':
            saklarEko = 'on'
            await update.message.reply_text('on bos')

        else:
            saklarEko = 'off'
            await update.message.reply_text('off')
        return

    
    if saklarEko == 'on':
        await update.message.reply_text(update.message.text)

    
async def hokiGame(upd: Update, ctx: ContextTypes.DEFAULT_TYPE):
    import numpy as n
    global jawabn
    lstangka = n.random.randint(1,9,5)
    lststr = map(str,lstangka)
    chatid = upd.message.chat_id
    jawabn = n.random.choice(range(len(lstangka)))
    await upd.message.reply_text('Siap untuk menguji kehokian anda?')
    await ctx.bot.send_poll(chat_id=chatid, type='quiz', question='Pilihlah salah satu dan lihat seberapa hoki anda :>', options=lststr, is_anonymous=False, explanation='aauuuuu', correct_option_id=int(jawabn))
    

async def reaksiPollingan(upd:Update, ctx: ContextTypes.DEFAULT_TYPE):
    # ans = upd.poll_answer
    #pollid = ans.poll_id
    await upd.message.reply_text('yoo')
    # if ans.option_ids and ans.option_ids[0] == jawabn:
    #     await upd.message.reply_text('Siap hoki')
    # else:
    #    await upd.message.reply_text('Siapnda?')

    

# /remind
async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    idPesanOrg =update.message.message_id
    chatid = update.message.chat_id
    await context.bot.setMessageReaction(message_id=idPesanOrg, chat_id=chatid, reaction=[ReactionTypeEmoji(emoji='😱')])
    try:
        
        delay = float(context.args[0][:-1])  # Ambil angka
        unit = context.args[0][-1]        # Ambil huruf (m/d)
        pesan = " ".join(context.args[1:])

       
        # Konversi ke detik
        if unit == "m":
            delay *= 60
        elif unit == "h":
            delay *= 3600
        else:
            await update.message.reply_text("Gunakan format contoh: /remind 10m belajar")
            return

        await update.message.reply_text(f"Oke, gue bakal ingetin '{pesan}' dalam {context.args[0]}")

        # Tunggu delay lalu kirim pesan
        await asyncio.sleep(int(delay))
        await update.message.reply_text(f"⏰ Waktunya: {pesan}")

    except Exception as e:
        await update.message.reply_text("Format salah bro! Contoh: /remind 10m belajar")

async def jokesBafuck2(upd:Update, ctx:ContextTypes.DEFAULT_TYPE):
    import requests as r
    joke = r.get('https://icanhazdadjoke.com/slack').json()
    await upd.message.reply_text(joke['attachments'][0]['fallback'])

async def quote(upd:Update, ctx:ContextTypes.DEFAULT_TYPE):
    import requests as r
    raw = r.get('https://stoic.tekloon.net/stoic-quote')
    katakata = raw.json()
    await upd.message.reply_text('"'+katakata['data']['quote']+'" ~ '+katakata['data']['author'])





def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))
    app.add_handler(CommandHandler("joke", jokesBafuck2))
    app.add_handler(CommandHandler("kata", quote))
    app.add_handler(CommandHandler('cekhoki', hokiGame))
    app.add_handler(PollAnswerHandler(reaksiPollingan))
    app.add_handler(MessageHandler(filters.TEXT,echo))
    print("Botnya dh jalan")
    app.run_polling()

if __name__ == "__main__":
    main()
