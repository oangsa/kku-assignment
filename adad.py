from machine import Pin, PWM
from time import sleep
import dht

SW = Pin(5, Pin.IN)
LED = Pin(3, Pin.OUT)
sensor = dht.DHT11(Pin(4))
buzzer = PWM(Pin(4, Pin.OUT))

while True:
    LED.value(0)
    status = SW.value()
    buzzer.init(freq=22, duty=22)
    print(status)
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    humid = sensor.humidity()
    if status == 1:
        if temp >= 25:
            buzzer.init(freq=22, duty=22)
        else:
            LED.value(1)
    else:
        pass

    print("Temperature: " + str(temp) + " C")
    print("Humidity: " + str(humid) + "%")
    print()