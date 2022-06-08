from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back = KeyboardButton('Bosh Menu 🏚')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(back)

button1 = KeyboardButton('Dasturlash Kurslari 💻')
button2 = KeyboardButton('Grafik Dizayn Kurslari 🎨')
button3 = KeyboardButton('Offise Dasturlari Kurslari 🏛')
button4 = KeyboardButton('SMM Kurslari 👨‍🎓')

one_open = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3, button4)

python = KeyboardButton('Python Kurslari')
java = KeyboardButton('Java Kurslari')
flutter = KeyboardButton('Flutter Kurslari')
html_css = KeyboardButton('Html/Css Kurslari')

two_open = ReplyKeyboardMarkup(resize_keyboard=True).add(python, java, flutter, html_css, back)

autocad = KeyboardButton('AutoCad')
uchdmax = KeyboardButton('3D Max')
blender = KeyboardButton('Blender')
photoshop = KeyboardButton('Photoshop')
ilustratsa = KeyboardButton('Ilustratsa')

grafik_dizan_list_button = ReplyKeyboardMarkup(resize_keyboard=True).add(autocad, uchdmax, blender, photoshop,
                                                                         ilustratsa,back)

winword = KeyboardButton('WinWord 2016')
excel = KeyboardButton('Excel 2016')
powerpoint = KeyboardButton('PowerPoint')

ofis_dasturlar_list_button = ReplyKeyboardMarkup(resize_keyboard=True).add(winword, excel, powerpoint,back)

instagram_smm = KeyboardButton('SMM Kurslar')
fasebok_smm = KeyboardButton('SMM chilar Kurishi Kerak\nBulgan Videolar')

smm_kurslar_list_button = ReplyKeyboardMarkup(resize_keyboard=True).add(instagram_smm,fasebok_smm,back)