import openseespy.opensees as ops
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## FUNZIONI ##
def Find( Ltreno, Ftreno, LTagEle, LtotStruttura, vTreno, dt = 0.01):
    #Ltreno: lista treno;
    #LTagEle: lista tag soggetti al carico già ordinati progressivamente;
    #LtotStruttura: lunghezza della struttura
    #vTreno: velocità del treno in m/s;
    Pstart = ops.nodeCoord(LTagEle[0])
    #Pend = ops.nodeCoord(LTagEle[-1])

    Lincr = []
    Lincr.append(0.0)
    for i in range(len(Ltreno)-1):
        Lincr.append( Lincr[i] + Ltreno[i+1] )
    
    PLoadPos = [ [ -i + Pstart[0], Pstart[1]]  for i in Lincr] #Posizione del carico al tempo zero
    print("PLoadPos", PLoadPos)

    Ltot = sum(Ltreno) + LtotStruttura
    t = Ltot/vTreno #tempo totale
  
    passo = vTreno*dt #incremento del passaggio in metri
    n = int(Ltot/passo)
    increment = np.linspace(0, Ltot, n)

    #Posizione carico nei vari incrementi
    PPosIncr = []
    for i in increment:
        pos = []
        for item in PLoadPos:
            pos.append([item[0] + i, item[1]])
        PPosIncr.append(pos)
    

    infoLoadIncr = []
    for iPos in PPosIncr:
        #print(iPos)
        saveForce = []
        for jPos, iF in zip(iPos, Ftreno):
            #print(jPos, iF)
            for iEle in LTagEle: #cordinate dei punti start e and degli elementi
                #print(iEle)
                #print(ops.eleNodes(iEle))
                cordI = ops.nodeCoord(ops.eleNodes(iEle)[0])[0] #cordinata X nodo I
                cordJ = ops.nodeCoord(ops.eleNodes(iEle)[1])[0] #cordinata X nodo J
                #print(cordI, cordJ)
                Lele = cordJ - cordI #lunghezza elemento
                #print(Lele)
                #print(jPos)
                if jPos[0] < cordJ and jPos[0] >= cordI:
                    xL = (jPos[0] - cordI)/Lele
                    saveForce.append([iEle, iF, xL])
                
                elif iEle == LTagEle[-1] and jPos[0] == cordJ: #per il passaggio sull'ultimo elemento
                    xL = (jPos[0] - cordI)/Lele
                    saveForce.append([iEle, iF, xL])
            
        infoLoadIncr.append( saveForce )
        #break
    
    return infoLoadIncr


        

