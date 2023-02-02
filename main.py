def main():
    ##################################################
    # Comlete your code here
    reg_hours = int(40)
    reg_rate = float(18.25)
    o_rate = float(27.78)
    workhours = int(input("How many hours did you work this week?: "))
    reg_charge = reg_hours * reg_rate
    o_charge = (workhours - reg_hours) * o_rate
    total_wage = reg_charge + o_charge
    print(reg_charge)
    print(o_charge)
    print(total_wage)
    ##################################################
    pass


if __name__ == '__main__':
    main()
