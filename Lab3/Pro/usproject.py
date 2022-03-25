import datetime
import re

import Pro.project as pro

def us(Mail):
    while True:
        print('> Create Project - press (1)')
        print('> Delete Project - Press (2)')
        print('> Update Project - press (3)')
        print('> View All Projects - press (4)')
        print('> View by date Projects - press (5)')
        print('> Exit - press (6)')
        userChoice = int(input('> your choice: '))
        if userChoice == 1:
            regex = "%d-%m-%Y"
            title = input('> project title: ')
            details = input('> project details: ')
            total = int(input('> project total target: '))
            while True:
                startDate = input('> project start date: ')
                if datetime.datetime.strptime(startDate, '%d-%m-%Y'):
                    break
                else:
                    continue
            while True:
                endDate = input('> project end data: ')
                if datetime.datetime.strptime(endDate, '%d-%m-%Y'):
                    break
                else:
                    continue
            projectStatus = pro.Project.createProject( Mail, title, details, total, startDate, endDate)
            if projectStatus:
                print('> Project Created Successfully...')
            else:
                print('> Sorry Project Creation Failed...')
        elif userChoice == 2:
            title = input('> enter project title: ')
            status = pro.Project.deleteOneProject(Mail, title)
            if status:
                print('> Project Deleted Successfully...')
            else:
                print('> Project Deletion Failed...')
        elif userChoice == 3:
            title = input('> enter project title: ')
            status = pro.Project.update(Mail, title)
            if status:
                print(status)
                print('> Project Updated Successfully...')
            else:
                print(status)
                print('> Project Update Failed...')
        elif userChoice == 4:
            pro.Project.findAllProject(Mail)
        elif userChoice == 5:
            print('>  Project start date - press (1)')
            print('>  Project end date - Press (2)')
            userChoice2 = int(input('> your choice: '))
            if userChoice2 == 1:
                date = input('> enter project start date: ')
                pro.Project.findstartProject(Mail,date)
            elif userChoice2 == 2:
                date = input('> enter project end date: ')
                pro.Project.findendProject(Mail,date)
            else:
                print('> Sorry, Enter Valid Input\n')
        elif userChoice == 6:
            exit()
        else:
            print('> Sorry, Enter Valid Input\n')