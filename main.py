import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# دریافت توکن از متغیر محیطی (در render تنظیم می‌شود)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# منوی اصلی
main_keyboard = ReplyKeyboardMarkup(
    [["📦 مشاهده کاتالوگ محصولات"], ["ℹ️ درباره ما", "📞 تماس با ما"]],
    resize_keyboard=True
)

# زیرمنوی کاتالوگ
catalog_keyboard = ReplyKeyboardMarkup(
    [["🛁 شیرآلات البرز", "🟣 محصولات پرنیان", "🔴 محصولات آلتون"], ["🔙 بازگشت"]],
    resize_keyboard=True
)

# تابع شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات شرکت توکل تجارت اسپادانا خوش آمدید 🌐\nلطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=main_keyboard
    )

# مدیریت پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 مشاهده کاتالوگ محصولات":
        await update.message.reply_text("یکی از برندهای زیر را انتخاب کنید:", reply_markup=catalog_keyboard)

    elif text == "🛁 شیرآلات البرز":
        await send_pdf(update, "pdfs/alborz.pdf", "📄 کاتالوگ شیرآلات البرز")

    elif text == "🟣 محصولات پرنیان":
        await send_pdf(update, "pdfs/parnian.pdf", "📄 کاتالوگ محصولات پرنیان")

    elif text == "🔴 محصولات آلتون":
        await send_pdf(update, "pdfs/altun.pdf", "📄 کاتالوگ محصولات آلتون")

    elif text == "🔙 بازگشت":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)

    elif text == "ℹ️ درباره ما":
        await update.message.reply_text(
            "شرکت *توکل تجارت اسپادانا* با هدف ارائه بهترین و باکیفیت‌ترین محصولات بهداشتی و ساختمانی فعالیت خود را آغاز کرده است.\n"
            "این مجموعه با بهره‌گیری از برندهای معتبر مانند *آلتون، پرنیان و البرز*، تلاش دارد نیازهای مشتریان در زمینه تجهیزات آشپزخانه، شیرآلات و هود را به بهترین شکل ممکن تأمین کند.\n"
            "ما همواره به کیفیت، مشتری‌مداری و خدمات پس از فروش متعهد هستیم.",
            parse_mode='Markdown'
        )

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "شماره‌های تماس شرکت:\n"
            "☎ 037-37352955\n"
            "☎ 037-37352956\n"
            "☎ 037-37352957\n"
            "📲 09912629410\n"
            "📲 09912629411\n"
            "📲 09912629412"
        )

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌های منو را انتخاب کنید.")

# تابع ارسال PDF
async def send_pdf(update: Update, file_path: str, caption: str):
    try:
        with open(file_path, 'rb') as f:
            await update.message.reply_document(document=f, caption=caption)
    except FileNotFoundError:
        await update.message.reply_text("❗ فایل مربوط به این برند یافت نشد.")

# اجرای ربات
if name == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("🤖 ربات در حال اجراست...")
    app.run_polling()Image Writer for Microsoft Windows
Release 1.0.0 - The "Holy cow, we made a 1.0 Release" release.
======
About:
======
This utility is used to read and write raw image files to SD and USB memory devices.
Simply run the utility, point it at your raw image, and then select the
removable device to write to.

This utility can not write CD-ROMs.  USB Floppy is NOT supported at this time.

Future releases and source code are available on our Sourceforge project:
http://sourceforge.net/projects/win32diskimager/

This program is Beta, and has no warranty. It may eat your files,
call you names, or explode in a massive shower of code. The authors take
no responsibility for these possible events.

===================
Build Instructions:
===================
Requirements:
1. Now using QT 5.7/MinGW 5.3.  

Short Version:
1. Install the Qt Full SDK and use QT Creator to build.  
   See DEVEL.txt for details

=============
New Features:
=============
Verify Image - Now you can verify an image file with a device.  This compares
the image file to the device, not the device to the image file (i.e. if you
write a 2G image file to an 8G device, it will only read 2G of the device for
comparison).
Additional checksums - Added SHA1 and SHA256 checksums.
Read Only Allocated Partitions - Option to read only to the end of the defined partition(s).  Ex:  Write a 2G image to a 32G device, reading it to a new file will only read to the end of
the defined partition (2G).
Save last opened folder - The program will now store the last used folder in
the Windows registry and default to it on next execution.
Additional language translations (thanks to devoted users for contributing).

=============
Bugs Fixed
=============
https://bugs.launchpad.net/win32-image-writer
LP: 1285238 - Need to check filename text box for valid filename (not just a directory).
LP: 1323876 - Installer doesn't create the correct permissions on install
LP: 1330125 - Multi-partition SD card only partly copied
https://sourceforge.net/p/win32diskimager/tickets/
SF:  7 - Windows 8 x64 USB floppy access denied. Possibly imaging C drive
SF:  8 - Browse Dialog doesnt open then crashes application
SF:  9 - Cannot Read SD Card
SF: 13 - 0.9.5 version refuses to open read-only image
SF: 15 - Open a image for write, bring window in the background
SF: 27 - Error1: Incorrect function
SF: 35 - Mismatch between allocating and deleting memory buffer
SF: 39 - Miswrote to SSD
SF: 40 - Disk Imager scans whole %USERPROFILE% on start
SF: 45 - Translation files adustment



=============
Known Issues:
=============
*  Lack of reformat capabilities.
*  Lack of file compression support

These are being looked into for future releases.

======
Legal:
======
Image Writer for Windows is licensed under the General Public
License v2. The full text of this license is available in 
GPL-2.

This project uses and includes binaries of the MinGW runtime library,
which is available at http://www.mingw.org

This project uses and includes binaries of the Qt library, licensed under the 
"Library General Public License" and is available at 
http://www.qt-project.org/.

The license text is available in LGPL-2.1

Original version developed by Justin Davis <tuxdavis@gmail.com>
Maintained by the ImageWriter developers (http://sourceforge.net/projects/win32diskimager).

