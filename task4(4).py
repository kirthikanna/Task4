class tv:#PARENT CLASS OR BASE CLASS
    def __init__(TCL,price,inches,OnOffstatus,volume,channel,vol=50,chan=1):
        TCL.price=price
        TCL.inches=inches
        TCL.OnOffstatus=OnOffstatus
        TCL.volume=volume
        TCL.channel=channel
        TCL.v=vol
        TCL.c=chan

    def decreasevolume(TCL):  # THE METHOD TO DECREASE THE VOLUME OF TV
        if TCL.volume >= 100:
            TCL.volume = TCL.volume - 10
            print("decreased the tv volume")

    def increasevolume(TCL):  # THE METHOD TO INCREASE THE VOLUME OF THE TV
        if TCL.volume >= 0 & TCL.volume <= 100:
            TCL.volume = TCL.volume + 10
            print("increased the tv volume to", TCL.volume)

    def chan(TCL):  # TO DISPLAY THE CHANNEL NUMBER OF THE TV
        if TCL.channel <= 50:
            print("channel number is", TCL.channel)
        else:
            print("you have entered the invalid channel number")
    def resetTv(TCL):  # METHOD TO RESET THE TV
                print("tv reset to default volume and channel")
                print("the default volume of tv is", TCL.volume)
                print("the default channel of tv is", TCL.chan)

    def status(TCL):  # METHOD TO DISPLAY THE STATUS OF THE TV
                print("the TCL tv is at channel number", TCL.channel, "and volume of tv is", TCL.volume)
class Led(tv):  # SUBCLASS AND WE USED THE CONCEPT OF INHERITANCE
     def __init__(TCL, price, inches, ONOffstatus, volume, channel, screenthickness, energyusage, lifespan,
                         refreshrate, viewingangle, backlight):
                super().__init__(price, inches, ONOffstatus, volume, channel)
                TCL.screenthickness = screenthickness
                TCL.energyusage = energyusage
                TCL.lifespan = lifespan
                TCL.refreshrate = refreshrate
                TCL.viewingangle = viewingangle
                TCL.backlight = backlight

     def display(TCL):  # THE METHOD TO DISPLAY THE ADDITIONAL FEATURES OF THE TV
         print("the additional features of tv are")
         print("screen thickness is", TCL.screenthickness)
         print("energy usage of tv is ", TCL.energyusage)
         print("life span of tv is", TCL.lifespan)
         print("refreshrate of tv is", TCL.refreshrate)
         print("viewing angle of tv is", TCL.viewingangle)
         print("backlight of tv is", TCL.backlight)
class plasma(Led):  # SUBCLASS AND WE USED THE CONCEPT OF INHERITANCE
      pass
t = plasma(50000, 55, 'onoff', 10, 30, 1, '20kw', '20years', '0.5sec', '31degress', '75percent')
t.increasevolume()  # CALLING THE METHOD OF A CLASS
t.decreasevolume()
t.chan()
t.resetTv()
t.status()
t.display()
