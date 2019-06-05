#!/home/ubuntu/environment/NeuralNet/bin/python3

from textgenrnn import textgenrnn as tgr

textgen = None

if input("use preexisting weights (y/n): ") == 'n':
    textgen = tgr() # create a rnn
    textgen.reset() # just in case
    textgen.train_from_largetext_file("plain_articles.txt", new_model=True, num_epochs = int(input("Epochs (Recommended 50):")))
    textgen.save("truenews.hdf5")
else:
    textgen = tgr("truenews.hdf5")

go = False

temp = 0.5

while not go:
    go = True
    temp = int(input("Temperature (0.5 recommended): "))
    if temp > 1:
        if input("It is not recommended to have a temperature over 1.0. Are you sure? (y/n): ") != 'y':
            go = False
            pass
    elif temp <= 0:
        print("that won't work")
        raise IOError("Temperature must be positive.")

num = int(input("Number of documents: "))

textgen.generate(num, temperature = temp)        