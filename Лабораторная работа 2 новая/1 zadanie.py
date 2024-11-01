salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital=0
for i in range (1,11):
    if(i>1):
        spend=spend+increase*spend
        money_capital=money_capital+spend-salary
    else:
        money_capital=spend-salary
if (money_capital%1!=0):
    money_capital=(money_capital//1)+1 

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
