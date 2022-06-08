import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *

token = '5559863217:AAElJaj88HIRDibdLbWoa_PvACIkPz74f1w'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Assalomu aleykum botga xush kelibsiz!", reply_markup=one_open)


@dp.message_handler()
async def send_video(message: types.Message):
    if message.text == 'Dasturlash Kurslari 💻':
        await message.reply(
            "Dasturlash Kurslari Ruyhati 📃", reply_markup=two_open)

    elif message.text == 'Grafik Dizayn Kurslari 🎨':
        await message.reply(
            "Grafik Dizayn Kurslari Ruyhati 🎨 ", reply_markup=grafik_dizan_list_button)

    elif message.text == 'Bosh Menu 🏚':
        await message.answer(
            "Bosh Menu 🏚", reply_markup=one_open)

    elif message.text == 'Offise Dasturlari Kurslari 🏛':
        await message.reply(
            "Offise Dasturlari Kurslari 🏛 ", reply_markup=ofis_dasturlar_list_button)


    elif message.text == 'SMM Kurslari 👨‍🎓':
        await message.reply(
            "SMM Kurslar Ruyhati 👨‍🎓 ", reply_markup=smm_kurslar_list_button)

        # **********************************************************************************************

    # grafik dizayn kurslari

    elif message.text == 'AutoCad':
        await message.answer("https://youtu.be/BdyGnAfZHDE\n")
        await message.answer("https://youtu.be/qLDvBJE8FZ8\n")
        await message.answer("https://youtu.be/Cd0Jk1PQMAY\n")
        await message.answer("https://youtu.be/TLDGAnCD65k\n", reply_markup=grafik_dizan_list_button)

        # **********************************************************************************************

    elif message.text == '3D Max':
        await message.answer("https://youtu.be/p4QHHh347eA\n")
        await message.answer("https://youtu.be/KtVs9zt6--8\n")
        await message.answer("https://youtu.be/l4hlMPDk0uQ\n")
        await message.answer("https://youtu.be/aePz9TmmV7U\n")
        await message.answer("https://youtu.be/Y9wpUEjbGQY\n")
        await message.answer("https://youtu.be/pfUZ1HcRNHA\n")
        await message.answer("https://youtu.be/yRWKKTI0rjM\n")
        await message.answer("https://youtu.be/apbzpfyk7SE\n", reply_markup=grafik_dizan_list_button)

        # **********************************************************************************************

    elif message.text == 'Blender':
        await message.answer("https://youtu.be/DncqDaR71ZA\n")
        await message.answer("https://youtu.be/6V1Igv68o5I\n")
        await message.answer("https://youtu.be/446u64KAg3M\n")
        await message.answer("https://youtu.be/hZT3EmFhklg\n")
        await message.answer("https://youtu.be/tMISorvpJQE\n")
        await message.answer("https://youtu.be/VWPsX-DIKA8\n")
        await message.answer("https://youtu.be/DCSiQxLAJSA\n")
        await message.answer("https://youtu.be/iXVU8c5XyIQ\n")
        await message.answer("https://youtu.be/1UXxt9vpd0s\n")
        await message.answer("https://youtu.be/W6jCPNKEBkQ\n")
        await message.answer("https://youtu.be/0f07uGS5ZJM\n")
        await message.answer("https://youtu.be/mM2gp1YsqhQ\n", reply_markup=grafik_dizan_list_button)

        # **********************************************************************************************

    elif message.text == 'Photoshop':
        await message.answer("https://youtu.be/QkFbCLRitf0\n")
        await message.answer("https://youtu.be/ygTjexBbruo\n")
        await message.answer("https://youtu.be/XiI4HWL5nRs\n")
        await message.answer("https://youtu.be/eIUIqZ1Xm3U\n")
        await message.answer("https://youtu.be/MJm5jLJBjAo\n")
        await message.answer("https://youtu.be/Xhfx_vvKxfw\n")
        await message.answer("https://youtu.be/AI_aA4JUWI0\n")
        await message.answer("https://youtu.be/XNz19VaNL7U\n", reply_markup=grafik_dizan_list_button)

        # **********************************************************************************************

    elif message.text == 'Ilustratsa':
        await message.answer("https://youtu.be/PAFREtwTVBo\n")
        await message.answer("https://youtu.be/Vu5IOGSR9sg\n")
        await message.answer("https://youtu.be/tReOSQkL018\n")
        await message.answer("https://youtu.be/dNkRmht6e34\n")
        await message.answer("https://youtu.be/pZslTzIXR0g\n")
        await message.answer("https://youtu.be/S9LwD71AcNk\n")
        await message.answer("https://youtu.be/5HKT23YuHK0\n")
        await message.answer("https://youtu.be/wHAx9z7OIAM\n")
        await message.answer("https://youtu.be/b4F36iVecN8\n")
        await message.answer("https://youtu.be/AYKc3G3arT8\n")
        await message.answer("https://youtu.be/s2imF1dA_JQ\n")
        await message.answer("https://youtu.be/RejKxhLJPWI\n")
        await message.answer("https://youtu.be/JZKOv5m5-iY\n")
        await message.answer("https://youtu.be/JZKOv5m5-iY\n")
        await message.answer("https://youtu.be/GRRVmG-S2QQ\n")
        await message.answer("https://youtu.be/hro3Jnevd4U\n")
        await message.answer("https://youtu.be/hro3Jnevd4U\n")
        await message.answer("https://youtu.be/uToOI1OjoS4\n")
        await message.answer("https://youtu.be/UbdqNsXUGNc\n")
        await message.answer("https://youtu.be/3ZoWh4O-ucw\n")
        await message.answer("https://youtu.be/YUaP3tlyY_w\n")
        await message.answer("https://youtu.be/wFqQDbcsNIc\n")
        await message.answer("https://youtu.be/Yuz7O1I70mM\n")
        await message.answer("https://youtu.be/3mfx4_d9108\n")
        await message.answer("https://youtu.be/I904aFyiyEg\n")
        await message.answer("https://youtu.be/ZsM_7UbYnrQ\n", reply_markup=grafik_dizan_list_button)


        # **********************************************************************************************

    # office dasturlari kurslari

    elif message.text == 'WinWord 2016':
        await message.answer("https://youtu.be/DcE1bRTIvog\n")
        await message.answer("https://youtu.be/anyrypp_YOI\n")
        await message.answer("https://youtu.be/oTBDUM_5hXQ\n")
        await message.answer("https://youtu.be/oTBDUM_5hXQ\n")
        await message.answer("https://youtu.be/RgWIkFuusSk\n")
        await message.answer("https://youtu.be/HLZFrQhA3LY\n")
        await message.answer("https://youtu.be/nBBZqm6BaUo\n")
        await message.answer("https://youtu.be/2ZZBjJrlB_c\n")
        await message.answer("https://youtu.be/tM7oKj0k1Cw\n")
        await message.answer("https://youtu.be/tM7oKj0k1Cw\n", reply_markup=ofis_dasturlar_list_button)

        # **********************************************************************************************

    elif message.text == 'Excel 2016':
        await message.answer("https://youtu.be/0KIw98oFwVs\n")
        await message.answer("https://youtu.be/Av0aumrOTmc\n")
        await message.answer("https://youtu.be/i6EM91VkjBk\n")
        await message.answer("https://youtu.be/sVPP_PcAC1E\n")
        await message.answer("https://youtu.be/Qn2zOetITng\n")
        await message.answer("https://youtu.be/-qdNg9Zth1o\n")
        await message.answer("https://youtu.be/-qdNg9Zth1o\n")
        await message.answer("https://youtu.be/dz8EOmRP3G4\n", reply_markup=ofis_dasturlar_list_button)

        # **********************************************************************************************

    elif message.text == 'PowerPoint':
        await message.answer("https://youtu.be/pywHGA2g-0w\n")
        await message.answer("https://youtu.be/nR0tcZVazoM\n")
        await message.answer("https://youtu.be/iUQGxGOKEs0\n")
        await message.answer("https://youtu.be/BGOBkCcUcww\n")
        await message.answer("https://youtu.be/wVX43LPDotQ\n")
        await message.answer("https://youtu.be/fo2vL_RoqT8\n")
        await message.answer("https://youtu.be/95kF7Yz95Lk\n")
        await message.answer("https://youtu.be/MwETtKvm-f0\n", reply_markup=ofis_dasturlar_list_button)

        # **********************************************************************************************

    # SMM Kurslari

    elif message.text == 'SMM chilar Kurishi Kerak\nBulgan Videolar':
        await message.answer("https://youtu.be/-CVv3gpDBrA\n")
        await message.answer("https://youtu.be/ObhUhFUgBRs\n")
        await message.answer("https://youtu.be/H4FWXkhsTms\n")
        await message.answer("https://youtu.be/Gz6J3nBDxFU\n")
        await message.answer("https://youtu.be/9nPpkg2vSOE\n")
        await message.answer("https://youtu.be/nUn9bS_nmO4\n", reply_markup=smm_kurslar_list_button)

        # **********************************************************************************************

    elif message.text == 'SMM Kurslar':
        await message.answer("https://youtu.be/nUn9bS_nmO4\n")
        await message.answer("https://youtu.be/nUn9bS_nmO4\n")
        await message.answer("https://youtu.be/bN7WAkffoM4\n")
        await message.answer("https://youtu.be/ZJ-edYEgey0\n")
        await message.answer("https://youtu.be/BBddYvehWxQ\n")
        await message.answer("https://youtu.be/dC2k4Y2c3U8\n")
        await message.answer("https://youtu.be/dC2k4Y2c3U8\n")
        await message.answer("https://youtu.be/6448sa5_iKE\n")
        await message.answer("https://youtu.be/PT3isVB0I2k\n")
        await message.answer("https://youtu.be/xgZyBIWgr9Q\n")
        await message.answer("https://youtu.be/FKGb2_mYZN0\n", reply_markup=smm_kurslar_list_button)

        # **********************************************************************************************

    # python kurslari

    elif message.text == 'Python Kurslari':

        await message.answer("https://youtu.be/_f8cpjAz0sw\n")
        await message.answer("https://youtu.be/fj_GLU344bQ\n")
        await message.answer("https://youtu.be/Q3H1OUj_XU8\n")
        await message.answer("https://youtu.be/-haxzF1rzZ0\n")
        await message.answer("https://youtu.be/slMBSFsORow\n")
        await message.answer("https://youtu.be/o5XIOTLBPIU\n")
        await message.answer("https://youtu.be/ixc2mq0FKHA\n")
        await message.answer("https://youtu.be/RhgjRtIEFnI\n")
        await message.answer("https://youtu.be/DAQClN-s6y4\n")
        await message.answer("https://youtu.be/5ZAsEq94TA0\n")
        await message.answer("https://youtu.be/_cvnzZN5eic\n")
        await message.answer("https://youtu.be/S5zqzqZSJgk\n")
        await message.answer("https://youtu.be/tykfZMFi7Pk\n")
        await message.answer("https://youtu.be/MYQi17lZwwA\n")
        await message.answer("https://youtu.be/4odkjB1BEaY", reply_markup=two_open)


        # **********************************************************************************************

    # Java kurslari

    elif message.text == 'Java Kurslari':

        await message.answer("https://youtu.be/hhyFI9hTwrM\n")
        await message.answer("https://youtu.be/5N_73oUlnkY\n")
        await message.answer("https://youtu.be/7CmbXZOZzn0\n")
        await message.answer("https://youtu.be/II2R41e_ydY\n")
        await message.answer("https://youtu.be/II2R41e_ydY\n")
        await message.answer("https://youtu.be/Qqo77lZhzGY\n")
        await message.answer("https://youtu.be/Qqo77lZhzGY\n")
        await message.answer("https://youtu.be/V5SHKWgyIyg\n", reply_markup=two_open)


        # **********************************************************************************************

    # Flutter kurslari

    elif message.text == 'Flutter Kurslari':

        await message.answer("https://youtu.be/x2L3VkEMwB4\n")
        await message.answer("https://youtu.be/Mwtc8JIPBmw\n")
        await message.answer("https://youtu.be/lgXUrJmb3Go\n")
        await message.answer("https://youtu.be/Oveo6VFZRhU\n")
        await message.answer("https://youtu.be/Z49zqCSViIE\n")
        await message.answer("https://youtu.be/e0KN13wJtL0\n")
        await message.answer("https://youtu.be/cLMEH0RapZ4\n")
        await message.answer("https://youtu.be/0SIVi8CkOX4\n")
        await message.answer("https://youtu.be/QDahHuDGf_4\n", reply_markup=two_open)


        # **********************************************************************************************

    # Html/Css kurslari

    elif message.text == 'Html/Css Kurslari':

        await message.answer("https://youtu.be/xcGtfYUfDLo\n")
        await message.answer("https://youtu.be/uUULF8ikQoY\n")
        await message.answer("https://youtu.be/GVKi9E7DjAs\n")
        await message.answer("https://youtu.be/b8Fk2u_C7i8\n")
        await message.answer("https://youtu.be/GBvdEBdiWhQ\n")
        await message.answer("https://youtu.be/8SJc1OHQ01Q\n")
        await message.answer("https://youtu.be/ttbt7Y7vxQc\n")
        await message.answer("https://youtu.be/6kN2RxpVH18 ", reply_markup=two_open)

        # **********************************************************************************************


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
