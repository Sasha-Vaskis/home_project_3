price = 0
gazon = input('есть ли у вас газон?').strip().lower().replace('yes', 'да')
if gazon == "да":
    s_gazon = int(input('какая площадь газона ?'))
    price += 10 + (s_gazon * 2)

wood = input('Есть ли у вас Лиственные деревья?').strip().lower().replace('yes', 'да')
if wood == "да":
    num = int(input('Сколько?'))
    price += num * 20

wood_hvoy = input('Есть ли у вас хвойные деревья?').strip().lower().replace('yes', 'да')
if wood_hvoy == "да":
    num = int(input('Сколько?'))
    price += num * 8

woter = input('Есть ли водоем?').strip().lower().replace('yes', 'да')

if woter == "да":
   v_woter = int(input('Каков его объем (Кубометры)?'))
   if v_woter < 20:
    price += 60 + (6*v_woter)
   else:
    price += 60 + (4 * v_woter)
print('Наши услуги будут стоить:', price)