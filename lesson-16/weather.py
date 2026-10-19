from functions import (
  get_temperature, 
  is_hot
)

temperature = get_temperature()
hot = is_hot(temperature)

print(f"The temp is {temperature}, is it hot? {hot}")