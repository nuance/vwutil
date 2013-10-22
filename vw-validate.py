import fileinput


def check_header(header, err):
    """Validate the start of an example (everything up to the |)"""
    if not header:
        err("Header should not be empty")
        return

    parts = header.split(' ')

    if len(parts) > 3:
        err("Too many parts in the header: %d" % len(parts))

    try:
        float(parts[0])
    except ValueError:
        err("Label is not a float: \'%s\'" % parts[0])

    if len(parts) > 1:
        try:
            float(parts[1])
        except ValueError:
            err("Importance is not a float: \'%s\'" % parts[1])


def check_namespace(namespace, err):
    parts = namespace.split(' ')

    for idx, part in enumerate(parts):
        key = 'feature' if idx else 'namespace'

        if ':' not in part:
            continue

        feature_parts = part.split(':')
        if len(feature_parts) > 2:
            err('Extra : in %s: \'%s\'' % (key, part))

        try:
            float(feature_parts[1])
        except ValueError:
            err('Count must be a float: \'%s\'' % feature_parts[1])


def check_example(example, err):
    parts = example.split('|')
    if len(parts) <= 1:
        err('Expected an example with a header and at least one namespace')

    check_header(parts[0], err)
    for part in parts[1:]:
        check_namespace(part, err)

if __name__ == '__main__':
    for idx, line in enumerate(fileinput.input()):
        line = line.rstrip()
        erred = False

        def report_error(err):
            global erred
            if not erred:
                erred = True
                print 'Errors for example %d (\'%s\')' % (idx, line)

            print '\t' + err

        check_example(line, report_error)
