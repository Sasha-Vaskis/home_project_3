tab = []
while True:
    data = input("что у вас ?")
    print('Спасибо')
    if data == 'exit':
        break
    if data:
        tab.append(data)
        continue
    else:
        sklad = tab.pop()
        print('Возьмите вот вам',sklad)
        print('всего хорошего')

