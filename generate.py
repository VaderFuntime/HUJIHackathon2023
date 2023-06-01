import openai

openai.api_key = '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'
MODEL_NAME = "curie:ft-hujihackathon-2023-06-01-11-39-13"


def generate_confession():
    res = openai.Completion.create(
        model=MODEL_NAME,
        prompt="Hey my name is John and "
    )
    return res.choices[0]['text']



if __name__ == '__main__':
    print(generate_confession())