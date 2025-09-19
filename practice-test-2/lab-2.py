# 16 ounces in a pound
# 2000 pounds in a ton
# 3200 ounces in a ton

# solution accepts an integer value representing any number of ounces
# solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())

#convert ounces to pounds and tons 
tons = ounces // 32000  # 1 ton
remaining_after_tons = ounces % 32000

pounds = remaining_after_tons // 16
remaining_ounces = ounces % 16

#output number of tons, remaining pounds, and remaining ounces
print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {remaining_ounces}')
