#!/usr/bin/env python3
"""
    Hidden Markov Models project
"""
import numpy as np


def lock(boxes):
    ''' lockbox method to determine if edges connected
            to absorbing state
    '''
    length = len(boxes)
    open = [0 for i in range(length)]
    open[0] = 1
    s = [0]
    while s:
        n = s.pop()
        for i in boxes[n]:
            try:
                if not open[i]:
                    open[i] = 1
                    s.append(i)
            except IndexError:
                pass
    os = sum(open)
    return True if os == length else False


def absorbingg(P):
    """ determines if a markov chain is absorbing:
        P square 2D ndarray (n, n) transition matrix
            P[i, j] is the probability of transitioning from state i to state j
            n is the number of states in the markov chain
        Returns: True if it is absorbing, or False on failure
    """
    if type(P) is not np.ndarray or\
            len(P.shape) != 2 or \
            P.shape[0] != P.shape[1]:
        return False

    # print("1", P == 1)
    # print("2", np.any(P == 1, axis=0))
    # print(P[:, np.any(P==1, axis=1)])
    # print(np.argwhere(P != 0))
    # print(np.where(P != 0))
    # box = []
    # for p in P:
    #    box.append(p.nonzero())

    # print(np.any(P!=0, axis=1))
    # print(np.nonzero(P))
    # print(lock(P[:, np.any(P==1, axis=0)] ))
    # return
    diag = np.diag(P)
    # dim = P.shape[0]
    '''q = (P - np.eye(dim))
    ones = np.ones(dim)'''
    # print("q", q)
    '''q = np.c_[q, ones]
    QTQ = np.dot(q, q.T)
    # print(QTQ)
    bQT = np.ones(dim)'''
    # print("bQT", bQT)
    # print("solved", np.linalg.solve(QTQ, bQT))
    # print(diag)
    if np.any(diag == 1):  # and regular(P) == None:
        # try:
        # Q, R = decompose(P)
        # print("q", Q, "R", R)
        '''if np.all(np.sum(Q, axis=0)) == True:
            #n = expected_steps_fast(Q)
            #print(n)
            #print(96)
            return True'''
        # d, v = np.linalg.eig(P)
        # s = np.sum(v @ np.diag(d >= 1).astype(int)
        # @ np.linalg.inv(v), axis=1)
        # print(s)
        # if (s == 1).all():
        #    # print(96)
        #    return True
        box = []
        for p in P:
            box.append(np.argwhere(p != 0).tolist()[0])
        b = lock(box)
        if b:
            return False
        # else:
        #    #print(99)
        #    return False
        ''' I must be same size as Q '''
        # I = np.eye(Q.shape[0])
        # iq = I - Q
        # F = np.linalg.pinv(iq)
        # FR = F.T @ R
        # print("FR", FR)
        # except Exception as E:
        #    print(E)
        #    return False
        return True
    else:
        return False
