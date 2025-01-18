//LED 모래시계 동작 코드

#include "LedControl.h"

#define  MATRIX_A  0
#define  MATRIX_B  1

// Matrix
#define PIN_DATAIN 3
#define PIN_CLK 2
#define PIN_LOAD 4         

// Accelerometer

#define PIN_X A6
#define PIN_Y A7
 
long setTime = 18000; // 18초 (시간을 변경하고 싶다면 이부분을 수정하세요)
int interval = setTime/64;
int dir[2];
int currentMatrix;
int DotMatrix[8][8];
int DotX[8][8];
int DotY[8][8];
bool array[2][8][8];
int space = 8;
bool isAble = false;
unsigned long startMills;

LedControl lc = LedControl(PIN_DATAIN, PIN_CLK, PIN_LOAD, 2);

void setup(){
  Serial.begin(9600);
  lc.shutdown(0,false);
  lc.shutdown(1,false);
  lc.setIntensity(0,2);
  lc.setIntensity(1,2);
  Serial.begin(9600);
  startMills = millis();

  for(int i = 0;i<8;i++){
    for(int j = 0;j<8;j++){
      DotMatrix[i][j] = 1;
      DotX[i][j] = i;
      DotY[i][j] = j;
      lc.setLed(1,i,j,true);
      array[1][i][j] = true;
    }
  }
} 

 

void loop(){

  for(int i =0;i<8;i++){
    for(int j = 0;j<8;j++){
      Move(i,j);
    }
  }

  unsigned long time = millis();

  if((time-startMills) > interval){
    isAble = true;
    startMills = time;
  }

}

 

void Move(int i,int j){

  GetDirection();

  int newX = DotX[i][j];
  int newY = DotY[i][j];
  int newMatrix = DotMatrix[i][j];

  newX+=dir[0];
  newY+=dir[1];

  if(newMatrix == 0 && newX == -1 && newY == 8 && isAble){
    newMatrix = 1;
    newX =7;
    newY=0;
  }
 
  if(newMatrix == 1 && newX == 8 && newY == -1 && isAble){
    newMatrix = 0;
    newX = 0;
    newY = 7;
  }

  if(!IsMovable(newMatrix,newX,newY)){

    if(newMatrix != DotMatrix[i][j]){
      return;
    }

    bool isLeftMovable = IsMovable(newMatrix,DotX[i][j],newY);
    bool isRightMovable = IsMovable(newMatrix,newX,DotY[i][j]);

    if(!isLeftMovable && !isRightMovable){
      return;
    }

    if(isLeftMovable && isRightMovable){
      if(rand()>16383){
        isLeftMovable = false;
      }else{
        isRightMovable = false;
      }
    }

    if(isLeftMovable){
      newX =DotX[i][j];
    }else if(isRightMovable){
      newY = DotY[i][j];
    }
  }

  lc.setLed(DotMatrix[i][j],DotX[i][j],DotY[i][j],false);

  array[DotMatrix[i][j]][DotX[i][j]][DotY[i][j]] = false;


  if(DotMatrix[i][j] != newMatrix&&isAble){
    isAble = false;
  }

  DotMatrix[i][j] = newMatrix;
  DotX[i][j] = newX;
  DotY[i][j] = newY;

  lc.setLed(DotMatrix[i][j],DotX[i][j],DotY[i][j],true);
  array[DotMatrix[i][j]][DotX[i][j]][DotY[i][j]] = true;

}

bool IsMovable(int matrix, int x, int y){
  if(x>=space || y>=space || x<0 || y<0){
    return false;
  }
  return !array[matrix][x][y];
}

void GetDirection(){
  int x;
  int y;

  x = ChangeValue(analogRead(PIN_X)-330);
  y = ChangeValue(analogRead(PIN_Y)-330);

  if(x==1){
    if(y==1){
      dir[0]=0;
      dir[1]=1;

    }else if(y==-1){
      dir[0]=-1;
      dir[1]=0;
    }else{
      dir[0]=-1;
      dir[1]=1;
    }
  }else if(x==-1){
    if(y==1){
      dir[0]=1;
      dir[1]=0;
    }else if(y==-1){
      dir[0]=0;
      dir[1]=-1;
    }else{
      dir[0]=1;
      dir[1]=-1;
    }
  }else{ 
    if(y==1){
      dir[0]=1;
      dir[1]=1;
    }else if(y==-1){
      dir[0]=-1;
      dir[1]=-1;
    }else{
      dir[0]=0;
      dir[1]=0;
    }
  }
}

int ChangeValue(int value){

  if(value<40 && value>-40){
    return 0;
  }else if(value>=40){
    return 1;
  }else{
    return -1;
  }

}