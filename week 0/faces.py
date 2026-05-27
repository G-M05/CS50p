def convert(text):
    text = text.replace(":(", "🙁").replace(":)", "🙂")
    return text


def main():
    text = input("what is an emoticon you would like to convert? ")

    print(convert(text))


main()