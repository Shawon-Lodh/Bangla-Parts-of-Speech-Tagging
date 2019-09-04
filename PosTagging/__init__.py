import csv


def main():
    rooted_dict = {}
    input_data = open("input.txt", "r")

    with open('reference_root_words.csv', 'r') as rooted_data:
        rooted_data = csv.reader(rooted_data)
        with open("new_reference_root_words.csv", "w+", newline='') as new_rooted_data:
            new_rooted_data = csv.writer(new_rooted_data)
            new_rooted_data.writerow(['SL.', 'Root', 'Parts of speech'])
            for data in rooted_data:
                if len(data[2]) >= 2:
                    new_rooted_data.writerow(data)
                # rooted_dict.update({data[2]: data[1]})
    # for data in rooted_dict:
    #     print(data[0])
    # with open("reference_root_words.csv", 'r') as csvfile:
    #     rooted_data = csv.reader(csvfile)
    #
    #     with open('suffix.csv', 'w+', newline='') as csvfile:
    #         suffix_result = csv.writer(csvfile)
    #         suffix_result.writerow(['Suffix', 'Parts of speech'])
    #
    #         with open('result.csv', 'w+', newline='') as csvfile:
    #             rooted_word_result = csv.writer(csvfile)
    #             rooted_word_result.writerow(['Root Word', 'Parts of speech'])
    #
    #             for data1 in input_data:
    #                 flag = 0
    #                 for data2 in rooted_data:
    #                     ln1 = len(data1)
    #                     ln2 = len(data2[2])
    #                     mn = min(ln1, ln2)
    #                     str1 = data1[0: mn - 1]
    #                     str2 = data2[2]
    #                     str2 = str2[0: mn - 1]
    #
    #                     if str1 is str2:
    #                         print(str1)
    #                         rooted_word_result.writerow([str1, data2[1]])
    #                         flag = 1
    #                         if ln1 == mn and ln2 != mn:
    #                             suffix_result.writerow([str2[mn: ln2], data2[1]])
    #                         elif ln2 == mn and ln1 != mn:
    #                             suffix_result.writerow([str1[mn: ln1], data2[1]])
    #
    #                 if flag == 0:
    #                     with open("suffix.csv", 'r') as suffix_data:
    #                         suffix_data = csv.reader(suffix_data)
    #                         for data3 in suffix_data:
    #                             ln3 = len(data1) - len(data3[0])
    #                             str3 = data1
    #                             str2 = str3[ln3 - 1:]
    #                             if str2 == data3[0]:
    #                                 with open('reference_root_words.csv', 'w+', newline='') as csvfile:
    #                                     new_word = csv.writer(csvfile)
    #                                     new_word.writerow([data1, data3[1]])
    #                 else:
    #                     print(data1 + "is unknown")


if __name__ == "__main__":
    main()
