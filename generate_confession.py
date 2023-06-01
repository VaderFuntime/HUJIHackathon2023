import openai
import translator

openai.api_key = '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'
MODEL_NAME = "davinci:ft-hujihackathon:conf-500-eng-2023-06-01-14-14-18"


def generate_confession_english(max_tokens, temperature):
    res = openai.Completion.create(
        model=MODEL_NAME,
        prompt="#335",
        max_tokens=max_tokens,
        temperature=temperature
    )
    print(f"english: \n{res.choices[0]['text']}")
    return res.choices[0]['text']


def generate_confession_hebrew(max_tokens=100, temperature=0.4):
    return translator.eng_to_heb(
        generate_confession_english(max_tokens=max_tokens, temperature=temperature))


if __name__ == '__main__':
    print(f"hebrew: \n{generate_confession_hebrew(max_tokens=200)}")
