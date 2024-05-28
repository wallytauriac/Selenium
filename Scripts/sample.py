import time

start = time.time()
time.sleep(3)
end = time.time()
print(f"{(end - start):.1f} seconds")

elapsed = end - start
elapsed = f"{elapsed:.1f} seconds"
print(elapsed)

if __name__ == "__main__":
    print("Bye")