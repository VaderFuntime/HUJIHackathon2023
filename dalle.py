import os
import openai
genres = ['Realism', 'Impressionism', 'Cubism', 'Abstract Expressionism',
          'Surrealism', 'Pop Art', 'Minimalism', 'Modern art']

# openai.api_key = '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'
openai.api_key = 'smk-E8O9doroPMMqQBMyPSkeT3BlbkFJwe7FefTR2ZTSee1BnIiG'
openai.Model.list()
response = openai.Image.create(prompt='people waiting in a line surrounded '
                                      'by fire, modern art', n=1,
                            size="1024x1024")
image_url = response['data'][0]['url']
# print(image_url)
