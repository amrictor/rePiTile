from terrarium import Terrarium

tank = Terrarium()

while True:
  humidity = tank.get_humidity()

  if humidity < 40:
    try:
      tank.mist(6)
    except Exception as e:
      print(e)