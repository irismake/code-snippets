// 블럭 생성 코드

import * as Blockly from 'blockly';

export const blocks = Blockly.common.createBlockDefinitionsFromJsonArray([
  {
    type: 'codi_dotmatrix_draw',
    message0: '%{BKY_CODI_DOTMATRIX_DRAW}',
    args0: [
      {
        type: 'codi_field_matrix',
        name: 'MATRIX',
        value: [
          [0, 1, 0, 1, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0],
        ],
      },
    ],
    style: 'dotMatrix_blocks',
    previousStatement: null,
    nextStatement: null,
  },
]);
  