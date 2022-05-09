try:
    # Open a file in write-mode
    f = open("myfile.txt", 'r')
    f.write("Hello World!")
except IOError as e:
    print("An error occurred:", e)
finally:
    try:
        print("Closing the file now")
        f.close()
    except NameError as ne:
        print("An error occurred:", ne)