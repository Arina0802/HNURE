print("у магазині продаються такі товари: яблуко, банан, апельсин")

apples = int(input("скільки яблук ви купите?"))
bananas = int(input("скільки бананів ви купите?"))
oranges = int(input("скільки апельсинів ви купите?"))

apple = 10
banana = 24
orange = 32

result1 = (apples * apple)
result2 = (bananas * banana)
result3 = (oranges * orange)

result = (apples * apple) + (bananas * banana) + (oranges * orange) 

print("ціна яблук", result1, "грн")
print("ціна бананів", result2, "грн")
print("ціна апельсинів", result3, "грн")

print("з вас:", result, "грн")