import random

import openai
import translator

openai.api_key = '' \
                 ''
OLD_MODEL_NAME = "davinci:ft-hujihackathon:conf-500-eng-2023-06-01-14-14-18"
MODEL_NAME = "curie:ft-hujihackathon:ver2-curie-2023-06-01-23-02-56"


def generate_confession_english(max_tokens, temperature):
    res = openai.Completion.create(
        model=MODEL_NAME,
        prompt="#335",
        max_tokens=max_tokens,
        temperature=temperature,
        presence_penalty=1,
        frequency_penalty=0.5,
    )
    return trim_to_last_dot(res.choices[0]['text'])


def generate_confession_eng_heb(max_tokens: int = 100, temperature: float = 0.4):
    eng = generate_confession_english(max_tokens=max_tokens, temperature=temperature)
    heb = translator.eng_to_heb(eng)
    return eng, add_random_number(heb)


def trim_to_last_dot(conf: str)-> str:
    return conf[:conf.rfind('.') + 1]

def add_random_number(conf: str) -> str:
    # sample a random number between 1 and 40000
    random_number = str(random.randint(1, 40000))
    # add the random number to the confession
    return f"#{random_number}\n{conf}"

if __name__ == '__main__':
    print(f"hebrew: \n{generate_confession_eng_heb(max_tokens=200, temperature=1)}")
