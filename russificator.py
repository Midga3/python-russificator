##################################################################
# MADE BY MIDGA3
# Tutorial can be found on py.midga3.ru
# Type from line 121
##################################################################
# Туториал на сайте py.midga3.ru
# Писать с 121 строки
# 
##################################################################
import sys
import traceback

try:
    def принт(n):
        try:
            print(n)
        except Exception:
            ошибка()
    def ошибка():
        exc_type, exc_value, exc_traceback = sys.exc_info()
        try:
            tb = traceback.extract_tb(exc_traceback)[0]
        except:
            tb = traceback.extract_tb(exc_traceback)[1]
        print(f'''{лицо()} Ошибка {tb.filename}:
    Строка {tb.lineno},
        {exc_value}
        {tb.line}''')
    def еслиравно(i1, i2, i3):
        try:
            if i1 == i2:
                exec(str(i3).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def еслиравноиначе(i1, i2, i3, i4):
        try:
            if i1 == i2:
                exec(str(i3).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
            else:
                exec(str(i4).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def если(i1, i2):
        try:
            if f"{i1}":
                exec(str(i2).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def добавить(i1, i2):
        try:
            i1.append(i2)
        except Exception:
            ошибка()
    def кол(i1):
        try:
            return(len(i1))
        except Exception:
            ошибка()
    def впорядке(i1, i2, i3):
        try:
            for i in range(i1, i2):
                exec(
                    str(i3)
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
    def взначениях(i1, i2):
        try:
            for i in i1:
                exec(
                    str(i2)
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
    def покаравно(i1, i2, i3):
        try:
            while i1 == i2:
                exec(str(i3).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def макс(i1):
        try:
            return(max(i1))
        except Exception:
            ошибка()
    def мин(i1):
        try:
            return(min(i1))
        except Exception:
            ошибка()
    def стоп():
        try:
            exit()
        except Exception:
            ошибка()
    def запуск(i1):
        try:
            exec(str(i1).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def ввод(i1):
        try:
            return(input(i1))
        except Exception:
            ошибка()
    def инт(i1):
        try:
            return(int(i1))
        except Exception:
            ошибка()
    def стр(i1):
        try:
            return(str(i1))
        except Exception:
            ошибка()
    def флоат(i1):
        try:
            return(float(i1))
        except Exception:
            ошибка()
    def бул(i1):
        try:
            return(bool(i1))
        except Exception:
            ошибка()
    def лист(i1):
        try:
            return(list(i1))
        except Exception:
            ошибка()
    def словарь(i1):
        try:
            return(dict(i1))
        except Exception:
            ошибка()
    def кортеж(i1):
        try:
            return(tuple(i1))
        except Exception:
            ошибка()
    def сет(i1):
        try:
            return(set(i1))
        except Exception:
            ошибка()
    def длина(i1):
        try:
            return(len(i1))
        except Exception:
            ошибка()
    def заменить(i1, i2, i3):
        try:
            return(i1.replace(i2, i3))
        except Exception:
            ошибка()
    def импорт(i1):
        try:
            exec(f"import {i1}", globals())
        except Exception:
            ошибка()
    def рандчисл(i1, i2):
        try:
            return(random.randint(i1, i2))
        except Exception:
            ошибка()
    def рандсписок(i1):
        try:
            return(random.choice(i1))
        except Exception:
            ошибка()
    def лицо() -> str:
        try:
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
##################################################################
# ОНЛИ ИМПОРТЫ!(я не отвечаю за превод библиотек)
# (ОФИЦ ПОДДЕРЖКА ОНЛИ RANDOM)
##################################################################
    импорт("random")
##################################################################ы
# END OF THE TUTORIAL
# КОНЕЦ ТУТОРИАЛА


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