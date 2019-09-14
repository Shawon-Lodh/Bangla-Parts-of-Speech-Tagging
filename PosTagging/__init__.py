import csv


def main():
    word = "অঙ্গীকার"
    for i in range(1, len(word)):
        print('"' + word[:i] + '"' + " + " + '"' + word[i:] + '"')

if __name__ == "__main__":
    main()
