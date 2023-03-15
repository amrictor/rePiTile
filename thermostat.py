from terrarium import Terrarium

tank = Terrarium()

while True:
  humidity = tank.get_humidity()

  if humidity < 30:
    try:
      tank.mist(6)
    except:
      print("waiting to mist")