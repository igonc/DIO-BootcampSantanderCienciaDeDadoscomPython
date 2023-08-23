salary = 2000

def salarybonus(bonus):
    global salary
    salary += bonus
    return salary

print('The salary with bonus is: ', salarybonus(500))