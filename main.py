from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from  groq import Groq
TOKEN = "8867014686:AAGn_cpcEJ7Ekme_tgo06odR_VOuY_nxSJA"
client = Groq(api_key="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")
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from openai import OpenAI


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا! أرسل أي رسالة وسأحاول الرد عليها.")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text

        response = client.chat.completions.create(
           model="llama-3.3-70b-versatile",

            messages=[
        {"role": "user", "content": user_message}
    ]
        )

        await update.message.reply_text(
    response.choices[0].message.content
)
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ:\n{e}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot Started...")
app.run_polling()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت خدام ✅")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "سلام" in text:
        await update.message.reply_text("وعليكم السلام")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")

    elif "زاد" in text:
        await update.message.reply_text("حبيبي")
    elif "زاد" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif " زاد " in text:
        await update.message.reply_text("غالي")
    elif "زاد" in text:
        await update.message.reply_text("اهلين يا غالي")
    elif "زاد" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
    elif "كيف حالك" in text:
        await update.message.reply_text("بخير الحمد لله")
         
    else:
        await update.message.reply_text("ما فهمتش الرسالة")
async def avatar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    photos = await context.bot.get_user_profile_photos(user.id, limit=1)

    if photos.total_count == 0:
        await update.message.reply_text("ما عندكش صورة بروفايل.")
        return

    file_id = photos.photos[0][-1].file_id

    await update.message.reply_photo(
        photo=file_id,
        caption="📷 هذه صورة بروفايلك."

    )
      
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()