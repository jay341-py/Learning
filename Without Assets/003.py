#Write a Python function that calculates simple interest given principal, rate, and time.


def interest(principal, rate, time_ye):
    ae = rate/100
    aa = ae * time_ye
    ab = 1 + aa
    ac = principal * ab
    ad = ac - principal
    print(f"Your principal is {principal} at a rate of {rate}% for {time_ye} years.\nWith this info your total interest is {ad} and total payable amount is {ac}")


interest(10000, 10, 6)
