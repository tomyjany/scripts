def computeThetaSGD(x, y, alpha=0.1, nIter=100, order=1, lmbd=0):
    """
    x - vektor vstupnich hodnot, doba studia
    y - vektor vystupnich  hodnot, zisk bodu
    alpha - krok
    nIter - pocet iteraci
    order - rad polynomu
    lmbd - regularizacni parametr lambda
    """
    
    #################################################################
    # ZDE DOPLNIT
    
    #x = np.insert(x, 0, 1, axis=1)
    bias_vector = np.ones((x.shape[0], order))
    x = np.concatenate((bias_vector,x), axis = 1)
    #theta = np.array([0,0], ndmin=2).T
    theta = np.zeros(order+1).reshape(-1,1)
    print(theta)
    for i in range(0,nIter):
        temp = np.dot(theta.T,x.T)
        temp = (temp.T - y)
        theta = theta*(1 - alpha*lmbd) - ( alpha *  x.T@(temp))
    #...
    
    #################################################################
    return theta
