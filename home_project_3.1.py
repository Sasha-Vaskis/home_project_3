price = 0
gazon = input('есть ли у вас газон?')
if gazon == "да":
    s_gazon = int(input('какая площадь газона ?'))
    price += 10 + (s_gazon * 2)

wood = input('Есть ли у вас Лиственные деревья?')
if wood == "да":
    num = int(input('Сколько?'))
    price += num * 20

wood_hvoy = input('Есть ли у вас хвойные деревья?')
if wood_hvoy == "да":
    num = int(input('Сколько?'))
    price += num * 8

woter = input('Есть ли водоем?')
if woter == "да":
    v_woter = int(input('Каков его объем (Кубометры)?'))
    price += 60+(4 if v_woter > 20 else 6)

print('Наши услуги будут стоить:', price)