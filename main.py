# Example of GET method for adding data to a Thingspeak channel

# This code can be executed from repl.it

# Python 3 only:
angle = 191
current = 10
z = abs(angle - current)
y = (angle - current) % 360
x = abs(angle - current) % 360
if abs(angle - current) > 180:
  l = 360 - x
else:
  l = x
print(z)
print(y)
print(x)
print(l)

print('step = ', int((abs(angle - current)/360)*512*8))
if x < 180:
  if angle > current:
    step = int(((l)/360)*512*8)
    print('clockwise')
    print(step)
  if angle < current:
    step = int(((l)/360)*512*8)
    print('counterclockwise')
    print(step)
if x > 180: 
  if angle < current:
    step = int(((l)/360)*512*8)
    print('clockwise')
    print(step)
  if angle > current:
    step = int(((l)/360)*512*8)
    print('counterclockwise')
    print(step)


'''
print(x)
print('step = ', int((abs(angle - current)/360)*512*8))
if x > 180:
  if current > angle:
    l = (360 - current) + (angle)
  if current < angle:
    l = (360 - angle) + (current)
  step = int((abs(l)/360)*512*8)
  print('counterclockwise')
  print(step)
if x < 180: 
  step = int((abs(x)/360)*512*8)
  print('clockwise')
  print(step)
'''
'''
from urllib.request import urlopen
from urllib.parse import urlencode

import random, time

api = "KA31NDKQWNO6M5SJ"   # Enter your API key

while True:
  params = {
    "api_key":api,
    1: random.randrange(100,1000),
    2: random.randrange(100,1000),
    3: random.randrange(100,1000) }
  params = urlencode(params)   # put dict data into a GET string

  # add "?" to URL and append with parameters in GET string:
  url = "https://api.thingspeak.com/update?" + params
  try:
    response = urlopen(url)      # open the URL to send the request
    print(response.status, response.reason)  # display the response
    print(response.read()) # display response page data
    time.sleep(16)    # 15 sec minimum
  except Exception as e:
    print(e)
'''