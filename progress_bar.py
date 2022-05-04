from tqdm import tqdm, trange
import time
from colorama import Fore

green = Fore.GREEN

def progress_bar() -> None:
    print(green + '\r')
    with tqdm(total=100) as pbar:
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)

