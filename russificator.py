##################################################################
# MADE BY MIDGA3
# Type from line 121
##################################################################
# Писать с 121 строки
##################################################################
import sys
import traceback

try:
    def принт(значение):
        """
        Старый добрый принт
        """
        try:
            print(значение)
        except Exception:
            ошибка()
    def ошибка():
        """
        Обработчик ошибок(WIP?) 67
        """
        exc_type, exc_value, exc_traceback = sys.exc_info()
        try:
            tb = traceback.extract_tb(exc_traceback)[0]
        except:
            tb = traceback.extract_tb(exc_traceback)[1]
        print(f'''{лицо()} Ошибка {tb.filename}:
    Строка {tb.lineno},
        {exc_value}
        {tb.line}''')
    def еслиравно(значение1, значение2, код):
        """
        Если значение1 равно значению2 выполнит код
        """
        try:
            if значение1 == значение2:
                exec(str(код).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def еслиравноиначе(значение1, значение2, код1, код2):
        """
        Если значение1 равно значению2, выполнит код1, иначе выполнит код2
        """
        try:
            if значение1 == значение2:
                exec(str(код1).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
            else:
                exec(str(код2).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def если(значение, код):

        try:
            if значение:
                exec(str(код).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def добавить(список, значение):
        """
        Добавляет значение в список
        """
        try:
            список.append(значение)
        except Exception:
            ошибка()
    def впорядке(значение1, значение2, код):
        """
        for i in range(значение1, значение2): код
        """
        try:
            for i in range(значение1, значение2):
                exec(
                    str(код)
                    .replace(" и ", " and ")
                    .replace(" или ", " or ")
                    .replace(" не ", " not ")
                    .replace("если", " if ")
                    .lstrip(),
                    globals(),
                    locals(),
                )
        except Exception:
            ошибка()
    def взначениях(список, код):
        """
        for i in список
        """
        try:
            for i in список:
                exec(
                    str(код)
                    .replace(" и ", " and ")
                    .replace(" или ", " or ")
                    .replace(" не ", " not ")
                    .replace("если", " if ")
                    .lstrip(),
                    globals(),
                    locals(),
                )
        except Exception:
            ошибка()
    def покаравно(значение1, значение2, код):
        """
        while з1 == з2: код
        """
        try:
            while значение1 == значение2:
                exec(str(код).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def макс(список):
        """
        Выводит максимальное значение из списка
        """
        try:
            return(max(список))
        except Exception:
            ошибка()
    def мин(список):
        """
        Выводит минимальное значение из списка
        """
        try:
            return(min(список))
        except Exception:
            ошибка()
    def стоп():
        """
        Стоп программа.
        (СТОП МАШИНА!!!)
        """
        try:
            exit()
        except Exception:
            ошибка()
    def запуск(код):
        """
        exec
        """
        try:
            exec(str(код).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def ввод(текст = None):
        """
        Дает пользователю ввод с кастом текстом(необязательно)
        """
        try:
            return(input(текст))
        except Exception:
            ошибка()
    def инт(значение):
        """
        Превращает значение в int
        """
        try:
            return(int(значение))
        except Exception:
            ошибка()
    def стр(значение):
        """
        Превращает значение в список
        """
        try:
            return(str(значение))
        except Exception:
            ошибка()
    def флоат(значение):
        """
        Превращает значение в float
        """
        try:
            return(float(значение))
        except Exception:
            ошибка()
    def бул(значение):
        """"
        Стандартный Bool
        """
        try:
            return(bool(значение))
        except Exception:
            ошибка()
    def лист(значение = None):
        """
        Создает лист из значения/пустой
        """
        try:
            return(list(значение))
        except Exception:
            ошибка()
    def словарь(значение = None):
        """
        Создает словарь из значения/пустой
        """
        try:
            return(dict(значение))
        except Exception:
            ошибка()
    def кортеж(значение = None):
        """
        Создает кортеж из значение/пустой
        """
        try:
            return(tuple(значение))
        except Exception:
            ошибка()
    def сет(значение = None):
        """
        Превращает значение в сет/создает пустой сет
        """
        try:
            return(set(значение))
        except Exception:
            ошибка()
    def длина(значение):
        """
        Возвращает длину списка либо строки, которую вы вставите.
        """
        try:
            return(len(значение))
        except Exception:
            ошибка()
    def заменить(список, значение1, значение2):
        try:
            return(список.replace(значение1, значение2))
        except Exception:
            ошибка()
    def импорт(библиотека):
        """
        Наш старый любимый импорт библиотек. Официальная поддержка "random"
        """
        try:
            exec(f"import {библиотека}", globals())
        except Exception:
            ошибка()
    def рандчисл(число1, число2):
        """
        Возвращает рандомное число из ограниений.
        """
        try:
            return(random.randint(число1, число2))
        except Exception:
            ошибка()
    def рандсписок(список):
        """
        Выбирает случайное значение из списка
        """
        try:
            return(random.choice(список))
        except Exception:
            ошибка()
    def лицо() -> str:
        """
        Возвращает краивое лицо с помощью ASCII арта
        """
        try:
            импорт("random")
            return(
            random.choice(
            [
                "ヽ(๑◠ܫ◠๑)ﾉ",
                "(◕ᴥ◕ʋ)",
                "ᕙ(`▽´)ᕗ",
                "(✿◠‿◠)",
                "(▰˘◡˘▰)",
                "(˵ ͡° ͜ʖ ͡°˵)",
                "ʕっ•ᴥ•ʔっ",
                "( ͡° ᴥ ͡°)",
                "(๑•́ ヮ •̀๑)",
                "٩(^‿^)۶",
                "(っˆڡˆς)",
                "ψ(｀∇´)ψ",
                "⊙ω⊙",
                "٩(^ᴗ^)۶",
                "(´・ω・)っ由",
                "( ͡~ ͜ʖ ͡°)",
                "✧♡(◕‿◕✿)",
                "โ๏௰๏ใ ื",
                "∩｡• ᵕ •｡∩ ♡",
                "(♡´౪`♡)",
                "(◍＞◡＜◍)⋈。✧♡",
                "╰(✿´⌣`✿)╯♡",
                "ʕ•ᴥ•ʔ",
                "ᶘ ◕ᴥ◕ᶅ",
                "▼・ᴥ・▼",
                "ฅ^•ﻌ•^ฅ",
                "(΄◞ิ౪◟ิ‵)",
                "٩(^ᴗ^)۶",
                "ᕴｰᴥｰᕵ",
                "ʕ￫ᴥ￩ʔ",
                "ʕᵕᴥᵕʔ",
                "ʕᵒᴥᵒʔ",
                "ᵔᴥᵔ",
                "(✿╹◡╹)",
                "(๑￫ܫ￩)",
                "ʕ·ᴥ·　ʔ",
                "(ﾉ≧ڡ≦)",
                "(≖ᴗ≖✿)",
                "（〜^∇^ )〜",
                "( ﾉ･ｪ･ )ﾉ",
                "~( ˘▾˘~)",
                "(〜^∇^)〜",
                "ヽ(^ᴗ^ヽ)",
                "(´･ω･`)",
                "₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡",
                "(。・・)_且",
                "(=｀ω´=)",
                "(*•‿•*)",
                "(*ﾟ∀ﾟ*)",
                "(☉⋆‿⋆☉)",
                "ɷ◡ɷ",
                "ʘ‿ʘ",
                "(。-ω-)ﾉ",
                "( ･ω･)ﾉ",
                "(=ﾟωﾟ)ﾉ",
                "(・ε・`*) …",
                "ʕっ•ᴥ•ʔっ",
                "(*˘︶˘*)",
                "ಥ_ಥ",
                "･ﾟ･(｡>д<｡)･ﾟ･",
                "(┬┬＿┬┬)",
                "(◞‸◟ㆀ)",
                " ˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚",
            ]
        )
            )
        except Exception:
            ошибка()
    def вар(функция):
        """
        Возвращает все возможные варианты класса/фунцкии
        """
        try:
            return dir(функция)
        except Exception:
            ошибка()
    def сум(список):
        """
        Возвращает сумму чисел из списка Python
        """
        try:
            return sum(список)
        except Exception:
            ошибка()
    def срзнач(список):
        """
        Возвращает среднее арифмитическое из списка
        """
        try:
            return sum(список)/len(список)
        except Exception:
            ошибка()
    def двоич(число):
        """
        Возвращает число в десятичной системе
        """
        try:
            return int(bin(число).split("b")[1])
        except Exception:
            ошибка()
    def восмирич(число):
        """
        Возращает число в восьмеричной системе
        """
        try:
            return int(oct(число).split("o")[1])
        except Exception:
            ошибка()
    def шестнадцатирич(число):
        """
        Возвращает число в шестнадцатиричной системе
        """
        try:
            return int(hex(число).split("x")[1])
        except Exception:
            ошибка()
    def десятич(число, система):
        """
        Возвращает число в десятичной системе из другой системы счисления
        """
        try:
            return int(str(число), система)
        except Exception:
            ошибка()
##################################################################
# ОНЛИ ИМПОРТЫ!(я не отвечаю за превод библиотек)
# (ОФИЦ ПОДДЕРЖКА ОНЛИ RANDOM)
    импорт("random")
##################################################################
#################################################################ы
# END OF THE TUTORIAL
# КОНЕЦ ТУТОРИАЛА

# TYPE CODE FROM HERE
# ПИСАТЬ КОД ОТСЮДА

    
##################################################################
# DO NOT TOUCH THIS
##################################################################
# НЕ ТРОГАТЬ!
##################################################################
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    try:
        tb = traceback.extract_tb(exc_traceback)[-2]
    except:
        tb = traceback.extract_tb(exc_traceback)[-1]
    print(f'''{лицо()} Ошибка {tb.filename}:
    Строка {tb.lineno},
        {exc_value}
        {tb.line}''')
