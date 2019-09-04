import csv


class SuffixFilter:
    def __init__(self):
        pass

    def suffixFinding(self, predefined_root_word):
        try:
            rooted_dict = {}
            input_data = []
            raw_word = []
            pos_tag = []
            '''The reference or predefined root word and parts of speech store in dictionary (rooted_dict).'''
            with open(predefined_root_word + '.csv', 'r') as rooted_data:
                rooted_data = csv.reader(rooted_data)
                for data in rooted_data:
                    rooted_dict.update({data[1]: data[2]})
                    input_data.append(data[3])
                    raw_word.append(data[0])
                    pos_tag.append(data[2])
            '''Store the result main word, root word, root word's parts of speech and the suffix'''
            index = -1
            with open('suffix_filter_result.csv', 'w+', newline='') as csvfile:
                rooted_word_result = csv.writer(csvfile)
                rooted_word_result.writerow(['Parts of speech', 'Suffix'])
                for j, word in enumerate(input_data):
                    if len(data) <= 2:
                        continue
                    for i in range(0, word.__len__(), 1):
                        # িতাপ্রতিদ্বন্দ্বিতাহীন
                        if (word[:i] in rooted_dict) or (word[i:] in rooted_dict):
                            index = i
                            print([word[:i], word[i:], rooted_dict.get(word[i:]), rooted_dict.get(word[:i])])
                    if index is -1:
                        rooted_word_result.writerow([pos_tag[j], word])
                        index = -1
        # [data, data[:index], rooted_dict[data[:index]], data[index:], '']

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
