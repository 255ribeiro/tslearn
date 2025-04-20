import zebende as zb
import numpy as np

def rho_dcca(x, y, tws, ignore_anti_corr):
    x = x.reshape(x.shape[0], x.shape[1])
    y = y.reshape(y.shape[0], y.shape[1])
    input_data = np.concatenate((y, x), axis=0)
    dcca_of =[]
    for i in range(x.shape[0]):
        for j in range( y.shape[0]):
            dcca_of.append([i,j])
    dcca_of = np.array(dcca_of)
    print(dcca_of)
    print(input_data.shape)
    dfa, dcca, pdcca = zb.p_dcca(input_data.T, tws=tws, DCCA_of=dcca_of)

    pdcca.reshape(x.shape[0], y.shape[0])

    if ignore_anti_corr == True:
        return np.power(pdcca - 1, 2)
    if ignore_anti_corr == False:
        return np.abs(np.power(pdcca , 2) - 1)


