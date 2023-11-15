import random
import csv
import os
from load_csv import name_list,surname_list,word_list

                        

def gen_name(seed):
    random.seed(seed)
    name = random.choice(name_list)
    surname = random.choice(surname_list).capitalize()
    return (name,surname)



def gen_email(seed,name):
    random.seed(seed)
    ints = ""
    if random.randint(0, 1):
        ints = str(random.randint(100, 999))
    return f"{name.lower()}{ints}@poofdata.dk"

def gen_phone(seed,length=8):
    random.seed(seed)
    return "".join([str(random.randint(0,9)) for _ in range(length)])

def gen_address(seed):
    random.seed(seed)
    pass


def gen_job(seed):
    random.seed(seed)
    jobs_list = ["Unemployed","Engineer","Doctor","Lawyer","Teacher","Nurse","Programmer","Developer","Designer","Architect","Accountant","Analyst","Assistant","Auditor","Clerk","Consultant","Contractor","Manager","Officer","Operator","Planner","Representative","Specialist","Supervisor","Technician","Writer","Artist","Musician","Actor","Athlete","Chef","Dentist","Electrician","Farmer","Firefighter","Mechanic","Police","Scientist","Soldier","Veterinarian","Waiter","Waitress","Cashier"]
    return random.choice(jobs_list)

def gen_company(seed):
    random.seed(seed)
    suffix = ["LLC","Co","Inc","Corp","Ltd","GmbH","S.A.","Group","Labs","Media","Capital","Industries","Properties","Associates","Design"]
    company_name = random.choice(word_list).capitalize()+" "+random.choice(suffix)
    return company_name


