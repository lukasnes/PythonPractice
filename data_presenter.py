open_invoices = open('CupcakeInvoices.csv')
import math
for line in open_invoices:
    print(line)

open_invoices = open('CupcakeInvoices.csv')
for line in open_invoices:
    line = line.strip('\n').split(',')
    print(line)
    print(line[2])

open_invoices = open('CupcakeInvoices.csv')
for line in open_invoices:
    line = line.strip('\n').split(',')
    total = int(line[3]) * int(float(line[4]))
    print(math.floor(total))

open_invoices = open('CupcakeInvoices.csv')
grand_total = 0
for line in open_invoices:
    line = line.strip('\n').split(',')
    total = int(line[3]) * int(float(line[4]))
    grand_total += total
print(grand_total)

open_invoices.close()
    