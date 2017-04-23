import argparse
import unittest


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", dest="start_dir", nargs="?",
                        type=str, default=".",
                        help="Name of root directory for test cases discovery")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    suite = unittest.TestLoader().discover(start_dir=args.start_dir)
    unittest.TextTestRunner(verbosity=2).run(suite)