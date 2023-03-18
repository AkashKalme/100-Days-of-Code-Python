name = "Akash"
country = "India"
letter = "Hey, my name is {0} and I am from {1}."
print(letter.format(name, country))
letter2 = f"Hey, my name is {name} and I am from {country}."
print(letter2)
letter3 = f"Hey, my name is {{name}} and I am from {{country}}."
print(letter3)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
price = 49.2812
txt2 = f"For only {price:.2f} dollars!"
print(txt2)

print(f"{2*45}")
print(type(f"{2*45}"))