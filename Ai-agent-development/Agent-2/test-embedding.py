# here we are going to generate embedding vectors based on the data provided



from openai import OpenAI
from similarity import cosine_similarity

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
text1 = "Python is a programming language"
text2 = "Python is used for software developement"

embedding1 = client.embeddings.create(
    model="nomic-embed-text",
    input= text1
)

embedding2 = client.embeddings.create(
    model="nomic-embed-text",
    input= text2
)

embedding3 = client.embeddings.create(
    model="nomic-embed-text",
    input= "pizza is delicious"
)

#printing consine score
print(cosine_similarity(embedding1.data[0].embedding, embedding2.data[0].embedding)) #more similar score is 0.77

print(cosine_similarity(embedding1.data[0].embedding, embedding3.data[0].embedding)) #less similar score is 0.41


# embedding = response.data[0].embedding

# print(len(embedding))
# print(type(embedding))