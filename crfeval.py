#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def eval_seg():
    try:
        result_file = open('result/seg/output.txt', 'r')
        # result_file = open('result/pos/output.txt', 'r')
    except:
        print 'result file is not specified, or open failed!'
        sys.exit()

    wc_of_test = 0
    wc_of_gold = 0
    wc_of_correct = 0
    flag = True

    for l in result_file:
        if l == '\n':
            continue

        _, g, r = l.strip().split('\t')

        if r != g:
            flag = False

        if r in ('E', 'S'):
            wc_of_test += 1
            if flag:
                wc_of_correct +=1
            flag = True

        if g in ('E', 'S'):
            wc_of_gold += 1

    print 'WordCount from test result:', wc_of_test
    print 'WordCount from golden data:', wc_of_gold
    print 'WordCount of correct segs :', wc_of_correct

    # Precision
    P = wc_of_correct/float(wc_of_test)
    # Recall
    R = wc_of_correct/float(wc_of_gold)

    print 'P = %f, R = %f, F-score = %f' % (P, R, (2*P*R)/(P+R))

def eval_pos():
    try:
        result_file = open('result/pos/output.txt', 'r')
    except:
        print 'result file is not specified, or open failed!'
        sys.exit()

    wc_of_test = 0
    wc_of_gold = 0
    wc_of_correct = 0
    flag = True

    result_file = result_file.readlines()
    wc_of_test = len(result_file)

    for l in result_file:
        if l == '\n':
            continue


        _, g, r = l.strip().split('\t')

        if r == g:
            wc_of_correct +=1


    print 'WordCount from test result:', wc_of_test
    print 'WordCount of correct pos :', wc_of_correct

    # Precision
    P = wc_of_correct/float(wc_of_test)
    # Recall
    # R = wc_of_correct/float(wc_of_gold)

    # print 'P = %f, R = %f, F-score = %f' % (P, R, (2*P*R)/(P+R))
    print 'P = %f' % P



if __name__ == '__main__':
    eval_seg()
    eval_pos()
