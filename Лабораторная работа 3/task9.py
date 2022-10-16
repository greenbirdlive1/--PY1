salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for x in range(months):
    money = spend * (1 + increase) ** x - salary
    need_money += money

print(round(need_money))
