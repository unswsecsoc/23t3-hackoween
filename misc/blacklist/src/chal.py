while 1:
    try:
        print("Enter code to evaluate:")
        code = input("> ")

        blacklist = ["import", "open", "system", "eval", "exec"]

        for bw in blacklist:
            if bw in code.lower():
                print(f"ERROR! the word {bw} is not allowed!")
                exit()

        result = eval(code)
        print(f"The result is {result}")
    except Exception as e:
        print("An unexpected error occurred!")
        print(e)
