import os

workdir = "c:\\paal\\git\\listservice\\"
os.chdir(workdir)

df = open('list.txt', 'r')
dataset = df.readlines()
#df.close

#print(len(dataset))

# strip, split, rstrip

def servers():
    servers = []
    for i in dataset:
        if i.startswith("hostname"):
            servers.append(i[9:22].rstrip())
        else:
            None
    return servers    

def index():
    index = []
    for i in range(60060,60070):
        index.append(i)
    #for i in range(65000,65100):
    #    index.append(i)
    return index


def ports():
    ports = []
    for i in dataset:
        if i.startswith("hostname"):
            None
        else:
            #print(i[:5])
            ports.append(i[:5].rstrip())
    return ports


def pids():
    pids = []
    for i in dataset:
        if i.startswith("hostname"):
            None
        else:
            pids.append(i[42:48].rstrip())
    return pids

def services():
    services = []
    for i in dataset:
        #if i[:8]  == "hostname":
        if i.startswith("hostname"):
            None
        else:
            services.append(i[11:40].rstrip())
    return services

def configs():
    configs = []
    for i in dataset:
        #if i[:8]  == "hostname":
        if i.startswith("hostname"):
            None
        else:
            configs.append(i[73:].rsplit('-i')[0])
    return configs

def index():
    indexlist = []
    makeindexlist = index()
    for i in makeindexlist:
        indexlist.append(int(i))
    print(indexlist)


def uniqueindex(): # Unique ports - 
    sort = ports()
    unique_list = []

    for x in sort:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


if __name__ == '__main__':
    #print(servers())
    #print(makeindex())
    print(ports())
    #print(pids())
    #print(services())
    #print(configs())
    print(uniqueindex())

