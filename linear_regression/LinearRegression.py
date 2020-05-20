"""
Author: Tony Code
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#prepare data
train_X = np.linspace(-1,1,100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3
#visualize data
plt.plot(train_X,train_Y,'ro', label = 'Original data')
plt.legend()
plt.show()

#create model
#placehoder
X = tf.placeholder("float32")
Y = tf.placeholder("float32")
#model parameters
W = tf.Variable(tf.random_normal([1]),name = "weight")
b = tf.Variable(tf.zeros([1],name = "bias"))

#forward propagation
z = tf.multiply(X,W) + b
tf.summary.histogram('z',z)   #display the predicted value as a histogram

#back propagation
cost = tf.reduce_mean(tf.square(Y - z))
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
tf.summary.scalar('loss function', cost)   #display loss in scalar

#train
init = tf.global_variables_initializer()

#define tarining parameters
training_epochs = 20

display_step = 2

saver = tf.train.Saver()
modelpath = "model/"
filename = "model-{}".format(training_epochs)

#start session
with tf.Session() as sess:
    sess.run(init)

    merged_summary_op = tf.summary.merge_all()  #merge all summary
    #create summary_writer to write into file 
    summary_writer = tf.summary.FileWriter('log/mnist_with_summaries',sess.graph)
    
    plotdata = {"batchsize":[],"loss":[]}
    #feed data to the model 
    for epoch in range(training_epochs):
        for (x,y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict = {X:x, Y:y})

        summary_str = sess.run(merged_summary_op,feed_dict = {X:x,Y:y})
        summary_writer.add_summary(summary_str,epoch)

        #print train information
        if epoch % display_step == 0:
            loss = sess.run(cost, feed_dict = {X:train_X, Y:train_Y})
            print("Epoch:", epoch, "loss = ", loss, " W = ", sess.run(W), " b = ", sess.run(b))
            if not (loss == "NA"):
                plotdata["batchsize"].append(epoch)
                plotdata["loss"].append(loss)

    #save model
    saver.save(sess,modelpath+filename)
    
    print("Train Finished!")
    print("loss = ", sess.run(cost,feed_dict = {X:train_X,Y:train_Y})," W = ",sess.run(W)," b = ", sess.run(b))
        
    #visualization
    def moving_average(a, w=10):
        if len(a) < w:
            return a[:]
        return [val if idx < w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]
    
    plt.plot(train_X,train_Y,'ro', label = 'Original data')
    plt.plot(train_X, sess.run(W)*train_X + sess.run(b), label = 'Fittedline')
    plt.legend()
    plt.show()

    plotdata["avgloss"] = moving_average(plotdata["loss"])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata["batchsize"], plotdata["avgloss"], 'b--')
    plt.xlabel('Minibatch number')
    plt.ylabel('Loss')
    plt.title('Minibatch run vs Training loss')
    plt.show()
    
    #test model
    print("x = 0.2,z = ",sess.run(z,feed_dict = {X:0.2}))
    













            
