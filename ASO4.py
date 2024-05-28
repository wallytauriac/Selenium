from Selenium.test_selectToCart import TestSelectToCart
from Selenium.test_selectToCart2 import TestSelectToCart2
import time

# Test Case 1
print("**************** Test Case 1 Results ******************************")
# Store start time
t = time.time()
obj = TestSelectToCart()
obj.setup_method("setup")
log = obj.test_our_products()
if len(log) > 0:
    for entry in log:
        print("Log entry: ", entry)

obj.teardown_method("shutdown")
# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")

# Category images "speakersImg, laptopsImg, tabletsImg"
ctgy = ["speakersImg", "laptopsImg", "tabletsImg"]
# Brand values "Bose=manufacturer_0, HP=manufacturer_1, Logitech=manufacturer_2"
brnd = ["manufacturer_0", "manufacturer_1", "manufacturer_2"]
display = ["display_0", "display_1"]
# Test Case 2
print("**************** Test Case 2 Results ******************************")
# Store start time
t = time.time()
obj = TestSelectToCart2()
obj.setup_method("setup")
log = obj.test_our_products(ctgy[0], brnd[0], display[0])
if len(log) > 0:
    for entry in log:
        print("Log entry: ", entry)

# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")
# Test Case 3
print("**************** Test Case 3 Results ******************************")
# Store start time
t = time.time()
obj = TestSelectToCart2()
obj.setup_method("setup")
log = obj.test_our_products(ctgy[1], "", display[0])
if len(log) > 0:
    for entry in log:
        print("Log entry: ", entry)

# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")

obj.teardown_method("shutdown")

if __name__ == "__main__":
    print("Bye")