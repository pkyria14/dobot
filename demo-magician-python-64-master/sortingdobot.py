import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

# Load Dll and get the CDLL object
api = dType.load()
# Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:", CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
    Calibration__0__Run__1 = None
Place_X_blue = None
ColorSensor_X = None
ColorSensor_Y = None
ColorSensor_Z = None
Place_Y_blue = None
R = None
Place_Z_blue = None
G = None
Place_X_green = None
stop = None
B = None
Place_Y_green = None
MAX = None
Place_Z_green = None
Place_X_red = None
Grab_X = None
Grab_Y = None
Grab_Z = None
Place_Y_red = None
Place_Z_red = None
RedCount = None
GreenCount = None
BlueCount = None
PlacingInterval = None

"""Describe this function...
"""
def INITIALIZE():
  global Place_X_blue, Place_Y_blue, Place_Z_blue, Place_X_green, Place_Y_green, Place_Z_green, Place_X_red, Place_Y_red, Place_Z_red, Grab_X, Grab_Y, Grab_Z, ColorSensor_X, ColorSensor_Y, ColorSensor_Z, PlacingInterval, stop, RedCount, BlueCount, GreenCount
  Place_X_blue = 211.3298
  Place_Y_blue = 45.9067
  Place_Z_blue = -36.1904
  Place_X_green = 122.1451
  Place_Y_green = 121.2453
  Place_Z_green = -35.9775
  Place_X_red = 160.4537
  Place_Y_red = 96.399
  Place_Z_red = -32.8536
  Grab_X = 254.9184
  Grab_Y = -109.7544
  Grab_Z = 15.6738
  ColorSensor_X = 154.369
  ColorSensor_Y = -115.7922
  ColorSensor_Z = 27.9397
  PlacingInterval = 40
  stop = 0
  dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
  RedCount = 0
  BlueCount = 0
  GreenCount = 0
  dType.SetColorSensor(api, 1 ,1, 0)
  dType.SetInfraredSensor(api, 1 ,1, 0)
  dType.SetWAITCmdEx(api, 1, 1)
  dType.SetPTPJointParamsEx(api,200,200,200,200,200,200,200,200,1)
  dType.SetPTPCommonParamsEx(api,100,100,1)
  dType.SetPTPJumpParamsEx(api,50,100,1)

"""Describe this function...
"""
def getcoler():
  global ColorSensor_X, ColorSensor_Y, ColorSensor_Z, R, G, B, MAX, Place_Y_red, RedCount, Place_X_red, Place_Z_red, Place_X_green, Place_Y_green, Place_Z_green, GreenCount, Place_X_blue, Place_Y_blue, Place_Z_blue, BlueCount
  dType.SetPTPCmdEx(api, 0, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, 0, 1)
  dType.SetWAITCmdEx(api, 5, 1)
  R = dType.GetColorSensorEx(api, 0)
  G = dType.GetColorSensorEx(api, 1)
  B = dType.GetColorSensorEx(api, 2)
  MAX = max([R, G, B])
  if MAX == R:
    print('Red')
    dType.SetPTPCmdEx(api, 0, Place_X_red,  Place_Y_red,  Place_Z_red, 0, 1)
    RedCount = RedCount + 1
  elif MAX == G:
    print('Green')
    dType.SetPTPCmdEx(api, 0, Place_X_green,  Place_Y_green,  Place_Z_green, 0, 1)
    GreenCount = GreenCount + 1
  else:
    print('Blue')
    dType.SetPTPCmdEx(api, 0, Place_X_blue,  Place_Y_blue,  Place_Z_blue, 0, 1)
    BlueCount = BlueCount + 1
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)


INITIALIZE()
print('START')
while stop < 3:
  print(dType.GetInfraredSensor(api, 1)[0])
  if (dType.GetInfraredSensor(api, 1)[0]) == 0:
    dType.SetEndEffectorSuctionCupEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  Grab_Z, 0, 1)
    getcoler()
    stop = stop + 1
    print('RESULTS')
    print(BlueCount)
    print(GreenCount)
    print(RedCount)
