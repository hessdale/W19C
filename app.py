# import input handler to take inputs from user
import input_handler
# import random to generate random nums
import random
# defining game function with health arguements
def game(user_health,cpu_health):
    # returned strings from input handler
    user_attack=input_handler.get_attack()
    user_defence=input_handler.get_defence()
    # random numbers generated from 0 - 100 for cpu
    cpu_attack= random.randint(0,100)
    cpu_defence= random.randint(0,100)
    # if statements that have all the out comes of the battle
    if (user_attack == 1 and cpu_defence >= 50):
        cpu_health=cpu_health - 10
        print('you hit the cpu!')
        print('cpu hp:')
        print(cpu_health)
    elif(user_attack == 1 and cpu_defence < 50):
        print('cpu attack blocked')
    elif(user_attack == 2 and cpu_defence >= 50):
        print('cpu attack blocked')
    elif(user_attack == 2 and cpu_defence < 50):
        cpu_health=cpu_health - 10
        print('you hit the cpu!')
        print('cpu hp:')
        print(cpu_health)
    if (cpu_attack < 50 and user_defence ==2):
        user_health=user_health - 10
        print('your hp:')
        print(user_health)
    elif (cpu_attack < 50 and user_defence == 1):
        print('you blocked the attack')
    elif (cpu_attack >= 50 and user_defence == 2):
        print('you blocked the attack')
    elif (cpu_attack >= 50 and user_defence == 1):
        user_health=user_health - 10
        print('your hp:')
        print(user_health)
    # if statement at end of fight to check health and if its above 0 then it re runs the function with health as arguements
    if(cpu_health > 0 and user_health > 0):
        game(cpu_health,user_health)
    elif(cpu_health <= 0):
        print('you have won!')
    elif(user_health <= 0):
        print('you have lost!')
# starting the game with players health at 100
game(100,100)