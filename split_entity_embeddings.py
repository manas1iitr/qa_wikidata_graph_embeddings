import numpy as np

ent_emb = {}
sz = 50000
entity_emb = np.load('entity_embeddings.npy')
print(len(entity_emb))

j=0
for i in range(0, len(entity_emb), sz):
    print(i)
    if i+sz < len(entity_emb):
        ent_emb[j] = entity_emb[i:i+sz:1]
    else:
        ent_emb[j] = entity_emb[i:len(entity_emb):1]
    j = j+1
    print(j)

# print(len(ent_emb))
# print(ent_emb[0].shape)
# print(ent_emb[9].shape)

for i,emb in enumerate(ent_emb):
    np.save('entity_embeddings_%d' % (i), emb)