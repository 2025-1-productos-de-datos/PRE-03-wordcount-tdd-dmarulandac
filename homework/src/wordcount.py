## wordcount.py

import os
import sys

from homework.src._internals.parse_args import parse_args


def read_all_lines(input_folder):
    lines=[]
    for filename in os.listdir(input_folder):
        file_path=os.path.join(input_folder,filename)
        with open(file_path,"r",encoding="utf-8")as f:
            lines.extend(f.readlines())
    return lines




def main():
    input_folder, output_folder = parse_args()
    lines=read_all_lines(input_folder)