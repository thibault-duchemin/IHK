import io
import argparse

def initialize_argument_parser():
    parser = argparse.ArgumentParser(description='Simulate Indian health solutions')
    parser.add_argument('-s', '--solution', dest='solution', 
            help='the solution to test', default='health kiosk')
    return vars(parser.parse_args())

if __name__ == "__main__":
    args = initialize_argument_parser()
    print 'Solution to test:', args['solution']