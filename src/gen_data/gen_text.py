import random
import csv


name_list = []
with open("./gen_data/static/names.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        if row != []:
            name_list.append(row[0])

surname_list = []
with open("./gen_data/static/surnames.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        if row != []:
            surname_list.append(row[0])


word_list = []
with open("./gen_data/static/word.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        word_list.append(row[0])
                        

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
    return f"{name.lower()}{ints}@poofdata.com"

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
    company_name = random.choice(word_list).capitalize() + " " + random.choice(suffix)
    return company_name


def gen_profile(seed):
    name = gen_name(seed)
    email = gen_email(seed,name[0])
    name = gen_name(seed)[0]+" "+gen_name(seed)[1]
    phone = gen_phone(seed)
    job = gen_job(seed)
    company = gen_company(seed)
    return {"name":name,"email":email,"phone":phone,"job":job,"company":company,"id":seed}