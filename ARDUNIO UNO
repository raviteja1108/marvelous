#include "U8glib.h"
U8GLIB_ST7920_128X64 u8g(13,11,10,U8G_PIN_NONE); //SPI
#include<SoftwareSerial.h>
#include<stdlib.h>
SoftwareSerial mySerial(2,3); //Rx,Tx pins
int no_of_items=0;
float item_price, total_price=0; 

void draw(String item_name,String item_p,String total_p,String total_items) {
  u8g.firstPage();
  for(int i=0;i<8;i++){
  u8g.setFont(u8g_font_unifont);
  u8g.setPrintPos(0,16);
  u8g.print(item_name);
  u8g.setPrintPos(0,32);
  u8g.print("Price: ");
  u8g.setPrintPos(64,32);
  u8g.print(item_p);
  u8g.setPrintPos(0,48);
  u8g.print("Count: ");
  u8g.setPrintPos(64,48);
  u8g.print(total_items);
  u8g.setPrintPos(0,64);
  u8g.print("Total: ");
  u8g.setPrintPos(64,64);
  u8g.print(total_p);  
  delay(1000);
  u8g.nextPage();
  }
  //delay(3000);
}
void intro(){
  u8g.firstPage();
  for(int i=0;i<8;i++){
    u8g.setFont(u8g_font_unifont);
    u8g.drawStr(38,16,"WELCOME");
    u8g.drawStr( 56,30 , "TO");
    u8g.drawStr( 34, 44, "ACE MART");
    delay(500);
    u8g.nextPage();
  }
  delay(5000);
}
void setup(void) {
  Serial.begin(115200);
  mySerial.begin(9600);
  // flip screen, if required
  u8g.setRot180();
  if ( u8g.getMode() == U8G_MODE_R3G3B2 ) {
    u8g.setColorIndex(255);     // white
  }
  else if ( u8g.getMode() == U8G_MODE_GRAY2BIT ) {
    u8g.setColorIndex(3);         // max intensity
  }
  else if ( u8g.getMode() == U8G_MODE_BW ) {
    u8g.setColorIndex(1);         // pixel on
  }
  else if ( u8g.getMode() == U8G_MODE_HICOLOR ) {
    u8g.setHiColorByRGB(255,255,255);
  }
  
  pinMode(8, OUTPUT);
  intro();
  delay(3000);
}

void loop(void) {
  String s1="",s2="",s3="",id="",item="";
  String msg=mySerial.readStringUntil('\r');
  Serial.println(msg);
  //Serial.println("msg");
  //String msg="1234560001:MAGGI(500g):56.00";
  int count_req=0;
  int i=0;
  while(msg[i]!='\0'){
    if(msg[i]==':'){
      count_req++;
    }
    i++;
  }
  if(count_req==2){
      int d1=msg.indexOf(":");
      int d2=msg.indexOf(":",d1+1);
      i=0;
      while(msg[i]!='\0'){
        if(i<d1){
          s1+=msg[i];
        }
        else if(i>d1 and i<d2){
          s2+=msg[i];
        }
        else if(i>d2){
          s3+=msg[i];
        }
        i++;
      }
    id=s1;
    item=s2;
    item_price=s3.toFloat();
    total_price+=item_price;
    no_of_items+=1;
    delay(3000);
  }
  String tp=String(total_price);
  String noi=String(no_of_items);
  draw(item,s3,tp,noi);
}
