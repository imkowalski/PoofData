import _test_func

url = "http://127.0.0.1:8000/api/user/"



for i in range(1,30):
    _test_func.test_status(url+"profile?seed="+str(i),200)
    print("Tested /user/profile?seed="+str(i)+" successfully")
print("\n"+"="*40+"\nTested /user/profile?seed=* successfully\n"+"="*40)

print("\n"+"="*40+"\nTested /user/* successfully\n"+"="*40+"\n")