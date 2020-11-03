import threading
#import serial
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
Place_Y_blue = None
ColorSensor_X = None
ColorSensor_Y = None
ColorSensor_Z = None
Place_Z_blue = None
R = None
Place_X_green = None
G = None
stop = None
Place_Y_green = None
B = None
Place_Z_green = None
MAX = None
Grab_X = None
Grab_Y = None
Grab_Z = None
Place_X_red = None
Place_Y_red = None
Place_Z_red = None
RedCount = None
GreenCount = None
BlueCount = None
PlacingInterval = None

#serdev = 'COM5:'  # serial device of JeVois

# JEVOIS CAMERA

def objectFound():
    with serial.Serial(serdev2, 6400, timeout=1) as ser:
        while 1:
            # Read a whole line and strip any trailing line ending character:
            line = ser.readline().rstrip()
            print("received: {}".format(line))
            # Split the line into tokens:
            tok = line.split()
            # Skip if timeout or malformed line:
            if len(tok) < 1:
                continue
            # Skip if not a standardized "Normal 2D" message:
            # See http://jevois.org/doc/UserSerialStyle.html
            if tok[0].decode('utf-8') != 'N2':
                continue
            # From now on, we hence expect: N2 id x y w h
            if len(tok) != 6:
                continue
            # Assign some named Python variables to the tokens:
            key, id1, x, y, w, h = tok
            id1 = (id1.decode('utf-8'))
            print(id1)
            return id1

"""Describe this function..."""
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

"""Describe this function..."""
def getcoler():
  global ColorSensor_X, ColorSensor_Y, ColorSensor_Z, R, G, B, MAX, Place_X_red, Place_Y_red, Place_Z_red, RedCount, GreenCount, Place_X_blue, Place_Y_blue, Place_Z_blue, BlueCount
  dType.SetPTPCmdEx(api, 0, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, 0, 1) #go to color sensor
  dType.SetWAITCmdEx(api, 2000, 1)
  R = dType.GetColorSensorEx(api, 0)
  G = dType.GetColorSensorEx(api, 1)
  B = dType.GetColorSensorEx(api, 2)
  MAX = max([R, G, B])
  if MAX == R:
    print('Red')
    dType.SetPTPCmdEx(api, 0, Place_X_red,  Place_Y_red,  Place_Z_red, 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)
    RedCount = RedCount + 1
  elif MAX == G:
    print('Green')
    dType.SetPTPCmdEx(api, 0, Place_X_red,  Place_Y_red,  Place_Z_red, 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)
    GreenCount = GreenCount + 1
  else:
    print('Blue')
    dType.SetPTPCmdEx(api, 0, Place_X_blue,  Place_Y_blue,  Place_Z_blue, 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)
    BlueCount = BlueCount + 1


INITIALIZE()
print('START')
while stop < 3:
  #print(dType.GetInfraredSensor(api, 1)[0])
  if (dType.GetInfraredSensor(api, 1)[0]) == 0:
    #objectid = objectFound()
    objectid = 'cube' #test
    if (objectid == 'cube'):
      dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  Grab_Z, 0, 1) #go to items position
      dType.SetEndEffectorSuctionCupEx(api, 1, 1) #sunction cup on = grap item
      getcoler()
      stop = stop + 1
      print('RESULTS')
      print('Blue: ',BlueCount)
      print('Green: ', GreenCount)
      print('Red', RedCount)
