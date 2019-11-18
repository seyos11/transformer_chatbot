
from retrieval import RetrievalBot, DIALOG_SIZE

rb = RetrievalBot()

info1 = 'I like heavy metal'
info2 = 'I have three sons and one daughter'
info3 = 'Hello, how are you?'
info4 = 'I am fine, i am doing some math exercises'
info5 = 'I used to study in sofware engineering university?'
personality = [info1]
info = [info3,info4,info5]
utterance = list(info)
question = rb.generate_question(utterance,info1)
print(question)