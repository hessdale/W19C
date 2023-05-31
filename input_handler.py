# functon that tries to get attack input from user and returns errors and restarts the function
def get_attack():
    print('Punch:1 Kick:2')
    try:
        attack=input('enter attack: ')
        return(int(attack))
    except ValueError:
        print('please enter number 1-2')
        get_attack()
    except TypeError:
        print('only select 1-2')
        get_attack()
    except:
        print('something went wrong')
        get_attack()
# functon that tries to get defence input from user and returns errors and restarts the function
def get_defence():
    print('High:1 Low:2')
    try:
        defence=input('enter defence: ')
        return(int(defence))
    except ValueError:
        print('please enter number 1-2')
        get_defence()
    except TypeError:
        print('only select 1-2')
        get_defence()
    except:
        print('something went wrong')
        get_defence()