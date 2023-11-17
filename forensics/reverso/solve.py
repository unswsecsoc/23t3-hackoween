if __name__ == "__main__":
    with open("thing.txt", "rb") as file:
        with open("result.png", "wb") as result:
            result.write(file.read()[::-1])