import * as Blockly from 'blockly/core';
import { DefinedOrder } from '../../constants/order';
import { type MicroPythonGenerator } from '../microPython';

export const forBlock = Object.create(null);

const defaultMatrixValue = '.....\n.....\n.....\n.....\n.....';
const dotmatrixGlobalKey = 'codi_dotmatrix';
const dotmatrixObjectAllocate =
  'matrix_led_5x5 = x16k33_matrix_led_5x5.X16k33MatrixLed5x5(i2c=machine.I2C(0, sda=21, scl=22), i2c_address=0x75)';

const arrayToSting = (array: number[][]) => {
  // 0 to '.', 1 to '#'
  const result = array.map((row) => row.map((col) => (col === 0 ? '.' : '#')));
  return result.map((row) => `${row.join('')}`).join('\n');
};

forBlock['codi_dotmatrix_draw'] = function (
  block: Blockly.Block,
  generator: MicroPythonGenerator,
) {
  const matrixValue = block.getFieldValue('MATRIX') || defaultMatrixValue;
  generator.addModuleDefinition(
    'x16k33_matrix_led_5x5',
    'import x16k33_matrix_led_5x5',
  );

  generator.addGlobal(
    dotmatrixGlobalKey,
    dotmatrixObjectAllocate,
    DefinedOrder.ALLOCATE,
  );

  return `matrix_led_5x5.show_leds("""\n${arrayToSting(matrixValue)}\n""")\n`;
};