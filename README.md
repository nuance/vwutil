vwutil
======

a few utility scripts for working with vowpal wabbit


## vw-validate.py

validate a file of examples, dumping errors to stdout

    > cat bad_examples | python vw_validate.py
    Errors for example 0 ('1754 foo 29625274|x:2a: ('''Ch...’)
        Importance is not a float: 'foo'
        Extra : in namespace: 'x:2a:'
        Count must be a float: '2a'

## eval-classification.sh

Report classification performance against a set of examples

    > bash eval-classification.sh bfgs.model test.vw -ACC -REC -PRC -ROC -t 0
        ACC    0.93630   pred_thresh  0.000000
        PRE    0.60821   pred_thresh  0.000000
        REC    0.23453   pred_thresh  0.000000
        ROC    0.70345

## eval-regression.sh

Report regression performance against a set of examples

    > bash eval-regression.sh bfgs.model test.vw
        RMSE: 79.757854
        RSQR: 0.277733

## csv2vw.py

Convert csv data to vw format.

Given a csv file with a header like datasets/chredlin.csv:

    "","race","fire","theft","age","involact","income","side"
    "60626",10,6.2,29,60.4,0,11.744,"n"
    "60640",22.2,9.5,44,76.5,0.1,9.323,"n"
    "60613",19.6,10.5,36,73.5,1.2,9.948,"n"

Convert it to vw input by calling csv2vw with the id variable name and the value to predict.

    > cat datasets/chredlin.csv | python csv2vw.py "" "involact"
    0.000000 60626|a fire:6 age:60 race:10 theft:29 income:11 side-n:1
    0.100000 60640|a fire:9 age:76 race:22 theft:44 income:9 side-n:1
    1.200000 60613|a fire:10 age:73 race:19 theft:36 income:9 side-n:1
    0.500000 60657|a fire:7 age:66 race:17 theft:37 income:10 side-n:1
    0.700000 60614|a fire:8 age:81 race:24 theft:53 income:9 side-n:1
