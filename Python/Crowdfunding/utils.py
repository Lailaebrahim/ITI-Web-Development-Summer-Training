import re

def ValidateEmail(email):
    if re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
        return True
    else:
        raise ValueError('Invalid Email')
  
def ValidatePassword(password, confirmPassword):
    if len(password) > 0 and password == confirmPassword:
        return True
    else:
        raise ValueError('Invalid Password')
  
def ValidateMobilePhone(mobilePhone):
    if re.match(r'\b01[0-9]{9}\b', mobilePhone):
        return True
    else:
        raise ValueError('Invalid mobilePhone')
  
def ValidateFname(fname):
    if re.match(r'\b[A-Z][a-z]+\b', fname):
        return True
    else:
        raise ValueError('Invalid First Name')
def ValidateLname(lname):
    if re.match(r'\b[A-Z][a-z]+\b', lname):
        return True
    else:
        raise ValueError('Invalid Last Name')


def ValidateDate(Date):
    if re.match(r'\b[0-9]{2}-[0-9]{2}-[0-9]{4}\b', Date):
        return True
    else:
        raise ValueError('Invalid Date')
    
def ValidateStartAndEnd(StartDate, EndDate):
    if StartDate < EndDate:
        return True
    else:
        raise ValueError('Start date must be before end date')