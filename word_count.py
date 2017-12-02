#Random Python Scripts
#(c) 2017 Maroko Gideon
#www.gmaroko.me
#marokogideon@gmail.com
#question by Ayman Nov, 2017


from collections import Counter
def main(filename):
    with open(filename) as file: #with will automatically close the file for you
        words = [word for line in file for word in line.split()] #list of all the words in the file
        print("Total No. of words in file: {}".format(len(words))) #total number of words in the file
        print("#"*30)
        count = Counter(words)
        for word, counted in count.most_common():
            print(word, counted, end="\n") #print the word and the total number of its occurences


filename = (input("Filename> "))  #file name, full path if not on the same dir
main(filename)
