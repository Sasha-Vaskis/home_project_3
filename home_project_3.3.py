tab = []
while True:
    data = input("что у вас ?")
    print('Спасибо')
    if data == 'exit':
        break
    if data:
        tab.append(data)
        print(tab)
        continue
    else:
        if tab:
            sklad = tab.pop()
            print('Возьмите вот вам', sklad)
        else:
            print('Зайдите позже')

