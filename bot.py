from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# تكوين نظام التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    try:
        # رسالة ترحيبية بأهمية الإسعافات الأولية
        message = (
            f"🚑 *مرحباً {user.first_name}!*\n\n"
            "🌟 *مرحباً بك في بوت دورة الإسعافات الأولية!*\n\n"
            "تكتسب مهارات الإسعافات الأولية أهمية بالغة للأسباب التالية:\n"
            "------------------------------------------------\n"
            "1️⃣ *إنقاذ الأرواح*: قد تكون الوحيد القادر على التدخل السريع قبل وصول المساعدة الطبية\n\n"
            "2️⃣ *الوقاية من المضاعفات*: الرعاية الأولى الصحيحة تمنع تفاقم الإصابات\n\n"
            "3️⃣ *المسؤولية المجتمعية*: معرفة الإسعافات تجعلك عضواً فاعلاً في مجتمعك\n\n"
            "4️⃣ *الثقة في الطوارئ*: التمكن من التعامل مع الحالات الطارئة بثبات أعصاب\n\n"
            "✅ *تساعدك هذه الدورة على:*\n"
            "   - التعرف على الحالات الطارئة\n"
            "   - تطبيق الإسعافات بشكل آمن\n"
            "   - التعامل مع النزيف والحروق والكسور\n"
            "   - إنعاش القلب والرئتين\n\n"
            "⌛ *طرق الانقاذ تتحكم في 50% من نتائج الحالات الطارئة قبل وصول المستشفى*\n\n"
            "للتسجيل في الدورة والحصول على شهادة معتمدة، انقر على الزر أدناه:"
        )
        
        # إنشاء زر التسجيل مع أيقونة
        web_app_url = "https://cammeral.github.io/AID2test/"
        register_button = InlineKeyboardButton(
            text="📝 البدء بالتسجيل", 
            web_app=WebAppInfo(url=web_app_url)
        )
        
        keyboard = InlineKeyboardMarkup([[register_button]])
        
        # إرسال الرسالة مع تنسيق Markdown
        await update.message.reply_text(
            text=message,
            reply_markup=keyboard,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
        
    except Exception as e:
        logger.error(f"حدث خطأ: {e}")
        await update.message.reply_text("⚠️ عذراً، حدث خطأ تقني. يرجى المحاولة مرة أخرى لاحقاً.")

def main() -> None:
    TOKEN = "7679921112:AAFC59eo9mI47vmhgqJKsrs5OnOZgQGZGCY"
    
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        logger.info("🔥 البوت يعمل بنجاح...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"خطأ في التشغيل: {e}")

if __name__ == "__main__":
    main()
