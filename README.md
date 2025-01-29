# FrequencyGenerators
Used ChatGPT to write code for SI5351A for Arduino Uno and RasPi5.  It currently generates frequencies of:
8.8MHz on Channel 0
14.175MHz on Channel 1
60MHz on Channel 2

8.8MHz and 14.175MHz are specific to testing the function of Kenwood TS820S radio.

Arduino code requires Etherkit Si5351 library by Jason Milldrum.  It appears to work, though the plotter only shows the level the frequency is at.  The arduino is too slow to read and show the waveform.

The Python code requires matplotlib and adafruit-circuitpython-si5351.  This needs tested, and should display the waveform to the screen. Unfortunately, I am having trouble loading all the dependencies.  The adafruit-circuitpython-si5351 code also relies on RPi.GPIO, which is not currently supported on Pi5.
