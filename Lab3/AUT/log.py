import AUT.vm as vm
import Pro.usproject as user

def login():
    Mail = input("Enter your E-mail: ")
    mail = vm.checkmail(Mail)
    passwd = input("Enter your Password: ")

    if vm.checklogin(mail,passwd):
        user.us(Mail)
    else:
        login()
