import argparse
import torch

def get_train_config():
    parse = argparse.ArgumentParser(description='CBC model')
    parse.add_argument('-devicenum', type=int, default=2, help='device id')
    # parse.add_argument('-lr', type=float, default=0.00001, help='learning rate')
    parse.add_argument('-lr', type=float, default=0.001, help='learning rate')
    # parse.add_argument('-epoch', type=int, default=200, help='device id')
    # parse.add_argument('-epoch', type=int, default=2000, help='device id')
    parse.add_argument('-epoch', type=int, default=300, help='epoch num')
    # parse.add_argument('-epoch', type=int, default=3000, help='epoch num')
    config = parse.parse_args()
    config.device = torch.device('cuda', config.devicenum)
    return config
# nohup python train_and_test_AntiACP_Alternate.py > /mnt/sdb/home/yxt/CBC_and_DATA/result/_AntiACP_Alternate_lr=0.000005_epoch=3000.log 2>&1 &