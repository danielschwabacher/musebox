#include <IRremoteInt.h>
#include <IRremote.h>

/*
  Circuit Specs:
  Ground colors: Black/Green
  Positive lead colors: Red/Orange
  LED resistors: 220 Ohms
*/


// If 1, Comms to Pi are disabled.
int PI_COMM_LOCKED = 1;

// White LED, blinks when ready for inputs
int STANDBY_LED = 8;
// Yellow LED, blinks when data is transmitted between systems
int PROCESSING_LED = 9; 
// Green LED, solid when playing music
int PLAYING_LED = 6;
// Red LED, solid when paused
int STOPPED_LED = 5;
// Blue LED, not sure yet
int EXTRA_LED = 4;


int is_playing = false;

// IR module
int IR_RECV_PIN = 7;

IRrecv irrecv(IR_RECV_PIN);
decode_results ir_results;

boolean processing_on = false;
String serial_code = "";


int CODE_CONTEXT = -1;

void setup(){
  Serial.begin(28800); 
  pinMode(STANDBY_LED, OUTPUT);
  pinMode(PROCESSING_LED, OUTPUT);
  pinMode(PLAYING_LED, OUTPUT);
  pinMode(STOPPED_LED, OUTPUT);
  pinMode(EXTRA_LED, OUTPUT);
  irrecv.enableIRIn();
  // Serial.println("Started Arduino Recivers.");
}

// Return a single character representing 
// the DO_CODE recieved over serial
// CODES:
// 1 - Play (p)
void update_code(){
   serial_code = Serial.readString();
   if (serial_code == "p"){
     CODE_CONTEXT = 1;
     return;  
   }
   if (serial_code == "r"){
     CODE_CONTEXT = 2;
     return;  
   }
   if (serial_code == "x"){
     CODE_CONTEXT = 3;
     return;  
   }
   if (serial_code == "n"){
     CODE_CONTEXT = 4;
     return;  
   } 
   return;
}


void loop(){  
  // digitalWrite(STANDBY_LED, LOW);
  if (irrecv.decode(&ir_results)){
    Serial.write(ir_results.value);
  }
  if (Serial.available() > 0){
    update_code();
    switch (CODE_CONTEXT){
      case 1:
        is_playing = !is_playing;
        digitalWrite(PLAYING_LED, is_playing);
        break;
      default:
        break;    
    }
  }
  irrecv.resume();
  delay(1000);
}
