import zebende as zb
import numpy as np

def rho_dcca(x, y, tws, ignore_anti_corr, square_values):
    x = x.reshape(x.shape[0], x.shape[1])
    y = y.reshape(y.shape[0], y.shape[1])
    input_data = np.concatenate((y, x), axis=0)
    dcca_of =[]
    for i in range(x.shape[0]):
        for j in range( x.shape[0], input_data.shape[0]):
            dcca_of.append([i,j])
    dcca_of = np.array(dcca_of)
    # print(dcca_of)
    # print(input_data.shape)
    dfa, dcca, pdcca = zb.p_dcca(input_data.T, tws=tws, DCCA_of=dcca_of)

    pdcca = pdcca.reshape(x.shape[0], y.shape[0])

    if square_values == True:
        compare_function = np.power
    if ignore_anti_corr == True:
        if square_values == True:
             dist = np.power(pdcca - 1, 2)
        else:
            dist =  np.abs(pdcca - 1)
    if ignore_anti_corr == False:
        if square_values == True:
             dist =  np.abs(np.power(pdcca, 2) - 1)
        else:
            dist = np.abs(np.abs(pdcca )- 1)

    return dist


def dfa_dist(x, y, tws):

    dfa_x = zb.dfa(x.T, tws)
    dfa_y = zb.dfa(y.T, tws)
    print('y_dfa_shape' , dfa_y.shape)
    dist = dfa_x.T - dfa_y
    return dist


