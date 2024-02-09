import random
import csv
from loguru import logger

from utils import Minter, Bridger
from info import keys
from config import shuffle, MODE, chain, to_chain, moralis_api, delay, count
from config import minter_mode, bridger_mode, NAME



def write_to_csv(key, address, result):
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(['key', 'address', 'result'])

        writer.writerow([key, address, result])

def main():
    if shuffle:
        random.shuffle(keys)

    if MODE == 'minter':
        logger.info(f'Minting started {NAME}...')
        for key in keys:
            mint_ = Minter(key, chain, count, delay, minter_mode)
            res = mint_.mint()
            write_to_csv(*res)
    if MODE == 'bridger':
        logger.info(f'Bridging started {NAME}...')
        for key in keys:
            bridge_ = Bridger(key, chain, to_chain, delay, moralis_api, bridger_mode)
            res = bridge_.bridge()
            write_to_csv(*res)


    if MODE == 'minter':
        logger.success('Minting complete')
    else:
        logger.success('Bridging complete')

if __name__ == '__main__':
    main()
