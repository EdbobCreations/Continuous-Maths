import math

def Newton(xn, l):
    #Calculate f,df/dx and return x(n+1) by doing Newton's method
    f = math.pow(math.e,(l * (xn - 1)))-xn
    df = l * math.pow(math.e,(l * (xn - 1))) - 1
    return xn - (f/df)

def FindRoot(l):
    #set x0 to 0
    xn = 0
    x1 = Newton(xn, l)
    #Repeat Newton's method until the difference is less than 10^-10
    while(abs(x1 - xn) >= math.pow(10, -10)):
        xn = x1
        x1 = Newton(xn, l)
    return x1



if __name__ == '__main__':
    #Print results
    for i in range(10,100):
        l = i/10
        print("#Lambda: "+str(l)+" Extinction probability: " + str(FindRoot(l)))


#Results:
#Lambda: 1.0 Extinction probability: 0.999999999846167
#Lambda: 1.1 Extinction probability: 0.8238658563681899
#Lambda: 1.2 Extinction probability: 0.6863016689587824
#Lambda: 1.3 Extinction probability: 0.5770300479387075
#Lambda: 1.4 Extinction probability: 0.48898882116941017
#Lambda: 1.5 Extinction probability: 0.4171883561341886
#Lambda: 1.6 Extinction probability: 0.3580186826583003
#Lambda: 1.7 Extinction probability: 0.30881395128813477
#Lambda: 1.8 Extinction probability: 0.26757003336323365
#Lambda: 1.9 Extinction probability: 0.23275641080327503
#Lambda: 2.0 Extinction probability: 0.20318786997997998
#Lambda: 2.1 Extinction probability: 0.17793513179431633
#Lambda: 2.2 Extinction probability: 0.15626142691420447
#Lambda: 2.3 Extinction probability: 0.13757672198100823
#Lambda: 2.4 Extinction probability: 0.12140418022589237
#Lambda: 2.5 Extinction probability: 0.10735524639079086
#Lambda: 2.6 Extinction probability: 0.09511090502969878
#Lambda: 2.7 Extinction probability: 0.08440742006040607
#Lambda: 2.8 Extinction probability: 0.07502536923813248
#Lambda: 2.9 Extinction probability: 0.06678113003113138
#Lambda: 3.0 Extinction probability: 0.059520209292640354
#Lambda: 3.1 Extinction probability: 0.053111973777275376
#Lambda: 3.2 Extinction probability: 0.04744545497487032
#Lambda: 3.3 Extinction probability: 0.042425985058648016
#Lambda: 3.4 Extinction probability: 0.0379724810529469
#Lambda: 3.5 Extinction probability: 0.03401523843618071
#Lambda: 3.6 Extinction probability: 0.030494127975822218
#Lambda: 3.7 Extinction probability: 0.027357113879696245
#Lambda: 3.8 Extinction probability: 0.024559029609871635
#Lambda: 3.9 Extinction probability: 0.02206056154879473
#Lambda: 4.0 Extinction probability: 0.019827401281778418
#Lambda: 4.1 Extinction probability: 0.017829535396028565
#Lambda: 4.2 Extinction probability: 0.01604064799926546
#Lambda: 4.3 Extinction probability: 0.014437616075432615
#Lambda: 4.4 Extinction probability: 0.01300008165042874
#Lambda: 4.5 Extinction probability: 0.011710087783133344
#Lambda: 4.6 Extinction probability: 0.010551767811048975
#Lambda: 4.7 Extinction probability: 0.009511079205540347
#Lambda: 4.8 Extinction probability: 0.008575574935467997
#Lambda: 4.9 Extinction probability: 0.007734206481663519
#Lambda: 5.0 Extinction probability: 0.006977153651144741
#Lambda: 5.1 Extinction probability: 0.00629567715804225
#Lambda: 5.2 Extinction probability: 0.005681990605963713
#Lambda: 5.3 Extinction probability: 0.0051291490537781785
#Lambda: 5.4 Extinction probability: 0.0046309517970403655
#Lambda: 5.5 Extinction probability: 0.004181857369072736
#Lambda: 5.6 Extinction probability: 0.0037769090738432698
#Lambda: 5.7 Extinction probability: 0.0034116696190059884
#Lambda: 5.8 Extinction probability: 0.0030821636312540358
#Lambda: 5.9 Extinction probability: 0.0027848270150747853
#Lambda: 6.0 Extinction probability: 0.002516462266234263
#Lambda: 6.1 Extinction probability: 0.00227419897783476
#Lambda: 6.2 Extinction probability: 0.00205545888363815
#Lambda: 6.3 Extinction probability: 0.001857924873838221
#Lambda: 6.4 Extinction probability: 0.0016795134953101903
#Lambda: 6.5 Extinction probability: 0.0015183505137942796
#Lambda: 6.6 Extinction probability: 0.001372749171320506
#Lambda: 6.7 Extinction probability: 0.001241190819974619
#Lambda: 6.8 Extinction probability: 0.0011223076541008216
#Lambda: 6.9 Extinction probability: 0.0010148672982847567
#Lambda: 7.0 Extinction probability: 0.0009177590388350205
#Lambda: 7.1 Extinction probability: 0.0008299815127144341
#Lambda: 7.2 Extinction probability: 0.0007506316905772688
#Lambda: 7.3 Extinction probability: 0.0006788950102605529
#Lambda: 7.4 Extinction probability: 0.0006140365341913554
#Lambda: 7.5 Extinction probability: 0.0005553930190738861
#Lambda: 7.6 Extinction probability: 0.0005023657992212644
#Lambda: 7.7 Extinction probability: 0.0004544143962600841
#Lambda: 7.8 Extinction probability: 0.00041105077788558374
#Lambda: 7.9 Extinction probability: 0.00037183419707218407
#Lambda: 8.0 Extinction probability: 0.0003363665508113748
#Lambda: 8.1 Extinction probability: 0.0003042882041959476
#Lambda: 8.2 Extinction probability: 0.00027527423161601976
#Lambda: 8.3 Extinction probability: 0.0002490310320809482
#Lambda: 8.4 Extinction probability: 0.00022529328032060795
#Lambda: 8.5 Extinction probability: 0.00020382117942595134
#Lambda: 8.6 Extinction probability: 0.00018439798442826586
#Lambda: 8.7 Extinction probability: 0.00016682776944624018
#Lambda: 8.8 Extinction probability: 0.00015093341389941373
#Lambda: 8.9 Extinction probability: 0.0001365547858389066
#Lambda: 9.0 Extinction probability: 0.00012354710271902892
#Lambda: 9.1 Extinction probability: 0.00011177945195915546
#Lambda: 9.2 Extinction probability: 0.00010113345545272806
#Lambda: 9.3 Extinction probability: 9.15020637944362e-05
#Lambda: 9.4 Extinction probability: 8.278846743944125e-05
#Lambda: 9.5 Extinction probability: 7.490511329923686e-05
#Lambda: 9.6 Extinction probability: 6.777281643428917e-05
#Lambda: 9.7 Extinction probability: 6.131995753890648e-05
#Lambda: 9.8 Extinction probability: 5.54817578419919e-05
#Lambda: 9.9 Extinction probability: 5.019962388006777e-05