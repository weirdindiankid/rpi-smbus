import tsl2591
import time

while 1:
	tsl = tsl2591.Tsl2591()
	full, ir = tsl.get_full_luminosity()
	lux= tsl.calculate_lux(full, ir)
	print("\nLux = ", lux)
	print("\rFull = ", full)
	print("\rIR = ", ir)
		
	time.sleep(0.5)

 
