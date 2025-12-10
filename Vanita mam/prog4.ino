int buttonPin =2;
int ledPin = 13;
int buttonState =0;
int lastButtonState = 0;
int ledState = LOW;
void setup()
{
 pinMode(buttonPin,INPUT);
 pinMode(ledPin,OUTPUT); 
}
void loop()
{
 buttonState = digitalRead(buttonPin);

	if(buttonState == HIGH && lastButtonState ==LOW)
 	{
   		ledState = !ledState;
  	    digitalWrite(ledPin,ledState);
 	}
	else
 	{
  		digitalWrite(ledPin,ledState);
 	}
 lastButtonState = buttonState;
}