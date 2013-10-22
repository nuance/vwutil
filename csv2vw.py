#!/usr/bin/env python

import sys
import ast


if __name__ == '__main__':
    id_key = sys.argv[1]
    label_key = sys.argv[2]

    names = None
    for idx, line in enumerate(sys.stdin):
        values = ast.literal_eval(line)

        if not idx:
            names = values
        else:
            id_val = None
            label_val = None

            variables = {}
            for name, value in zip(names, values):
                if name == id_key:
                    id_val = value.replace(' ', '_')
                elif name == label_key:
                    label_val = value
                else:
                    if isinstance(value, (int, float, long)):
                        variables[name] = value
                    elif isinstance(value, basestring):
                        variables[name + '-' + str(value)] = 1
                    else:
                        print >>sys.stderr, 'unknown value for %s: %s' % (name, value)

            print '%f %s|a ' % (label_val, id_val) + ' '.join('%s:%d' % (k, v) for k, v in variables.iteritems())
