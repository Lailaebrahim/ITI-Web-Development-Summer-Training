from utils import *
import uuid
import ast


class User():
    Users = {}

    def __init__(self, fname, lname, email, password, mobilePhone):
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__password = password
        self.__mobilePhone = mobilePhone

    def Regestiration(self):
        if self.__email in User.Users:
            raise ValueError('User already exists')
        else:
            User.Users[self.__email] = User.from_dict(self.__email, {
                'fname': self.__fname,
                'lname': self.__lname,
                'password': self.__password,
                'mobilePhone': self.__mobilePhone
            })

    @classmethod
    def LogIn(cls, email, password):
        if email in cls.Users:
            if cls.Users[email].getPassword() == password:
                return cls.Users[email]
            else:
                raise ValueError('Invalid Password')
        else:
            raise ValueError('Invalid Email')
        
    @classmethod
    def save(cls):
        for email, user in cls.Users.items():
            with open('D:/_Laila_Place/ITI_Summer_Training_2024_Web_Dev_Python/Day10/Crowdfunding/users.txt', 'w') as file:
                file.write(str(user)+"\n")

    @classmethod
    def load(cls):
        cls.Users = {}
        with open('D:/_Laila_Place/ITI_Summer_Training_2024_Web_Dev_Python/Day10/Crowdfunding/users.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                return {}
            for line in lines:
                line = line.strip()
                email, user_data = line.split(': ', 1)
                user_data = ast.literal_eval(user_data)
                cls.Users[email] = cls.from_dict(email, user_data)
        return cls.Users

    @classmethod
    def from_dict(cls, email, data):
        return cls(
            fname=data['fname'],
            lname=data['lname'],
            email=email,
            password=data['password'],
            mobilePhone=data['mobilePhone']
        )

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def __str__(self):
        return str(self.__email) + ': {' + \
            "'fname': '" + str(self.__fname) + "'," + \
            "'lname': '" + str(self.__lname) + "'," + \
            "'password': '" + str(self.__password) + "'," + \
            "'mobilePhone': '" + str(self.__mobilePhone) + \
            "'}"


class Project():
    Projects = {}

    def __init__(self, title, details, TotalTarget, StartDate, EndDate, UserEmail, id=None):
        self.__id = id or uuid.uuid4()
        self.__title = title
        self.__details = details
        self.__TotalTarget = TotalTarget
        self.__StartDate = StartDate
        self.__EndDate = EndDate
        self.__UserEmail = UserEmail

    def add_project(self):
        if self.__id in Project.Projects:
            raise ValueError('Project already exists')
        else:
            Project.Projects[self.__id] = Project.from_dict(self.__id, {
                'UserEmail': self.__UserEmail,
                'title': self.__title,
                'details': self.__details,
                'TotalTarget': self.__TotalTarget,
                'StartDate': self.__StartDate,
                'EndDate': self.__EndDate
            })
    
    @classmethod
    def save(cls):
        with open('D:/_Laila_Place/ITI_Summer_Training_2024_Web_Dev_Python/Day10/Crowdfunding/projects.txt', 'w') as file:
            for project_id, project in cls.Projects.items():
                file.write(str(project) + "\n")
    
    @classmethod
    def load(cls):
        cls.Projects = {}
        with open('D:/_Laila_Place/ITI_Summer_Training_2024_Web_Dev_Python/Day10/Crowdfunding/projects.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                return {}
            for line in lines:
                line = line.strip()
                project_id, project_data = line.split(': ', 1)
                project_data = ast.literal_eval(project_data)
                cls.Projects[project_id] = cls.from_dict(
                    project_id, project_data)
        return cls.Projects

    @classmethod
    def from_dict(cls, project_id, project_data):
        return cls(
            title=project_data['title'],
            details=project_data['details'],
            id=project_id,
            TotalTarget=project_data['TotalTarget'],
            StartDate=project_data['StartDate'],
            EndDate=project_data['EndDate'],
            UserEmail=project_data['UserEmail']
        )

    @classmethod
    def get_projects(cls, UserEmail):
        projects = []
        for project_id, project in cls.Projects.items():
            if project.getUser() == UserEmail:
                projects.append(project)
        return projects
    
    @classmethod
    def edit_project(cls, id, item):
        project=Project.Projects[id]
        if item=='1':
            title = input('Enter Project Title: ')
            project.__title=title
        elif item=='2':
            details = input('Enter Project Details: ')
            project.__details=details
        elif item=='3':
            TotalTarget = input('Enter Total Target: ')
            project.__TotalTarget=TotalTarget
        elif item=='4':
            StartDate = input('Enter Start Date: ')
            ValidateDate(StartDate)
            project.__StartDate=StartDate
        elif item=='5':
            EndDate = input('Enter End Date: ')
            ValidateDate(EndDate)
            ValidateStartAndEnd(project.__StartDate, EndDate)
            project.__EndDate=EndDate
        else:
            raise ValueError('Invalid Choice!')
        
    @classmethod
    def delete_project(cls, id):
        if id in cls.Projects:
            del cls.Projects[id]
        else:
            raise ValueError('Project not found')
        
    @classmethod
    def checkId(cls, id):
        if id in cls.Projects:
            return True
        else:
            return False

    def getId(self):
        return self.__id

    def getUser(self):
        return self.__UserEmail

    def __str__(self):
        return str(self.__id) + ": {" + \
            "'title': '" + str(self.__title) + "'," + \
            "'details': '" + str(self.__details) + "'," + \
            "'TotalTarget': '" + str(self.__TotalTarget) + "'," + \
            "'StartDate': '" + str(self.__StartDate) + "'," + \
            "'EndDate': '" + str(self.__EndDate) + "'," + \
            "'UserEmail': '" + str(self.__UserEmail) + \
            "'}"
