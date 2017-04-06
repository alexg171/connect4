import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin definitions
easy   = 4
medium = 5
hard   = 6
ai_diff = 14
startbtn = 15
resetbtn = 18
col1btn  = 23
col2btn  = 24
col3btn  = 25
col4btn  = 8
col5btn  = 7
col6btn  = 12
col7btn  = 16

colLed = 17 #multiple leds to one pin

# pin setup
#pull down resistor buttons must be connected to voltage and chosen pin
GPIO.setup(ai_diff, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(startbtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(resetbtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col1btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col2btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col3btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col4btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col5btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col6btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(col7btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(easy,   GPIO.OUT)
GPIO.setup(medium, GPIO.OUT)
GPIO.setup(hard,   GPIO.OUT)

# function definitions
### ai difficulty ###################################################
## Default ai difficulty is easy
ai_diff_btnst = 1
GPIO.output(easy, 1)

def aiDifficulty(channel):
        global ai_diff_btnst
        if (ai_diff_btnst ==1):   #from easy to medium
            ai_diff_btnst += 1
            GPIO.output(medium,1)
            GPIO.output(easy,0)
            ## call medium ai difficulty option
            
        elif (ai_diff_btnst ==2): #from medium to hard
            ai_diff_btnst += 1
            GPIO.output(hard,1)
            GPIO.output(medium,0)
            ## call hard ai difficulty option
            
        else:                   #from hard to easy
                ai_diff_btnst = 1
                GPIO.output(easy,1)
                GPIO.output(hard,0)
            ## call easy ai difficulty option
            
        print ("AI difficult button State:", ai_diff_btnst )
                                        
        
### start ###########################################################
# Calls start state when button is pressed
# startbtn = pin number
#GPIO.output(startbtn, 1)

def start(channel):
	# call start state
	print ("Start state called")
	
### reset ###########################################################
# Calls reset state when button is pressed
# startbtn = pin number
#GPIO.output(resetbtn, 1)

def reset(channel):
	# call reset state
	print ("Reset state called")
	
### column buttons ##################################################

def col1(channel):
	# call drop on column1
	print ("Player chooses column 1")

def col2(channel):
	# call drop on column2
	print ("Player chooses column 2")

def col3(channel):
	# call drop on column3
	print ("Player chooses column 3")

def col4(channel):
	# call drop on column4
	print ("Player chooses column 4")

def col5(channel):
	# call drop on column5
	print ("Player chooses column 5")

def col6(channel):
	# call drop on column6
	print ("Player chooses column 6")

def col7(channel):
	# call drop on column7
	print ("Player chooses column 7")
	
#####################################################################
	
# interrupt setup

GPIO.add_event_detect(ai_diff, GPIO.RISING,
                      callback=aiDifficulty, bouncetime=300)

GPIO.add_event_detect(startbtn, GPIO.RISING,
                      callback=start, bouncetime=300)

GPIO.add_event_detect(resetbtn, GPIO.RISING,
                      callback=reset, bouncetime=300)

GPIO.add_event_detect(col1btn, GPIO.RISING,
                      callback=col1, bouncetime=300)

GPIO.add_event_detect(col2btn, GPIO.RISING,
                      callback=col2, bouncetime=300)

GPIO.add_event_detect(col3btn, GPIO.RISING,
                      callback=col3, bouncetime=300)

GPIO.add_event_detect(col4btn, GPIO.RISING,
                      callback=col4, bouncetime=300)

GPIO.add_event_detect(col5btn, GPIO.RISING,
                      callback=col5, bouncetime=300)

GPIO.add_event_detect(col6btn, GPIO.RISING,
                      callback=col6, bouncetime=300)

GPIO.add_event_detect(col7btn, GPIO.RISING,
                      callback=col7, bouncetime=300)

        
while(1):
    x = 5
    
