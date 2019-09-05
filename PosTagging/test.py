import csv


class SuffixFilter:
    def __init__(self):
        pass

    def suffixFinding(self, predefined_root_word):
        try:

            ref_rooted_word = []
            ref_rooted_pos = []
            with open('reference_root_words.csv', 'r') as rooted_data:
                rooted_data = csv.reader(rooted_data)
                for word in rooted_data:
                    ref_rooted_word.append(word[2])
                    ref_rooted_pos.append(word[1])

            first_suffix_word = []
            first_suffix_pos = []
            with open('result.csv', 'r') as rooted_data:
                rooted_data = csv.reader(rooted_data)
                for word in rooted_data:
                    first_suffix_word.append(word[3])
                    first_suffix_pos.append(word[2])

            index = -1
            k = 0
            with open('suffix_filter_result.csv', 'w+', newline='') as csvfile:
                suffix_word_result = csv.writer(csvfile)
                suffix_word_result.writerow(['Parts Of Speech', 'Suffix'])
                for word1 in first_suffix_word:
                    if len(word1) < 3:
                        continue
                    for i in range(len(word1)):
                        for j in range(i, len(word1)):
                            sz = j - i
                            if sz < 4:
                                continue
                            if word1[i:j] in ref_rooted_word:
                                # print(word1)
                                index = j
                                break
                    if index > -1:
                        suffix_word_result.writerow([word1[index:], first_suffix_pos[k]])
                        index = -1
                    k = k + 1


        except Exception as msg:
            print("From Root Find in rootFinding Method: " + str(msg))


def main():
    try:
        root_finding = SuffixFilter()

        '''rootFinding method need two file one is input file which contains row words and second file is reference rooted words file'''

        root_finding.suffixFinding("result")
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main()
