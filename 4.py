
import re

a = "ГЩОавдылоа Овадлтлащ ОыфдльафзыаЗ За ыЗЗОЩОТШО."

p = re.compile(r'[А-Я][а-я]+')
m = p.findall(a)

print(m)




