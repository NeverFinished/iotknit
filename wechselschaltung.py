from iotknit import *

light_state = False

init("localhost")  # replace with your MQTT broker address

prefix("node1")
light1 = publisher("light")

prefix("node2")
light2 = publisher("light")

light1.publish("set", "off")
light2.publish("set", "off")


def on_button(msg):
    global light_state
    if msg == "pressed":
        light_state = not light_state
        state = "on" if light_state else "off"
        light1.publish("set", state)
        light2.publish("set", state)


prefix("node1")
button1 = subscriber("button")
button1.subscribe(callback=on_button)

prefix("node2")
button2 = subscriber("button")
button2.subscribe(callback=on_button)

run()
