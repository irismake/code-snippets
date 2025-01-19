import * as Blockly from 'blockly/core';
import { Order } from 'blockly/python';
import { DefinedOrder } from '../../constants/order';
import { type MicroPythonGenerator } from '../microPython';
import {
  axisConfiguration,
  gestureConfiguration,
} from '../../constants/configurations/codi_accelerometer';

export const forBlock = Object.create(null);

const accelerometerAllocate = `i2c_accelerometer = machine.I2C(0, sda=21, scl=22)
accelerometerSensor = qma6100p.Qma6100p(i2c_accelerometer)`;

const getRotationAngleFunction = `def getRotationAngle(accelerometerSensor, axis):
    accelerometerSensor.tick()
    if axis == "pitch":
        X, Y = accelerometerSensor.x, accelerometerSensor.y
    else:
        X, Y = accelerometerSensor.y, accelerometerSensor.x
    Z = accelerometerSensor.z
    if Z == 0:
        print('z=0')
        return 0
    denominator = math.sqrt(Y**2 + Z**2)
    result_rad = math.atan(X / denominator)
    result_deg = math.degrees(result_rad)
    if Z < 0:
        if result_deg > 0:
            result_deg = 180 - result_deg
        elif result_deg < 0:
            result_deg = abs(result_deg) - 180
    return result_deg\n`;

const gestureDetectionFunction = `def gestureDetection(accelerometerSensor, gesture):
    accelerometerSensor.tick()
    gesture_to_posture = {
        0: accelerometer.Accelerometer.POSTURE_SHAKE,
        1: accelerometer.Accelerometer.POSTURE_X_POSITIVE_TILT,
        2: accelerometer.Accelerometer.POSTURE_X_NEGATIVE_TILT,
        3: accelerometer.Accelerometer.POSTURE_Y_POSITIVE_TILT,
        4: accelerometer.Accelerometer.POSTURE_Y_NEGATIVE_TILT,
        5: accelerometer.Accelerometer.POSTURE_FACE_UP,
        6: accelerometer.Accelerometer.POSTURE_FACE_DOWN,
        7: accelerometer.Accelerometer.POSTURE_FREE_FALL
    }
    desired_posture = gesture_to_posture.get(gesture)
    current_posture = accelerometerSensor.posture
    return current_posture == desired_posture\n`;

forBlock['codi_accelerometer_detected'] = function (
  block: Blockly.Block,
  generator: MicroPythonGenerator,
) {
  const gestureValue = block.getFieldValue('GESTURE');
  const { gesture } = gestureConfiguration(gestureValue);

  generator.addModuleDefinition('accelerometer', 'import accelerometer');
  generator.addModuleDefinition('qma6100p', 'import qma6100p');

  generator.addGlobal(
    `codi_accelerometer`,
    accelerometerAllocate,
    DefinedOrder.ALLOCATE,
  );
  generator.addGlobal(
    `codi_accelerometer_detected`,
    gestureDetectionFunction,
    DefinedOrder.FUNCTION,
  );

  return [`gestureDetection(accelerometerSensor, ${gesture})`, Order.NONE];
};

forBlock['codi_accelerometer_angle'] = function (
  block: Blockly.Block,
  generator: MicroPythonGenerator,
) {
  const axisValue = block.getFieldValue('AXIS');
  const { axis } = axisConfiguration(axisValue);

  generator.addModuleDefinition('qma6100p', 'import qma6100p');
  generator.addGlobal(
    `codi_accelerometer`,
    accelerometerAllocate,
    DefinedOrder.ALLOCATE,
  );
  generator.addGlobal(
    `codi_accelerometer_angle`,
    getRotationAngleFunction,
    DefinedOrder.FUNCTION,
  );

  return [`getRotationAngle(accelerometerSensor, "${axis}")`, Order.NONE];
};