def CurvaVAcc(vel, dt = 0.01):
### DEFINIZIONE VEICOLO ###
    #l = [0.0] #lunghezza veicolo
    #Pz = [1000] #peso per asse
    l = [0, 4.8, 2.6, 12.4, 2.6, 4.8, 2.6] #lunghezza veicolo
    Pz = [17*10, 17*10, 17*10, 17*10, 17*10, 17*10,  17*10] #peso per asse
    #l = [0, 2, 4, 2] #lunghezza veicolo
    #Pz = [17*9.8067, 17*9.8067, 17*9.8067, 17*9.8067] #peso per asse
    #l = [0, 2.6, 4.8, 2.6] #lunghezza veicolo
    #Pz = [17*9.8067, 17*9.8067, 17*9.8067, 17*9.8067] #peso per asse
    # successivamente lo trasformo in Newton

    ## DEFINIZIONE MODELLO ###
    passoDiscr = 0.5
    L = 20 # 11.3 #Lunghezza in metri
    rho = 2500 #kg/m

    E = 35000*1000**2 #Modulo elastico in N/m2
    m = 13000 #7730  #kg/m
    f1 = 4.04 #7.15 # Hz
    teta = 0.04
    
    ni = 0.2 #Poisson
    
    A = m/rho #Area
    Avy = (4/3)*A
    I = (((f1*2*L**2)/(np.pi))**2)*m/E
    print(A*1000, I*1000**4)
    
    G = E/(2*(1+ni))

    ops.wipe()
    ops.model('basic', '-ndm',2, '-ndf', 3)

    nPunti = int(L/passoDiscr) +1
    pX = np.linspace(0.0, L, nPunti)
    #print(pX)
    ### PUNTI ###
    for i, itemX in enumerate(pX):
        ops.node(i+1,itemX,0)

    ## VINCOLI
    ops.fix(1,1,1,0)
    ops.fix(nPunti, 0,1,0)


    transfTag = 1
    ops.geomTransf('Linear', transfTag)
    secTag = 1
    ops.section('Elastic', secTag, E, A, I)
    N = 10
    integrationTag = 1
    ops.beamIntegration('NewtonCotes', integrationTag, secTag, N)
    maxIter=50
    tol=1e-30
    ## ELEMENT ###
    for i in range(0, nPunti-1):
        eleTag = i+1
        eleNodes = [i+1, i+2]
        ops.element('elasticBeamColumn', eleTag, *eleNodes, secTag, transfTag, '-mass', m) #BERNOULLI BEAM
        #ops.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E, G, A, I, Avy, transfTag, '-mass', m) #TIMOSHENKO BEAM
        #ops.element('forceBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, '-iter', maxIter, tol, '-mass', m)
        #ops.element('dispBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, '-iter', maxIter, tol, '-mass', m)

    ##ANALISI MODALE
    numEigen = 1
    eigVals = ops.eigen(numEigen)
    #omega = np.sqrt(eigVals)
    #frequency = omega/(2*np.pi)
    #tetha_list = [teta1]*numEigen
    #ops.modalDamping(*tetha_list)
    #print(frequency)


    #wi = omega[0]**0.5 #2*np.pi/Ti
    #wj = omega[2]**0.5 #2*np.pi/Tj
    
    #A = np.array([[1/wi, wi],[1/wj, wj]])
    #b = np.array([teta1,teta2])
    
    #x = np.linalg.solve(A,2*b)
    Ti = 0.9*1*(f1) #0.9
    Tj =1*1/(4*f1) #0.2
    
    #CALCOLO MANUALE
    wi = 2*np.pi/Ti
    wj = 2*np.pi/Tj
    
    a = teta*(2*wi*wj)/(wi+wj)
    b = teta*(2)/(wi+wj)
    print("A", a,b)
    
    #             M    KT  KI  Kn
    #ops.rayleigh(x[0],0.0,0.0,x[1])
    ops.rayleigh(a,0.0,0.0,b)


    ops.timeSeries('Constant', 1)


    ops.constraints('Plain')
    ops.numberer('Plain')
    ops.system('FullGeneral')
    #ops.algorithm('Linear')
    #ops.algorithm('SecantNewton')
    ops.algorithm('NewtonLineSearch')
    gamma = 0.5
    beta = 1/4
    ops.integrator('Newmark', gamma, beta, "-form", 'D')
    ops.test('NormDispIncr', 1.0e-12, 50, 3)
    #ops.integrator('CentralDifference')
    #ops.integrator('ExplicitDifference')
    #ops.analysis('Static')
    ops.analysis('Transient')
    
    
    ## ANALISI PASSAGGIO DEL TRENO
    a = Find(l, Pz, ops.getEleTags(), L, vel/3.6, dt)

    s = []
    acc = []
    velocity = []
    Norms = []
    for i, item in enumerate(a):
        ops.pattern('Plain', 1, 1)
        for j in item:
            #print(j)
            ops.eleLoad('-ele', j[0], '-type', '-beamPoint', -j[1]*1000, j[2])
        #ops.setTime(i)

        ops.setTime(dt*i)
        ok = ops.analyze(1, dt) # dtMin=0.0, dtMax=0.0, Jd=0)
        
        norms = ops.testNorm()
        iters = ops.testIter()
        for j in range(iters):
            Norms.append(norms[j])
        
        if ok < 0:
            break
        
        
        ops.record()
        f = ops.nodeDisp(int(nPunti/2))
        acc.append(ops.nodeAccel(int(nPunti/2)))
        velocity.append(ops.nodeVel(int(nPunti/2)))        
        s.append(f)
        #ops.remove("elementLoad", "all")
        ops.remove('loadPattern', 1)

    timeCorrent = dt*i
    s_end = 5 #secondi in oscillazione libera
    for i in range(0, int(s_end/dt)):
        timeCorrent = timeCorrent + dt*i 
        ops.setTime(timeCorrent)
        ops.analyze(1, dt)    
        f = ops.nodeDisp(int(nPunti/2))
        acc.append(ops.nodeAccel(int(nPunti/2)))
        velocity.append(ops.nodeVel(int(nPunti/2)))
        
        s.append(f)
    
    acc = np.transpose(np.array(acc))[1]
    velocity = np.transpose(np.array(velocity))[1]
    s = np.transpose(np.array(s))[1]
    
    time = [ i*dt for i in range(0, len(acc))]
    plt.figure(1)
    plt.title("Spostamento")
    plt.plot(time, s*1000)


    #az = [ i[2] for i in acc]
    plt.figure(2)
    plt.title("Accelerazione")
    plt.plot(time, acc)
    

    #vz = [ i[2] for i in vel]
    plt.figure(3)
    plt.title("velocità")
    plt.plot(time, velocity)
    #plt.show()
    
    ##RECORDER
    # Create the pandas DataFrame
    data={'tempo [s]': time, 'accelerazione [m/s2]': acc, 'velocità [m/s]': velocity, 'spostamento [m]': s}
    df = pd.DataFrame(data)
    filename = "Result"+ str(vel) + ".xlsx" 
    df.to_excel(filename) 

    return [acc, velocity, s, time, df] 

accMax = []
velMax = []
defMax = []
velocity = list(range(20,355,5))
dt = 0.005 #dt = 0.005 equivale ad una frequenza di campionamento di 200 Hz


listdata = []

for i in velocity:
    print(i)
    resultModel = CurvaVAcc(i, dt)
    accMax.append(max(abs(max(resultModel[0])), abs(min(resultModel[0]))))
    velMax.append(max(abs(max(resultModel[1])), abs(min(resultModel[1]))))
    defMax.append(max(abs(max(resultModel[2])), abs(min(resultModel[2]))))
    listdata.append(resultModel[4])

filename = "Result"+".xlsx" 
with pd.ExcelWriter(filename) as writer:  
    for i, idata in enumerate(listdata):
        name = str(20+ i*5)
        idata.to_excel(writer, sheet_name=name)


plt.figure(4)
plt.title("Accelerazione massima in mezzeria [m/s2]")
plt.plot(velocity, accMax)


plt.figure(5)
plt.title("Coefficiente di amplificazione dinamica")
plt.plot(velocity, abs(defMax/defMax[0]))
#plt.show()


