# Copyright (c) 2016
# Author: Eddie Fiorentine
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time
import smbus

#Constants
MLX_DEFAULT_ADDRESS = 0x5a
MLX_RAM_ADDR = 0x07
SMBUS = smbus.SMBus(1)

#Base functionality
def read_temp(addr = MLX_DEFAULT_ADDRESS, reg = MLX_RAM_ADDR, bus = SMBUS):
	tempObj = None
	try:
		tempObj = bus.read_byte_data(addr, reg)
	except:
		print("Error reading MLX90614 Sensor...")
		