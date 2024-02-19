def tax_calculator(get_salary):
    tax = 0
    salary = get_salary
    if salary <= 7010:
        tax = salary * 0.1
    else:
        tax = 7010 * 0.1
        salary -= 7010
        if salary <= 3050:
            tax += salary * 0.14
        else:
            tax += 3050 * 0.14
            salary -= 3050
            if salary <= 6090:
                tax += salary * 0.2
            else:
                tax += 6090 * 0.2
                salary -= 6090
                if salary <= 6290:
                    tax += salary * 0.31
                else:
                    tax += 6290 * 0.31
                    salary -= 6290
                    if salary <= 24250:
                        tax += salary * 0.35
                    else:
                        tax += 24250 * 0.35
                        salary -= 24250
                        if salary <= 13440:
                            tax += salary * 0.47
                        else:
                            tax += 13440 * 0.47
                            salary -= 13440
                            tax += salary * 0.5
    print(f"-----------------\n"
          f"Your salary amount is: {get_salary}\n"
          f"The amount of tax you must pay is: {tax:.2f}\n"
          f"Your net amount is: {get_salary - tax:.2f}")

get_salary = float(input("Enter your salary: "))
tax_calculator(get_salary)