import * as Blockly from 'blockly';
import {
  gesture,
  axis,
} from '../constants/dropdown-options/codi_accelerometer';

export const blocks = Blockly.common.createBlockDefinitionsFromJsonArray([
  {
    type: 'codi_accelerometer_detected',
    message0: '%{BKY_CODI_ACCELEROMETER_DETECTED}',
    args0: [
      {
        type: 'field_dropdown',
        name: 'GESTURE',
        options: gesture,
      },
    ],
    output: 'Boolean',
    style: 'accelerometer_blocks',
  },
  {
    type: 'codi_accelerometer_angle',
    message0: '%{BKY_CODI_ACCELEROMETER_ANGLE}',
    args0: [
      {
        type: 'field_dropdown',
        name: 'AXIS',
        options: axis,
      },
    ],
    output: 'Number',
    style: 'accelerometer_blocks',
  },
]);
