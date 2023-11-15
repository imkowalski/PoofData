import _test_func,time

url = "http://127.0.0.1:8000/api/object/"



for i in range(1,30):
    _test_func.test_status(url+"post?seed="+str(i),200)
    print("Tested /object/post?seed="+str(i)+" successfully")

print("\n"+"="*40+"\nTested /object/post successfully\n"+"="*40)
print("Waiting 60 seconds for the server for the limiter to reset")
time.sleep(60)

for i in range(1,30):
    _test_func.test_status(url+"comment?seed="+str(i),200)
    print("Tested /object/post?seed="+str(i)+" successfully")


print("\n"+"="*40+"\nTested /object/comment successfully\n"+"="*40)

print("\n"+"="*40+"\nTested /object/* successfully\n"+"="*40+"\n")