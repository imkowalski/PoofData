import _test_func,time

url = "http://127.0.0.1:8000/api/bulk/"



for i in range(1,30):
    _test_func.test_status(url+"posts/"+str(i),200)
    print("Tested /bulk/posts/"+str(i)+" successfully")
print("\n"+"="*40+"\nTested /bulk/posts/* successfully\n"+"="*40)

print("Waiting 60 seconds for the server for the limiter to reset")
time.sleep(60)

for i in range(1,30):
    _test_func.test_status(url+"comments/"+str(i),200)
    print("Tested /bulk/comments/"+str(i)+" successfully")
print("\n"+"="*40+"\nTested /bulk/comments/* successfully\n"+"="*40)

print("Waiting 60 seconds for the server for the limiter to reset")
time.sleep(60)

for i in range(1,30):
    _test_func.test_status(url+"images/"+str(i),200)
    print("Tested /bulk/images/"+str(i)+" successfully")
print("\n"+"="*40+"\nTested /bulk/images/* successfully\n"+"="*40)

print("\n"+"="*40+"\nTested /bulk/* successfully\n"+"="*40+"\n")