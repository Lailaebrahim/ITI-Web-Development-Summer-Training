from clases import *
from utils import *


def app():
    u = User.load()
    p = Project.load()
    print("Welcome to Crowdfunding!")
    while (1):
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        # Register
        if choice == '1':
            try:
                fname = input('Enter your First Name: ')
                ValidateFname(fname)

                lname = input('Enter your Last Name: ')
                ValidateLname(lname)

                email = input('Enter your Email: ')
                ValidateEmail(email)

                password = input('Enter your Password: ')
                confirmPassword = input('Confirm your Password: ')
                ValidatePassword(password, confirmPassword)

                mobilePhone = input('Enter your Mobile Phone: ')
                ValidateMobilePhone(mobilePhone)

                user = User(fname, lname, email, password, mobilePhone)
                user.Regestiration()
                print('User registered successfully!')
                print('==============================================================')
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        # Log IN
        elif choice == '2':
            try:
                trails = 2
                for i in range(2):
                    try:
                        email = input('Enter your Email: ')
                        password = input('Enter your Password: ')
                        current_user = User.LogIn(email, password)
                        print('User logged in successfully!')
                        print(
                            '==============================================================')
                        break
                    except ValueError as e:
                        trails -= 1
                        print(e)
                        print(f'Please try again you have {1-i} left')
                    except Exception as e:
                        trails -= 1
                        print(e)
                        print(f'Please try again you have {1-i} left')
                if trails == 0:
                    print('You have exceeded the number of trials, Bye!')
                    break

                while (1):
                    # Operations user can do after login in
                    print('1. Add New Project')
                    print('2. View Projects')
                    print('3. Edit A Project')
                    print('4. Delete A Project')
                    print('5. Log Out')
                    choice2 = input('Enter your choice: ')
                    if choice2 == '1':
                        try:
                            title = input('Enter Project Title: ')
                            details = input('Enter Project Details: ')
                            TotalTarget = input('Enter Total Target: ')
                            StartDate = input('Enter Start Date: ')
                            ValidateDate(StartDate)
                            EndDate = input('Enter End Date: ')
                            ValidateDate(EndDate)
                            ValidateStartAndEnd(StartDate, EndDate)

                            project = Project(
                                title, details, TotalTarget, StartDate, EndDate, current_user.getEmail())
                            created_project = project.add_project()
                            print(f'Project Created Successfully!!')
                            print(
                                    '==============================================================')
                        except ValueError as e:
                            print(e)
                        except Exception as e:
                            print(e)
                    elif choice2 == '2':
                        projects = Project.get_projects(
                            current_user.getEmail())
                        for project in projects:
                            print(project)
                            print(
                                '==============================================================')
                    elif choice2 == '3':
                        id=input('Enter Id of Project: ')
                        if Project.checkId(id):
                            item = input(
                                'Choose What to edit\n1. Title\n2. Details\n3. Total Target\n4. Start Date\n5. End Date\n6. Exit\n')
                            edit_project = Project.edit_project(id, item)
                            print(f'Project Edited Successfully!')
                            print(
                                '==============================================================')
                        else:
                            print('Project not found')
                    elif choice2 == '4':
                        id = input('Enter Id of Project: ')
                        if Project.checkId(id):
                            Project.delete_project(id)
                            print(f'Project Deleted Successfully!')
                            print(
                                '==============================================================')
                        else:
                            print('Project not found')
                    elif choice2 == '5':
                        print('Bye See you soon')
                        break

            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)

        # Exit
        elif choice == '3':
            print('Bye See you soon')
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")
    User.save()
    Project.save()


if __name__ == '__main__':
    app()
