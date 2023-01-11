# markov_chains.py
"""Volume 2: Markov Chains.
Bryant McArthur
Math 320
11/10/21
"""

import numpy as np
from scipy import linalg as la


class MarkovChain:
    """A Markov chain with finitely many states.

    Attributes:
        self.A: the transition matrix
        self.labels: a list of all possible states
        self.labels_to_indices: a dictionary that maps labels to their indices in self.A
    """
    # Problem 1
    def __init__(self, A, states=None):
        """Check that A is column stochastic and construct a dictionary
        mapping a state's label to its index (the row / column of A that the
        state corresponds to). Save the transition matrix, the list of state
        labels, and the label-to-index dictionary as attributes.

        Parameters:
        A ((n,n) ndarray): the column-stochastic transition matrix for a
            Markov chain with n states.
        states (list(str)): a list of n labels corresponding to the n states.
            If not provided, the labels are the indices 0, 1, ..., n-1.

        Raises:
            ValueError: if A is not square or is not column stochastic.

        Example:
            >>> MarkovChain(np.array([[.5, .8], [.5, .2]], states=["A", "B"])
        corresponds to the Markov Chain with transition matrix
                                   from A  from B
                            to A [   .5      .8   ]
                            to B [   .5      .2   ]
        and the label-to-index dictionary is {"A":0, "B":1}.
        """
        self.n, _ = A.shape  # get the size of the transition matrix

        u = np.round(np.sum(A, axis=0))  # get the column sum of the transition matrix

        v = np.ones((self.n,))

        if not np.array_equal(u, v):
            raise ValueError('A must be column stochastic.')

        if not states:
            states = list(range(self.n))  # if there're no state labels given, use the labels [0 1 ... n-1]

        self.A = A
        self.labels = states
        self.labels_to_indices = {state: i for i, state in enumerate(states)}  # construct a dictionary mapping the state labels to the row/column index that they correspond to in A

    # Problem 2
    def transition(self, state):
        """Transition to a new state by making a random draw from the outgoing
        probabilities of the state with the specified label.

        Parameters:
            state (str): the label for the current state.

        Returns:
            (str): the label of the state to transitioned to.
        """
        i = self.labels_to_indices[state]
        column = self.A[:, i]  # determine the column of A that corresponds to the provided state label
        draw = np.random.multinomial(1, column)
        j = np.argmax(draw)
        
        

        return self.labels[j],column


    # Problem 3
    def walk(self, start, N):
        """Starting at the specified state, use the transition() method to
        transition from state to state N-1 times, recording the state label at
        each step.

        Parameters:
            start (str): The starting state label.

        Returns:
            (list(str)): A list of N state labels, including start.
        """
        state = start  # start at the specified state
        labels = [state]
        for _ in range(N - 1):
            state = self.transition(state)  # transition from state to state N - 1 times
            labels.append(state)

        return labels

    # Problem 3
    def path(self, start, stop):
        """Beginning at the start state, transition from state to state until
        arriving at the stop state, recording the state label at each step.

        Parameters:
            start (str): The starting state label.
            stop (str): The stopping state label.

        Returns:
            (list(str)): A list of state labels from start to stop.
        """
        state = start
        labels = [state]
        while state != stop:
            state = self.transition(state)  # transition from state to state until arriving at the specified end state
            labels.append(state)

        return labels

    # Problem 4
    def steady_state(self, tol=1e-12, maxiter=40):
        """Compute the steady state of the transition matrix A.

        Parameters:
            tol (float): The convergence tolerance.
            maxiter (int): The maximum number of iterations to compute.

        Returns:
            ((n,) ndarray): The steady state distribution vector of A.

        Raises:
            ValueError: if there is no convergence within maxiter iterations.
        """
        x0 = np.random.rand(self.n, 1)  # generate a random state distribution vector

        i = 0
        converge = False
        while i < maxiter:
            x1 = np.dot(self.A, x0)
            if la.norm(x0 - x1) < tol:
                converge = True
                break

            x0 = x1
            i += 1

        if not converge:
            raise ValueError('Ak must converge.')

        return x1



