import random

# constant values

'''
dummy CAN FRAME SPECIFICATION
2 bits - MODULE
4 bits - Function
6 bits - value 

|----|-------|-------------|
|2   | 3     | 6           |
|1 1 | 1 1 1 | 1 1 1 1 1 1 |
|Mod | Function.| Value       |
|----|-------|-------------|
'''
'''
01 ENGINE
*Functionality:
010 - speed
020 - gear indicator
*Value 
according to selected functionality

46 COMFORT
010 - Windows
100 - Mirrors

03 ABS (module)
001 ABS
010 ESP
100 TC

08 HVAC
001 - Temp
010 - Fan speed
100 - Zone

16 STEERING
001 - Rotation (degree)
010 - Mode (Race, Comfort, Auto)

37 NAVIGATION
001 - Height above see level
010 - Latitude
020 - Longitude
100 - number of satellites

56 RADIO
010 - Band (AM/FM)
050 - Current Frequency
100 - RDS

35 CENTRAL LOCK
001 - door lock status
'''

czytnik = {
    "ENGINE": {"Speed": "010", "Gear Indicator": "020"},
    "COMFORT": {"Windows": "010", "Mirrors": "100"},
    "ABS": {"ABS": "001", "ESP": "010", "TC": "100"},
    "HVAC": {"Temp": "001", "Fan Speed": "010", "Zone": "100"},
    "STEERING_WHEEL": {"Rotation": "001", "Mode": "010"},
    "RADIO": {"Band": "010", "Current Frequency": "050", "RDS": "100"},
    "CENTRAL_LOCK": {"Door lock status": "001"},
    "NAVIGATION": {"Height above see level": "001", "Latitude": "010", "Longitude": "020", "Number of satellites": "100"}
}
# Module listing with IDs
modulesList = {
    'ENGINE': '01',
    'COMFORT': '46',
    'ABS': '03',
    'HVAC': '08',
    'STEERING_WHEEL': '16',
    'NAVIGATION': '37',
    'RADIO': '56',
    'CENTRAL_LOCK': '35'
}

SPEED = 50
LONGITUDE = 14.552
LATITUDE = 53.428
HEIGHT = 25
ITER = 0


def engine():
    global SPEED

    st = "01"
    list_of_functions = ['010']

    function_choice = random.choice(list_of_functions)
    st += function_choice

    SPEED += random.randint(-4, 10)

    st += '0000' + str(SPEED)
    return st


def comfort():
    st = "46"

    st += '010'
    st += '000001'

    return st


def abs():
    st = "03"
    st += "001"
    st += "000000"

    return st


def hvac():
    st = "08"
    st += "001"
    st += '000017'

    return st


def steering_wheel():
    st = "16"
    st += '010'
    st += '000002'

    return st


def navi():
    global HEIGHT
    st = "37"
    st += "001"
    st += '0000' + str(HEIGHT)

    return st


def radio():
    st = "56"
    st += "010"
    st += "000001"

    return st


def central_lock():
    st = "35"
    st += '001'
    st += '000001'

    return st


functionList = [engine, comfort, abs, hvac, steering_wheel, navi, radio, central_lock]


def read_can_network():
    global ITER
    res = functionList[ITER]()

    if ITER < len(functionList) - 1:
        ITER += 1
    else:
        ITER = 0

    return res
