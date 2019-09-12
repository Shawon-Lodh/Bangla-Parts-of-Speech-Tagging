import csv


class RootFind:
    def __init__(self):
        pass

    def rootFinding(self):
        try:

            suffix_dict = {}
            reference_root_dict = {}
            input_data = open("input.txt", "r")

            k = 0
            with open('result.csv', 'r') as csvfile:
                rooted_data1 = csv.reader(csvfile)
                for data in rooted_data1:
                    if (data[1].strip() is "\n") or (data[0].strip() is "\n") or (data[1].strip() is "") or (data[0].strip() is "") or (suffix_dict.get(data[1].strip()) is not None):
                        continue
                    else:
                        suffix_dict.update({data[1].strip(): data[0].strip()})
                        k += 1
            print(k)

            sz = -1
            with open('reference_root_words.csv', 'r') as rooted_data2:
                rooted_data2 = csv.reader(rooted_data2)
                for data in rooted_data2:
                    sz += 1
                    reference_root_dict.update({data[2]: data[1]})

            with open('reference_root_words.csv', 'a', newline='') as csvfile:
                final_result = csv.writer(csvfile)
                for data in input_data:
                    word = data.split()
                    for i in range(len(word)):
                        pos = ''
                        if reference_root_dict.get(word[i]) is not None:
                            print(word[i] + " 1 " + reference_root_dict.get(word[i]))
                            flag = 1
                            continue
                        else:
                            flag = 0
                            for j in range(len(word[i])):
                                if suffix_dict.get(word[i][j:]) is not None:
                                    print(word[i] + " " + suffix_dict.get(word[i][j:]))
                                    final_result.writerow([sz, word[i], suffix_dict.get(word[i][j:])])
                                    sz += 1
                                    flag = 1
                                    break
                            if flag is 0:
                                print(word[i] + "is unknown")

                    # for i in range(len(data)):
                    #     for j in range(i, len(data)):
                    #         sz = j - i
                    #         if sz < 4:
                    #             continue
                    #         if data[i:j] in rooted_dict:
                    #             pos = rooted_dict.get(data[i:j])
                    #             index = j
                    #             i = j
                    #             break
                    # if index is not -1:
                    #     rooted_word_result.writerow([data, data[:index], pos, data[index:]])
                    #     index = -1
                    # else:
                    #     rooted_word_result.writerow([data, data, pos, data[index:]])
                    #     index = -1

        except Exception as msg:
            print("From Root Find in rootFinding Method: " + str(msg))


def main():
    try:
        root_finding = RootFind()

        '''rootFinding method need two file one is input file which contains row words and second file is reference rooted words file'''

        root_finding.rootFinding()
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main()
