# Update - часть информации полученной нами от Телеграмма.
import re
import FNS_el_dok
from telegram import Update

# ApplicationBuilder - способ создать приложение с указанием типа настройки, т.е.
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from pars_web import pars_web



#token - секретный ключ к боту (получить у @BotFather)
app = ApplicationBuilder().token("5817608503:AAFJiFwjKhYW7Q21_EKXmMHvks9Y2k8va7g").build()

# функция вызывается при получении сообщения
# upd - новая информация от Telegramm
# context - служебная информация от Telegramm
async def text_replay(upd: Update, _context):
    user_text = upd.message.text
    name = upd.message.from_user.full_name
    pattern = r'^\d{10}$'
    print(name)
    if user_text == '/about_us':
        await upd.message.reply_text("# -*- coding: utf8 -*-\n  Мы рады приветствовать Вас в поисковой системе Ак Барс Банка.\n\n   Для проверки контрагента отправте ИНН организации. Для получения ИНН фзического лица отправте его данные в формате:\n\nИванов Иван Иванович 19.10.1985 12 34 123456 09.12.2010\n\n   Где 19.10.1985 - дата рождения,12 34 123456 - серия и номер паспорта,09.12.2010 - дата выдачи документа. ВСЕ ДАННЫЕ ДОЛЖНЫ БЫТЬ НАПИСАННЫ В ОДНУ СТРОКУ.\n\n    В ответ бот осуществит поиск компании и вышлет Вам ответ на запрос.\n\n В случае если вы не получили ответа - отправте запрос повторно через 5 минут.")
    elif user_text =='/about_creator':
        await upd.message.reply_text('Иедя реализации парсера сайтов принадлежит руководителю направления по защите банковской тайны Зишаншину Сергею Рафаилевичу.\nРеализацией идеи занимался специалист ЕСЦ отдела андеррайтинга кредитных заявок физических лиц Черный Сергей Николаевич.\nТелефон для связи: 8(961)390-31-38')
    elif user_text =='/start':
        await upd.message.reply_text('Преветствуем Вас в поисковой сиситеме Ак Барс Банка.')
    elif re.match(pattern, user_text):
        print(f"> [USER: {name}]: {user_text}")
        replay = f'Уважаемый {name}, мы получили от Вас запрос по проверке организации: {user_text}.'
        print(replay)
        # Запустить парсер
        await upd.message.reply_text(replay)
        total_report = pars_web(user_text)
        await  upd.message.reply_text(total_report[1])
        await upd.message.reply_document(document=open(total_report[0], 'rb'))
    else:
        print(f"> [USER: {name}]: {user_text}")
        replay = f'Уважаемый {name}, мы получили от Вас запрос по получению ИНН физического лица:\n\n {user_text}'
        await upd.message.reply_text(replay)
        list_inn = user_text.split(' ')
        print(list_inn)
        total_report_inn = FNS_el_dok.fns_rossii_inn(list_inn[0], list_inn[1], list_inn[2], list_inn[3], str(list_inn[4])+' '+str(list_inn[5])+' '+str(list_inn[6]),list_inn[7])
        for x in total_report_inn:
            await  upd.message.reply_text(x)

# Handler - обработчик сообщения
handler = MessageHandler(filters.TEXT, text_replay)
# прикрепляем обработчик к приложению
app.add_handler(handler)

# запускаем приложение
app.run_polling()