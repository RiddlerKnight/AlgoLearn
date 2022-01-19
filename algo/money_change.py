
def call_me():
    print("ok")

def us_change_cal(m):
    # Quarter = 25 pen
    # Dime = 10 pen
    # nickel = 5 pen
    # penny = 1 pen
    quarter = 0; dime = 0; nickel = 0; pennies = 0
    call_me()
    while m > 0:
        if int(m / 25) > 0:
            quarter = int(m / 25)
            m -= quarter * 25
            continue
        if int(m / 10) > 0:
            dime = int(m / 10)
            m -= dime * 10
            continue
        if int(m / 5) > 0:
            nickel = int(m / 5)
            m -= nickel * 5
            continue
        pennies = m
        m = 0
    
    return [quarter, dime, nickel, pennies]


print(us_change_cal(73))

