STRATEGY_FIFO = 'fifo'
STRATEGY_LIFO = 'lifo'
strategy = input('какая у вас стратегия ?')
tab = []
while True:
    data = input("что у вас ?")
    print('Спасибо')
    if data == 'exit':
        break
    if data:
        if strategy == STRATEGY_FIFO:
            tab.append(data)
        elif strategy == STRATEGY_LIFO:
            tab.insert(0, data)
        print(tab)
        continue
    else:
        if tab:
            print('Возьмите вот вам', tab.pop(0))
        else:
            print('Зайдите позже')