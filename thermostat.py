from terrarium import Terrarium

while True:
  humidity = Terrarium.get_humidity()

  if humidity < 30:
    Terrarium.mist(6)