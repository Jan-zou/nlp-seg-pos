# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jinglin Zou

import codecs
import os


def get_tagged_data(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for line in input_data.readlines():
        wlist = line.strip().split()
        for word in wlist:
            w, tag = word.split('/')
            output_data.write(w + '\t' + tag + '\n')
        output_data.write('\n')

    input_data.close()
    output_data.close()


def crf_segmenter(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    doc_list = input_data.readlines()

    for line in doc_list:
        if line == '\n':
            output_data.write('\n')
        else:
            line = line.strip().split('\t')
            word = line[0]
            tag = line[-1]
            output_data.write(word + '/' + tag + ' ')

    input_data.close()
    output_data.close()


if __name__ == '__main__':
    get_tagged_data('data/pos_train.txt', 'result/pos/train_pos.data')
    get_tagged_data('data/pos_test.txt', 'result/pos/test_pos.data')
    os.chdir('result/pos/')
    os.system('../../CRF++-0.58/crf_learn -f 3 -c 4.0 template train_pos.data model')
    os.system('../../CRF++-0.58/crf_test -m model test_pos.data > output.txt')
    crf_segmenter('output.txt', 'result.txt')
