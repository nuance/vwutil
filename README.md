vwutil
======

a few utility scripts for working with vowpal wabbit


## vw-validate.py

    # validate a file of examples, dumping errors to stdout
    > cat bad_examples | python vw_validate.py
    Errors for example 0 ('1754 foo 29625274|x:2a: ('''Ch...’)
        Importance is not a float: 'foo'
        Extra : in namespace: 'x:2a:'
        Count must be a float: '2a'

## eval-classification.sh

    # Report classification performance
    > bash eval-classification.sh bfgs.model test.vw -ACC -REC -PRC -ROC -t 0
        ACC    0.93630   pred_thresh  0.000000
        PRE    0.60821   pred_thresh  0.000000
        REC    0.23453   pred_thresh  0.000000
        ROC    0.70345
