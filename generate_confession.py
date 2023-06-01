import openai
import translator

openai.api_key = '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'
MODEL_NAME = "davinci:ft-hujihackathon:conf-500-eng-2023-06-01-14-14-18"


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
    return eng, translator.eng_to_heb(eng)


def trim_to_last_dot(conf: str)-> str:
    return conf[:conf.rfind('.') + 1]


if __name__ == '__main__':
    print(f"hebrew: \n{generate_confession_eng_heb(max_tokens=200)}")
