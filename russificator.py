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
        print(n)
    def ошибка():
        exc_type, exc_value, exc_traceback = sys.exc_info()
        try:
            tb = traceback.extract_tb(exc_traceback)[0]
        except:
            tb = traceback.extract_tb(exc_traceback)[1]
        print(f'''Ошибка {tb.filename}:
    Строка {tb.lineno},
        {exc_value}
        {tb.line}''')
    def ифравно(i1, i2, i3):
        try:
            if i1 == i2:
                exec(str(i3).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def ифравноиначе(i1, i2, i3, i4):
        try:
            if i1 == i2:
                exec(str(i3).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
            else:
                exec(str(i4).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def иф(i1, i2):
        try:
            if f"{i1}":
                exec(str(i2).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
        except Exception:
            ошибка()
    def добавить(i1, i2):
        i1.append(i2)
    def кол(i1):
        return(len(i1))
    def форрейндж(i1, i2, i3):
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
    def форин(i1, i2):
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
        return(max(i1))
    def мин(i1):
        return(min(i1))
    def стоп():
        exit()
    def запуск(i1):
        exec(str(i1).replace(" и ", " and ").replace(" или ", " or ").replace(" не ", " not ").replace("если", " if "), globals())
    def ввод(i1):
        return(input(i1))
    def инт(i1):
        return(int(i1))
    def стр(i1):
        return(str(i1))
    def флоат(i1):
        return(float(i1))
    def бул(i1):
        return(bool(i1))
    def лист(i1):
        return(list(i1))
    def словарь(i1):
        return(dict(i1))
    def кортеж(i1):
        return(tuple(i1))
    def сет(i1):
        return(set(i1))
    def длина(i1):
        return(len(i1))
    def заменить(i1, i2, i3):
        return(i1.replace(i2, i3))
    def импорт(i1):
        exec(f"import {i1}", globals())
    def рандчисл(i1, i2):
        return(random.randint(i1, i2))
    def рандсписок(i1):
        return(random.choice(i1))
##################################################################
# ОНЛИ ИМПОРТЫ!(я не отвечаю за превод библиотек)
# (ОФИЦ ПОДДЕРЖКА ОНЛИ RANDOM)
##################################################################
    импорт("random")
##################################################################ы
    M = []
    ифравно(1, 1, '''
a = рандчисл(0, 5)
if a == 1 или a == 2:
    принт("1")''')
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
    print(f'''Ошибка {tb.filename}:
    Строка {tb.lineno},
        {exc_value}
        {tb.line}''')