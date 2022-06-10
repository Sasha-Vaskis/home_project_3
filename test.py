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
        if tab:
            sklad = tab.pop()
            print('Возьмите вот вам', sklad)
        else:
            print('Зайдите позже')









            #sklad = tab.pop()
           # print('Возьмите вот вам',sklad,tab)
           # break
       # else:
            #print('всего хорошего',tab)



