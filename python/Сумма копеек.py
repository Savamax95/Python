def addUpChange(kop50, kop10, kop5, kop1):
    total = 0.50 * kop50 + 0.10 * kop10 + 0.05 * kop5 + 0.01 * kop1
    return total
kop50 = int(input("монет по 50 копеек: "))
kop10 = int(input("монет по 10 копеек: "))
kop5 = int(input("монет по 5 копеек: "))
kop1 = int(input("монет по 1 копейке: "))
total = addUpChange(kop50, kop10, kop5, kop1)
print ("Всего у нас: ", total, " рублей")

