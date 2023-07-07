import spacy
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.ent_type_)
    print('\n')

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    print('\n')

# Look up and print the explanations of entities you don't understand
print(spacy.explain("FAC"))
print(spacy.explain("GPE"))


# 1. FAC (Facility) - It represents buildings, airports, highways, bridges, etc.
#    This entity makes sense in terms of the sentence "The cotton clothing is made of grows in Mississippi" as it refers to a specific location.
# 2. GPE (Geo-Political Entity) - It represents countries, cities, and states.
#    This entity makes sense in terms of theThe above example demonstrates how to tokenize sentences, perform named entity recognition (NER), and entity recognition (ER) using spaCy in Python. It also showcases the use of `spacy.explain()` to look up and print the explanations of entity types.

'''In the provided comment at the bottom of the file, two entities were looked up: `FAC` (Facility) and `GPE` (Geo-Political Entity). Here are the answers to the questions for each entity:

1. `FAC` (Facility): It represents buildings, airports, highways, bridges, etc. In the context of the sentence "The cotton clothing is made of grows in Mississippi," 
it may refer to a facility or building involved in the cotton clothing production process. 
The association between "facility" and "cotton clothing" makes sense as cotton clothing is typically manufactured in facilities or factories.

2. `GPE` (Geo-Political Entity): It represents countries, cities, and states. In the same sentence, 
"The cotton clothing is made of grows in Mississippi," the entity `GPE` refers to the state of Mississippi,
 which is a geo-political entity. This association makes sense as Mississippi is a state and can be considered 
 the location where the cotton used for making the clothing grows.'''