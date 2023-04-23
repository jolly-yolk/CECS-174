customer_code = input("Input Customer Code (R, C, I): ")

if (customer_code == 'R' or customer_code == 'C' or customer_code == 'I'):
    start_reading = int(input("Input Start Reading: "))
    end_reading = int(input("Input End Reading: "))
    if (0 <= start_reading <= 999999999 and 0 <= end_reading <= 999999999):
        if (end_reading <= start_reading):
            print("Customer code:", customer_code)
            print(f'Beginning reading value in gallons and tenths of gallon {start_reading *.1}')
            print(f'Ending reading value in gallons and tenths of gallon {end_reading *.1}')
            used_gallons = 1000000000 - start_reading
            used_gallons *= .1
            end_reading *= .1
            used_gallons = end_reading + used_gallons
            print(f'Gallons of water used: {used_gallons:.1f}')
        else:
            start_reading *= .1
            end_reading *= .1
            print("Customer code:", customer_code)
            print(f'Beginning reading value in gallons and tenths of gallon {start_reading:.1f}')
            print(f'Ending reading value in gallons and tenths of gallon {end_reading:.1f}')
            used_gallons = end_reading - start_reading
            print(f'Gallons of water used: {used_gallons:.1f}')

        if (customer_code == 'R'):
            to_bill = (used_gallons * .0005) + 5
            print(f'Amount billed: ${to_bill:.2f}')

        if (customer_code == 'C'):
            if (used_gallons > 4000000):
                used_gallons -= 4000000
                to_bill = (used_gallons * .00025) + 1000
                used_gallons += 4000000
                print(f'Amount billed: ${to_bill:.2f}')
            else:
                to_bill = 1000.00
                print(f'Amount billed: ${to_bill:.2f}')

        if (customer_code == 'I'):
            if (used_gallons <= 4000000):
              to_bill = 1000.0
              print(f'Amount Billed$: ${to_bill:.2f}')
            elif (4000000 < used_gallons <= 10000000):
              to_bill = 2000.0
              print(f'Amount billed: ${to_bill:.2f}')
            else:
                used_gallons -= 10000000
                to_bill = (used_gallons * .00025) + 2000
                used_gallons += 10000000
                print(f'Amount billed: {to_bill:.2f}')
    else:
        print('Invalid input (beginning or ending reading value is out of the range)')
        
else:
    print('Invalid input (customer code)')