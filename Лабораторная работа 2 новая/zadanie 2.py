money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
i=0
while(money_capital>=0):
    i += 1
    if(i>1):
        spend=spend+spend*increase
        money_capital=money_capital-spend+salary
    else:
        money_capital=money_capital-spend+salary

print("Количество месяцев, которое можно протянуть без долгов:", i-1)
