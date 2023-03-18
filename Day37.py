def func(x):
    try:
        l = [2,4,6,7]
        print(l[x])
        return 1
    except:
        print("Error Occured.")
        return 0
    finally:
        print("Always Executed.")

func(3)