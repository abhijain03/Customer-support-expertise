import pandas as py


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier


from sklearn import metrics
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatwindow import *
from client import *

data=py.read_csv('../data/train_tweets.csv',delimiter=',',encoding='iso-8859-1',names=["result","tweet_id","date","query_type","user_id","text"])
x=data['text']
y=data['result']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)


count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(x)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y)
#clf=SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3,max_iter=10, tol=.21).fit(X_train_tfidf, y)


X_new_counts = count_vect.transform(x_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

y_pred = clf.predict(X_new_tfidf)


print("Accuracy",metrics.accuracy_score(y_test,y_pred))

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

responses=[]
def response():
    global responses
    def chunkstring(string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    global chat,chatbot
    ques=str(chat.text_var.get())
    docs_new=ques
    X_new_counts = count_vect.transform([docs_new])
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)
    responses.append(int(predicted))
    prev=chat.chat
    ans=chatbot.get_response(ques)
    user="\nYou: "+ques
    user=list(chunkstring(user, 20))
    user=('\n').join(user)
    bot="\nbot: "+str(ans)
    bot=list(chunkstring(bot, 20))
    bot=('\n').join(bot)
    data=chat.chat+user+bot
    chat.chat=data
    chat.textarea.delete('msgs')
    chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')
    
    if responses.count(0)>=4:
        chat.root.destroy()
        client_program()
        
        


trainer = ListTrainer(chatbot)

trainer.train(["hello ",
                "Hello Sir/Maam, How may I help you?",
                "hi ",
               "Hello Sir/Maam, How may I help you?",
               "i need your help",
                "Hello Sir/Maam, How may I help you?",
                
               "hello, my latop is not working?",
               "describe the problem please",
               "problem is  ",
               "ok, have you tried troubleshooting it?",
               "No it wont help?",
               "we will try to solve it as soon as possible and inform our executive"
               ])
# Get a response to the input text 'I would like to book a flight.'

chat=chatwindow()
chat.submit.configure(command=response)
chat.root.mainloop()

