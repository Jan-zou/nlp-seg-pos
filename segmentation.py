# !/usr/bin/env python
# -*- coding: utf-8 -*-
# zoujinglin

import codecs
import os


def get_tagged_data(input_file, output_file):
    # 4-tags for character tagging: B(Begin), E(End), M(Middle), S(Single)
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for line in input_data.readlines():
        wlist = line.strip().split()
        for word in wlist:
            word, _ = word.split('/')
            if len(word) == 1:
                output_data.write(word + '\tS\n')
            else:
                output_data.write(word[0] + '\tB\n')
                for w in word[1:len(word)-1]:
                    output_data.write(w + '\tM\n')
                output_data.write(word[-1] + '\tE\n')
        output_data.write('\n')

    input_data.close()
    output_data.close()


def crf_segmenter(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    doc_list = input_data.readlines()

    for line in doc_list:
        if line == '\n':    # each sentence end with \n
            output_data.write('\n')
        else:
            line = line.strip().split('\t')
            word = line[0]
            tag = line[-1]
            if tag == 'B':
                output_data.write(' ' + word)
            elif tag == 'M':
                output_data.write(word)
            elif tag == 'E':
                output_data.write(word + ' ')
            else:
                output_data.write(' ' + word + ' ')

    input_data.close()
    output_data.close()


if __name__ == '__main__':
    get_tagged_data('data/seg_train.txt', 'result/seg/train_seg.data')
    get_tagged_data('data/seg_test.txt', 'result/seg/test_seg.data')
    os.chdir('result/seg/')
    os.system('../../CRF++-0.58/crf_learn -f 3 -c 4.0 template train_seg.data model')
    os.system('../../CRF++-0.58/crf_test -m model test_seg.data > output.txt')
    crf_segmenter('output.txt', 'result.txt')

