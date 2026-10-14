def get_temperature():
    return int(input("Enter the temperature"))

def is_hot(temperature):
    return temperature >= 30

temperature = get_temperature()
hot = is_hot(temperature)

print(f"The temp is {temperature}, is it hot? {hot}")