# -*- coding: UTF-8 -*-
#travel rest hunt status

#import
import random
import time
#import smtplib send email import

#Welcome player
asker1 = input('Welcome to the game Oregon Trail - would you like to learn more? (y/n) ')
if asker1 == "y":
    print('''
    This game is all about surviving the Oregon Trail.\n It will be a long, strenous journy, but lot of people made it
    back in the long ago. Let us begin the trip.
    ''')
#asking name
player_name = input('What is your name?')
while len(player_name) >= 0:
  if len(player_name) > 1:
    print(str(player_name)+"? It is a good name.")
    break
  if len(player_name) == 1:
    player_name_choice = input(str(player_name)+"? Are you kidding me? Only one letter?(y/n): ")
    if player_name_choice == "y" or player_name_choice == "Y":
      print("Ok...")
      break
    if player_name_choice == "n" or player_name_choice == "N":
      player_name = input('What is your name? ')
  else:
    print("You do not type anything, try again")
    player_name = input('What is your name? ')

#easter eggs for name
if player_name == 'Meriwether Lewis':
  year_set = 1803
  mode_choice = 'impossible'
else:
  year_set = input('Enter a year, whatever you like: ')
  if year_set.isdigit():
    return_num = 0
  else:
    return_num = 1
  while return_num == 1:
    print('Error, please try again!')
    year_set = input('Enter a year whatever you like: ')
    if year_set.isdigit():
      return_num = 0
    else:
      return_num = 1
  year_set = int(year_set)
  print('Which mode do you want to play?')
  mode_choice = input('(easy,normal,hard,impossible,customize):')

#leap year function
#go to [https://github.com/yoshino-lin/Oregon-Trail] to support me!
'''
if (year_set % 4) == 0:
   if (year_set % 100) == 0:
       if (year_set % 400) == 0:
           print('leap year')
       else:
           print('no leap year')
   else:
       print('Leap year')
else:
   print('No leap year')
'''

while len(mode_choice) >= 0: 
#easy mode:
  if mode_choice == 'easy':
    food_num = 1000
    health_num = 10
    break
#noraml mode:
  elif mode_choice == 'normal':
    food_num = 500
    health_num = 5
    break
#hard mode:
  elif mode_choice == 'hard':
    food_num = 300
    health_num = 4
    break
#impossible mode:
  elif mode_choice == 'impossible':
    food_num = 150
    health_num = 3
    break
#customize mode:
  elif mode_choice == 'customize':
    #food number take in
    food_num = input('How much food do you want:')
    if food_num.isdigit():
      return_cm_num = 0
    else:
      return_cm_num = 1
    while return_cm_num == 1:
      print('Error ,please try again!')
      food_num = input('How much food do you want:')
      if food_num.isdigit():
        return_cm_num = 0
      else:
        return_cn_num = 1
    food_num = int(food_num)
    #health number take in
    health_num = input('How much health do you want:')
    if health_num.isdigit():
      return_cm_num2 = 0
    else:
      return_cm_num2 = 1
    while return_cm_num2 == 1:
      print('Erro,please try again!')
      health_num = input('How much health do you want:')
      if health_num.isdigit():
        return_cm_num2 = 0
      else:
        return_cn_num2 = 1
    health_num = int(health_num)
    break
#erro?
  else:
    print("Bad input, try again!")
    mode_choice = input('(easy,normal,hard,impossible,customize):')
    

#other basic strating value setting
player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
health_d1 = random.randint(1, 31)
health_d2 = random.randint(1, 31)
acident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0
month_appear = 'March'

#add days:
def add_days(min, max):
  global days_pass
  global month_num
  global MONTHS_WITH_31_DAYS
  global random_result
  global food_num
  global health_num
  global health_d1
  global health_d2
  global total_days
  global acident_appear

  random_result = random.randint(min, max)
  print('Now',random_result,"days passed..")
  days_pass_min = days_pass
  check_big = days_pass + random_result

  #acident
  if acident_appear >= days_pass and acident_appear <= check_big:
    a_number = random.randint(1, 3)
    a_health_num = random.randint(1, 2)
    if a_number == 1:
        print('During this time, you crossed a river.')
    if a_number == 2:
        print('During this time, you had dysentery.')
#    if a_number == 3:
#        print('You met some Indians, and they helped you find '+str(random_result2_food)+' food')
    if a_number == 3:
        print('One of your oxen was injured, and you spent '+str(random_result2_day)+'s trying to fix it.')
    random_result2_food = random.randint(1, 10)
    random_result2_day = random.randint(1, 10)
    print('As a result, you ate '+str(random_result2_food)+' lbs extra food.')
    print('It also took up an extra '+str(random_result2_day)+' days.')
    if a_health_num == 1:
      print('And you also lose 1 health')
      health_num -= 1
    food_num = food_num - random_result2_food - random_result2_day*5
    days_pass += random_result2_day
    total_days += random_result2_day
  #health decrease randomly  
  check_big = days_pass + random_result
  if health_d1 >= days_pass_min and health_d1 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')
  if health_d2 >= days_pass_min and health_d2 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')


  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5

  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)

