# TODO Напишите функцию для поиска индекса товара
def poisk (x, y):
    n=0
    for i in range (0, len(x)):
        if (x[i]==y):
            n=i
            break
        else:
            n='None'
    return n
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list,find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
