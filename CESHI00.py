# -*- coding: utf-8 -*-

# open original file
from collections import Counter

ori_file = open('happiness_seg.txt')

#deal with line break
content = ori_file.read().replace('\n', ',')
seglist = content.split()

#recoganize the words,creat a new list
recount_word = []
for i in range(0, len(seglist) - 1):
    if (len(seglist[i]) >= 2 and len(seglist[i+1]) >=2):
        recount_word.append(seglist[i] + ' ' + seglist[i+1])

def result_output(recount_word,n):
    word_counts = Counter(recount_word)

    top_n = word_counts.most_common(n)
    print(top_n)

word = recount_word
result_output(word,10)
