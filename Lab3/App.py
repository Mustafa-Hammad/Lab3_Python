import AUT.log as log
import AUT.Rig as rig

while True:
    print('> Crowd Funding Application')
    print('> Registration - Press (1)')
    print('> Login - Press (2)')
    print('> Exit - Press (3)')
    inputReader = int(input('> Your Choice: '))
    if inputReader == 1:
        while True:
            rig.register()
            break
    elif inputReader == 2:
        print('> USER LOGIN')
        while True:
            log.login()
    elif inputReader == 3:
        break
    else:
        print('> Sorry, Enter Valid Input\n')
