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
Calibration_X = None
Calibration_Y = None
Calibration_Z = None
Calibration_X2 = None
Calibration_Y2 = None
Calibration_Z2 = None
Calibration_X3 = None
Calibration_Y3 = None
Calibration_Z3 = None
Calibration_X4 = None
Calibration_Y4 = None
Calibration_Z4 = None
Place_X = None
Place_Y = None
Place_Z = None
HOME_X = None
HOME_Y = None
HOME_Z = None
j = None
k = None
CAL = None
time_start = None

print('[HOME] Restore to home position at first launch, please wait 30 seconds after turnning on the Dobot Magician.')
print('[BLOCKS] Place them besides the non-motor side of the conveyor belt, the same side where the pick and place arm is.')
print('[PLACING BLOCKS] Place the blocks by 3×3.')
print('[CALIBRATION POINT] Looking from the back of Dobot, the top left block is the calibration point.')
print('[CALIBRATION] Set the first variable to 0 to test the calibration point, then set 1 to start running.')
print('[DIRECTION] Standing behind Dobot Magician facing its front direction, X is front and back direction, Y is left and right direction. ')
print('[CONNECTION] Motor of the conveyor belt connects to port Stepper1.')
Calibration__0__Run__1 = 1
#Item 1
Calibration_X = 239.2877
Calibration_Y = 90.1665
Calibration_Z = -41.5215
#Item 2
Calibration_X2 = 229.3061
Calibration_Y2 = 69.6169
Calibration_Z2 = -41.1566
#Item 3
Calibration_X3 = 216.6747
Calibration_Y3 = 102.4487
Calibration_Z3 = -41.5052
#Item 4
Calibration_X4 = 206.5388
Calibration_Y4 = 80.5626
Calibration_Z4 = -41.6049
Place_X = 246.8
Place_Y = -113
Place_Z = 16
HOME_X = 211.5673
HOME_Y = -0.0002
HOME_Z = 134.9425
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
dType.SetPTPJointParamsEx(api,400,400,400,400,400,400,400,400,1)
dType.SetPTPCommonParamsEx(api,100,100,1)
dType.SetPTPJumpParamsEx(api,40,100,1)
dType.SetEndEffectorSuctionCupEx(api, 1, 1)
STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
dType.SetEMotorEx(api, 0, 0, int(vel), 1)
CAL = 1
print("Calibration ended")
if Calibration__0__Run__1:
  for count in range(4):
    #initialize variables
    j = 0
    k = 0
    if CAL == 1:
      dType.SetPTPCmdEx(api, 0, (Calibration_X - j),  (Calibration_Y - k),  (Calibration_Z - 10), 0, 1)
      print('ITEM 1')
    elif CAL == 2:
      dType.SetPTPCmdEx(api, 0, (Calibration_X2 - j),  (Calibration_Y2 - k),  (Calibration_Z2 - 10), 0, 1)
      print('ITEM 2')
    elif CAL == 3:
      dType.SetPTPCmdEx(api, 0, (Calibration_X3 - j),  (Calibration_Y3 - k),  (Calibration_Z3 - 10), 0, 1)
      print('ITEM 3')
    else:
      dType.SetPTPCmdEx(api, 0, (Calibration_X4 - j),  (Calibration_Y4 - k),  (Calibration_Z4 - 10), 0, 1)
      print('ITEM 4')
    CAL = CAL + 1
    dType.SetEndEffectorSuctionCupEx(api, 1, 1)
    dType.SetWAITCmdEx(api, 0.5, 1)
    dType.SetPTPCmdEx(api, 0, Place_X,  Place_Y,  Place_Z, 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)
    dType.SetWAITCmdEx(api, 0.5, 1)
    j = j + 25
    if j == 75:
      k = k + 25
      j = 0
    dType.SetPTPCmdEx(api, 7, 0,  0,  20, 0, 1)
    time_start = dType.gettime()[0]
    STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
    MM_PER_CRICLE = 3.1415926535898 * 36.0
    vel = float(50) * STEP_PER_CRICLE / MM_PER_CRICLE
    dType.SetEMotorEx(api, 0, 1, int(vel), 1)
    while True:
      if (dType.gettime()[0]) - time_start >= 4:
        STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
        MM_PER_CRICLE = 3.1415926535898 * 36.0
        vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
        dType.SetEMotorEx(api, 0, 0, int(vel), 1)
        break
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetPTPCmdEx(api, 0, HOME_X,  HOME_Y,  HOME_Z, 0, 1)
  CAL = 1