class SentenceGenerator(MarkovChain):
    """A Markov-based simulator for natural language.

    Attributes:
        (fill this out)
    """
    # Problem 5
    def __init__(self, filename):
        """Read the specified file and build a transition matrix from its
        contents. You may assume that the file has one complete sentence
        written on each line.
        """

        '''read the file and build a transition matrix from its contents'''
        with open(filename, 'r') as file:
            '''Algorithm 1.1 Convert a training set of sentences into a Markov chain'''
            sentences = file.read().split('.')  # read the training set from the file filename
            unique_words = set()
            for sentence in sentences:
                words = sentence.split()
                unique_words.update(words)  # get the set of unique words in the state labels
                
                
            unique_words = list(unique_words)
            
            """
            for word in unique_words:
                if word[0].isnumeric() == True:
                    unique_words.remove(word)
            """
            
            
            unique_words = ['$tart'] + unique_words + ['$top']  # add labels "$tart" and "$top" to the set of state labels
            n = len(unique_words)
            

            words_to_indices = {word: i for i, word in enumerate(unique_words)}

            M = np.zeros((n, n))  # initialize the transition matrix

            for sentence in sentences:
                words = sentence.split()
                words = ['$tart'] + words + ['$top']
                for i in range(len(words) - 1):
                    x, y = words[i], words[i + 1]
                    j, k = words_to_indices[x], words_to_indices[y]
                    M[k][j] += 1  # add 1 to the entry of the transition matrix that corresponds to transitioning from state x to state y

            M[-1][-1] = 1  # make sure the stop state transitions to itself
            M /= np.sum(M, axis=0)  # normalize each column by dividing by the column sums

            super().__init__(M, unique_words)

    # Problem 6
    def babble(self):
        """Create a random sentence using MarkovChain.path().

        Returns:
            (str): A sentence generated with the transition matrix, not
                including the labels for the $tart and $top states.

        Example:
            >>> yoda = SentenceGenerator("yoda.txt")
            >>> print(yoda.babble())
            The dark side of loss is a path as one with you.
        """

        raw_sentence = self.path('$tart', '$top')
        raw_sentence_stripped = raw_sentence[1:-1]
        sentence = ' '.join(raw_sentence_stripped)

        return sentence

    #Ling Task 6
    def task6(self,word):
        """Print Steady State"""
        nextword,column = self.transition(word)
        wordsandprobs = {}
        
        for i in range(len(column)):
            if column[i] != 0:
                wordsandprobs[list(self.labels_to_indices.keys())[list(self.labels_to_indices.values()).index(i)]] = column[i]
                
        sorted_probability = sorted(wordsandprobs.items(), key=lambda x: x[1], reverse=True)
        
        return nextword,column,self.labels_to_indices,sorted_probability
    
    
    

if __name__=='__main__':
    """
    weather = MarkovChain(np.array([[0.7, 0.6], [0.3, 0.4]]), ['hot', 'cold'])
    print(weather.labels)
    print(weather.labels_to_indices)

    yoda = SentenceGenerator('yoda.txt')
    for _ in range(3):
        print(yoda.babble())
    """
     
    d = dict()
    text = open('Communist Manifesto.txt','r',encoding = "utf-8")
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(' ')
        for word in words:
            if word in d:
                d[word] = d[word]+1
            else:
                d[word] = 1
                
    print('done')
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse = True)
    print(sorted_d[:25])
    
    top_words = [i[0] for i in sorted_d[:25]]
    top_words.remove(str(""))
    print(top_words)
     
    CM = SentenceGenerator("Communist Manifesto.txt")
    for word in top_words:
        if word != "project":
            print("Word:", word)
            w,c,d,p = CM.task6(word)
            print(p[:2])
    
    for _ in range(5):
        print(CM.babble())
    """
    BoM = SentenceGenerator('The Book of Mormon.txt')
    for _ in range(1):
        #print(BoM.babble())
        word,column,dictionary,prob = BoM.task6("Nephi")
        print(prob)
    """

    pass
