#!/usr/bin/env python
import argparse
import glob
import json
import os


def load_files(input_dir):
    data = []
    if os.path.exists(input_dir):
        for file in os.listdir(input_dir):
            if file.endswith(".json"):
                json_file = json.load(open(os.path.join(input_dir, file), 'r'))
                data.extend(json_file['values'])
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser("demo argument parser")
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--input_dir_2', default="")
    parser.add_argument('--output_dir', required=True)
    parser.add_argument(
        '-c', '--configuration_file',
        action='store',
        required=True,
        dest='config',
        help='Path to config file')

    args = parser.parse_args()

    data = load_files(input_dir=args.input_dir)
    data2 = load_files(input_dir=args.input_dir_2)
    result = {}

    directory = glob.glob("/pfs/**", recursive=True)
    print(directory)
    if len(data2) == len(data) > 0:
        result = {"values": [data[i] + data2[i] for i in range(len(data))]}
        json.dump(result, open(os.path.join(args.output_dir, "output.json"), 'w'))
    elif len(data) > 0 and os.path.isfile(args.config) and args.input_dir_2 == "":

        config = json.load(open(args.config, 'r'))
        if config['action'] == 'add':
            result = {"values": [i + config['value'] for i in data]}
        elif config['action'] == 'multiply':
            result = {"values": [i * config['value'] for i in data]}
        elif config['action'] == 'power':
            result = {"values": [pow(i, config['value']) for i in data]}
        else:
            result = {"values": data}
        json.dump(result, open(os.path.join(args.output_dir, "output.json"), 'w'))
        print("job completed successfuly")
    else:
        print("nothing happened with {} being a file: {}".format(args.config, os.path.isfile(args.config)))
