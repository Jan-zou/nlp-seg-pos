# !/usr/bin/env python
# -*- coding: utf-8 -*-
# JingLin Zou

import random
import codecs
import os


def train_test_split(raw_file, train_file, test_file):
    raw_data = codecs.open(raw_file, 'r', 'utf-8')
    train_data = codecs.open(train_file, 'w', 'utf-8')
    test_data = codecs.open(test_file, 'w', 'utf-8')

    doc_list = raw_data.readlines()
    doc_list = [doc for doc in doc_list if doc!=u'\n']  # delete empty doc line
    random.shuffle(doc_list)

    # 90% train data, 10% test data
    doc_list_len = len(doc_list)
    split_point = int(doc_list_len*0.9)
    i = 0
    for line in doc_list:
        if i < split_point:
            train_data.write(line)
        else:
            test_data.write(line)
        i += 1

    raw_data.close()
    train_data.close()
    test_data.close()


if __name__ == '__main__':
    train_test_split('data/data.txt', 'data/seg_train.txt', 'data/seg_test.txt')
    train_test_split('data/data.txt', 'data/pos_train.txt', 'data/pos_test.txt')
