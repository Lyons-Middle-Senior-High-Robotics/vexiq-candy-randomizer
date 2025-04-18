// User defined function
void myblockfunction_turnAllLedsOff();
// User defined function
void myblockfunction_turnAllLedsOn();

int Brain_precision = 0;

float myVariable, led, picked, Red;

float Colors[3];

// User defined function
void myblockfunction_turnAllLedsOff() {
  TouchLED1.setColor(colorType::none);
  TouchLED2.setColor(colorType::none);
  TouchLED3.setColor(colorType::none);
}

// User defined function
void myblockfunction_turnAllLedsOn() {
  TouchLED1.setColor(red);
  TouchLED2.setColor(blue);
  TouchLED3.setColor(green);
}

// "when started" hat block
int whenStarted1() {
  myblockfunction_turnAllLedsOn();
  Colors[0] = 3.0;
  Colors[1] = 2.0;
  Colors[2] = 1.0;  return 0;
}

int mathRandomInt(float a, float b) {
  if (a > b) {
    // Swap a and b to ensure a is smaller.
    float c = a;
    a = b;
    b = c;
  }
  int tmpA = static_cast<int>(a);
  int tmpB = static_cast<int>(b);
  int r = tmpA + rand() / (RAND_MAX / (tmpB - tmpA + 1));
  return r;
}

// "when Bumper1 pressed" hat block
void onevent_Bumper1_pressed_0() {
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1, 1);
  Brain.Screen.print(printToBrain_numberFormat(), static_cast<float>(Colors[static_cast<int>(picked) - 1]));
  Brain.Timer.reset();
  while ((Brain.Timer.value() < 5.0)) {
    led = static_cast<float>(mathRandomInt(1.0, 3.0));
    myblockfunction_turnAllLedsOff();
    if (led == 1.0) {
      Brain.playNote(3, 0, 250);
      TouchLED1.setColor(red);
    } else if (led == 2.0) {
      Brain.playNote(3, 1, 250);
      TouchLED2.setColor(blue);
    } else {
      Brain.playNote(3, 2, 250);
      TouchLED3.setColor(green);
    }
    wait(0.1, seconds);
  wait(20, msec);
  }
  if (picked == led) {
    Brain.playSound(tada);
    Brain.Screen.newLine();
    Brain.Screen.print("Winner Winner Chicken DInner");
  }
  else {
    Brain.playSound(wrongWaySlow);
    Brain.Screen.newLine();
    Brain.Screen.print("Better Luck Next Time");
  }
  wait(3.0, seconds);
  myblockfunction_turnAllLedsOn();
}

// "when TouchLED1 pressed" hat block
void onevent_TouchLED1_pressed_0() {
  picked = 1.0;
  TouchLED1.setColor(colorType::none);
  wait(0.5, seconds);
  TouchLED1.setColor(red);
  wait(0.5, seconds);
  TouchLED1.setColor(colorType::none);
  wait(0.3, seconds);
  TouchLED1.setColor(red);
  wait(0.5, seconds);
}

// "when TouchLED3 pressed" hat block
void onevent_TouchLED3_pressed_0() {
  picked = 3.0;
  TouchLED3.setColor(colorType::none);
  wait(0.5, seconds);
  TouchLED3.setColor(green);
  wait(0.5, seconds);
  TouchLED3.setColor(colorType::none);
  wait(0.3, seconds);
  TouchLED3.setColor(green);
  wait(0.5, seconds);
}

// "when TouchLED2 pressed" hat block
void onevent_TouchLED2_pressed_0() {
  picked = 2.0;
  TouchLED2.setColor(colorType::none);
  wait(0.5, seconds);
  TouchLED2.setColor(blue);
  wait(0.5, seconds);
  TouchLED2.setColor(colorType::none);
  wait(0.3, seconds);
  TouchLED2.setColor(blue);
  wait(0.5, seconds);
}


int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  // register event handlers
  Bumper1.pressed(onevent_Bumper1_pressed_0);
  TouchLED1.pressed(onevent_TouchLED1_pressed_0);
  TouchLED3.pressed(onevent_TouchLED3_pressed_0);
  TouchLED2.pressed(onevent_TouchLED2_pressed_0);

  wait(15, msec);
  whenStarted1();
}