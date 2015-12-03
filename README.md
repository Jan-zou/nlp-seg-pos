# nlp-seg-pos

Using CRF++ in some NLP tasks（dataset: 人民日报）


1. Install CRF++

        cd CRF++-0.58
        ./configure
        make
        sudo make install


2. Files statements

Under `data/`:
+ Raw DataSets: data.txt
+ Dictionary: dict.txt
+ training data(90%): train_seg.txt, train_pos.txt
+ test data(10%): test_seg.txt, test_pos.txt


3. Results statements
Under `result/seg/` or `result/pos/`:

+ `*.data`: 训练测试输入格式数据
+ `template`: 特征模板
+ `output.txt`: 训练测试结果
+ `result.txt`: 处理后的最终结果


4. Segmentation & Part-Of-Speech Tagging

        python preprocess.py  # split 90% train, 10% test
        python segmentation.py
        python pos.py
        python crfveal.py  # 评估结果

