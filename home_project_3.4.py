tab = []
while True:
    data = input("что у вас ?")
    print('Спасибо')
    if data == 'exit':
        break
    if data:
        tab.insert(0, data)
        print(tab)
        continue
    else:
        if tab:
            print('Возьмите вот вам',tab.pop(0))
        else:
            print('Зайдите позже')
