import pandas as pd
import translator as tr
from tqdm import tqdm


def translate_csv(csv_path: str):
    tqdm.pandas()
    df = pd.read_csv(csv_path)
    df['completion'] = df['completion'].progress_apply(tr.heb_to_eng)
    new_path = csv_path[:-4] + '_eng.csv'
    df.to_csv(new_path, index=False)


if __name__ == '__main__':
    translate_csv('confessions\ConfessionPosts500.csv')
