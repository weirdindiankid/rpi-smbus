# rpi-smbus
A couple of important fixes to the python-smbus modules used to handle I2C on the Raspberry Pi

## Installation Instructions
NB: This is incomplete code and not safe to use.

### Steps you need to take (TSL2591 specific)

1. Edit i2c baudrate to 8000
2. Connect Vin to the 5V out from the RPi

## Explanation
I will add more details when I have a second to breathe but for now, a simple explanation is that <a href="http://www.advamation.com/knowhow/raspberrypi/rpi-i2c-bug.html" target="_blank">I2C clock stretching is buggy on the Pi</a>.

Additionally, the 1.8 kOhm pull-up resistors are not enough to handle the 400KHz rate of the TSL2591 sensor.

As a workaround, then, we choose to attempt multiple bus writes and reads until one of them succeeds. This can be fixed a lot more elegantly but for now, since this was only a proof of concept, I will let this remain.

### Litmus Tests
To verify the device ID (should return 0x50 if configured correctly) run:

<code>python3 deviceid.py</code>

To get sensor values run:

<code>python3 poll.py</code>

The sensor's accuracy hasn't been tested and is worth verifying against comparable sensors at some point in the future.
