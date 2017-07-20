import numpy as np
from tensorflow.contrib import learn

x_text = ['This is a cat','This must be boy', 'This is a a dog']
max_document_length = max([len(x.split(" ")) for x in x_text])

## Create the vocabularyprocessor object, setting the max lengh of the documents.
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)

## Transform the documents using the vocabulary.
x = np.array(list(vocab_processor.fit_transform(x_text)))

## Extract word:id mapping from the object.
vocab_dict = vocab_processor.vocabulary_._mapping

## Sort the vocabulary dictionary on the basis of values(id).
## Both statements perform same task.
#sorted_vocab = sorted(vocab_dict.items(), key=operator.itemgetter(1))
sorted_vocab = sorted(vocab_dict.items(), key = lambda x : x[1])

## Treat the id's as index into list and create a list of words in the ascending order of id's
## word with id i goes at index i of the list.
vocabulary = list(list(zip(*sorted_vocab))[0])

r_label=[]
label=[1,2,3,4,5]

for l_num in label:
    lst = [0 for _ in range(5)]
    lst[-l_num] = 1
    r_label.append(lst)  # lst 범위 max_num까지 다 1로 바꾸고 r_label에 저장
r_label = np.array(r_label)
y = r_label

print(vocabulary)
print(x)

np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(y)))
x_shuffled = x[shuffle_indices]
y_shuffled = y[shuffle_indices]

print ("x : ",x_shuffled)
print ("y : ",y_shuffled)
