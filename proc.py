import sys
name=sys.argv[1]
x=open('{0}'.format(name),'r')
y=open('results.txt','a')
f=x.readline()
while f:
    if f.startswith('BASIS'):
        g=f.split()
        basis=g[1]
        #print(basis)
    if f.startswith('METHOD'):
        g=f.split()
        method=g[1]
    if f.startswith(' Total energy in the final basis set ='):
        g=f.split()
        energy=g[8]
    if f.startswith('       Tot'):
        g=f.split()
        dip=g[1]
    if f.startswith(' Total job time:'):
        g=f.split()
        time=g[3]
    f=x.readline()
processed='{0}, {1}, {2}, {3}, {4}, {5} \n'.format(name,method,basis,energy,dip,time)
#print(processed)
y.write(processed)
x.close()