#function part
def travle1(movedistance):
  global days_pass
  global travel_total_num
  add_days(3,7)
  movedistance = movedistance + random.randint(30, 60)
  travel_total_num += 1
  return movedistance

def rest(health):
  global days_pass
  global rest_total_num
  add_days(2,5)
  health = health + 1
  rest_total_num += 1
  return health

def hunt(hunting_food):
  global days_pass
  global hunt_total_num
  add_days(2,5)
  hunting_food = hunting_food + 100
  print('Gain: 100 lbs food')
  hunt_total_num += 1
  return hunting_food

#month_appear
def month_appear_fun():
  global month_appear
  if month_num == 1:
    month_appear = 'January'
  elif month_num == 2:
    month_appear = 'February'
  elif month_num == 3:
    month_appear = 'March'
  elif month_num == 4:
    month_appear = 'April'
  elif month_num == 5:
    month_appear = 'May'
  elif month_num == 6:
    month_appear = 'June'
  elif month_num == 7:
    month_appear = 'July'
  elif month_num == 8:
    month_appear = 'August'
  elif month_num == 9:
    month_appear = 'September'
  elif month_num == 10:
    month_appear = 'October'
  elif month_num == 11:
    month_appear = 'November'
  elif month_num == 12:
    month_appear = 'December'
  return month_appear

#loading part
print('--------------------------------------')
print('Now Loding...')
time.sleep(0.5)
print('Now loading the player settings...')
time.sleep(2)
print('Successfull!')
time.sleep(0.5)
print('Now loading the game settings...')
time.sleep(2)
print('Successfull!')
time.sleep(0.5)
print('Prepearing the trip for Oregon...')
time.sleep(2)
print('Successfull!')
time.sleep(0.5)
print('Game Ready!')
print('--------------------------------------')
print('Attention:')
print('We will be recreating Oregon Trail! The goal is to travel from NYC to')
print('Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each')
print('day costs you food and health. You can huntand rest, but you have to')
print('get there before winter. GOOD LUCK!')
print('--------------------------------------')

#main
while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
  month_appear_fun()
  if food_num <= 50:
    print('Warning! You only have '+ str(food_num) + " lbs food now.")
    print('You need hunt now.')
  if health_num <= 2:
    print('Warning! You only have '+ str(health_num) + " health now.")
    print('You need a rest.')
  print(str(player_name) + ', now it is ' + month_appear + ' '+str(days_pass) + ', ' + str(year_set) + ", and you have travled " + str(player_move_distance) + " miles.")
  choice = input('Your choice:')
  if choice == 'travel':
    player_move_distance = travle1(player_move_distance)
  elif choice == 'rest':
    if health_num < 5:
      print("You get 1 heath!")
      health_num = rest(health_num)
    if health_num >= 5:
      print("Your health is full, the maximum number for health is 5!")
  elif choice == 'hunt':
    food_num = hunt(food_num)
  elif choice == 'status':
    print('-Dear ' + str(player_name) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+".")
    print('-Food:',food_num,"lbs")
    print('-Health:',health_num)
    print('-Distance traveled:',player_move_distance)
    distance_left = 2000 - player_move_distance
    print('-'+str(total_days) +' days have passed.')
    print('-You have travled ' + str(player_move_distance) + " miles, there is still " + str(distance_left) + ' miles left.')
    status_total_num += 1
  elif choice == 'help':
    print('[travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).')
    print('[rest]: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).')
    print('[hunt]: adds 100 lbs of food and takes 2-5 days (random).')
    print('[status]: lists food, health, distance traveled, and day.')
    print('[quit]: will end the game.')
  elif choice == 'quit':
    quit_choice = input('Are you sure that you want to quit?(y/n)')
    if quit_choice == 'y':
      print('Game over...I cannot believe that you quit...')
      break
  elif choice == 'suicide':
    quit_choice2 = input('Are you sure?(y/n)')
    if quit_choice2 == 'y':
      print('Game over...You kill youslf...')
      break
  elif choice == 'easter egg':
      print("ok")
    else:
    print("This Choice is not available, please try again.")
  print('--------------------------------------')
#succeed!
if player_move_distance >= 2000:
  print('Nice job! you have arrived in Oregon')

#game over
if food_num <= 0:
  print('Game over, you have no food now.')

if health_num <= 0:
  print('Game over, you have no health now.')

if month_num >= 13:
  print('Game over, you run out of time!')
  
print('During the whole game, you:')
print('Travel ' + str(travel_total_num) +' times.')
print('Rest ' + str(rest_total_num) +' times.')
print('Hunt ' + str(hunt_total_num) +' times.')
print('Status ' + str(status_total_num) +' times.')

#restart
#restart_choice = input('Do you want to restart the game?')

def bot():
    player_name = "Benny the Bot"
    mode_choice = "impossible"


