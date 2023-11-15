import _test_func,time

url = "http://127.0.0.1:8000/api/image/"



for i in range(1,30):
    _test_func.test_status(url+"gen_identicon/"+str(i),200)
    print("Tested /image/gen_identicon/"+str(i)+" successfully")
print("\n"+"="*40+"\nTested /image/gen_identicon/* successfully\n"+"="*40)


_test_func.test_status(url+"gen_image",200)
print("Tested /image/gen_image successfully")

print("\n"+"="*40+"\nTested /image/* successfully\n"+"="*40+"\n")