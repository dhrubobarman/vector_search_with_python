import os
import utils

query = "imaginary characters from outer space at war"

print('------------------started------------------\n')
result = utils.collection.aggregate([{
    "$vectorSearch": {
        "queryVector": utils.generate_embedding(query),
        "path": "plot_embedding_hf",
        "numCandidates": 100,
        "limit": 4,
        "index": "PloatSemanticSearch"
    }
}])


for document in result:
    print(f"{document['title']}:\n{document['plot']}")
print('------------------finished------------------\n')

print(utils.generate_embedding_oai(query))
