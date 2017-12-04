const int sPin = 2;
const int camPin = 4;
int sStatus = 0;

void setup(){
  pinMode(sPin, INPUT); //listen at dpin 2
  Serial.begin(9600);
  
}
void loop(){
  sStatus = digitalRead(sPin);
  //digitalWrite(vPin, HIGH);
  if (takenPic(sStatus)){
    Serial.println("Switch is on, taking pic...!");
    }
    else{
      Serial.println("Switch is off");
      }

  }


bool takenPic(int statusP){ 
  if(statusP == HIGH){
    digitalWrite(camPin, HIGH);
    return camPin == LOW;
    }
    else
    {
    digitalWrite(camPin, LOW);
    return camPin == HIGH;
    }

  
  }
