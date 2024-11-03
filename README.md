## Heterogeneity in FL
This repository contains the distributed implementation for federated learning algorithm under data sets that are heterogeneous. The algorithm is published in the paper titled 'Federated Learning Games for Reconfigurable Intelligent Surfaces via Causal Representations' (https://ieeexplore.ieee.org/document/10437657). 

Follow instructions given below to run the distributed implementation. The server and client can be run on different hardware

## Server
### dependencies

1. [numpy](https://numpy.org/install/) (pip install numpy)  
2. [scikit-learn](https://scikit-learn.org/stable/install.html) (pip install scikit-learn)
3. [pytorch](https://pytorch.org/) 2.0 or latest
4. [websockets](https://websockets.readthedocs.io/en/stable/intro/index.html#installation) (pip install websockets)
5. [torchvision](https://pypi.org/project/torchvision/)
6. [bson](https://pypi.org/project/bson/) (pip install bson)
7. [tqdm](https://pypi.org/project/tqdm/) (pip install tqdm)

Download Server code and run *wbsocket_server.py*. 

**The data to be tested against for calculating test accuracy during training should be stored in a subfolder in _./data_ folder.** 

### dependencies

1. [pytorch](https://pytorch.org/) 2.0 or latest
2. [websockets](https://websockets.readthedocs.io/en/stable/intro/index.html#installation) (pip install websockets)
3. [torchvision](https://pypi.org/project/torchvision/)
4. [numpy](https://numpy.org/install/) (pip install numpy)  
5. [scikit-learn](https://scikit-learn.org/stable/install.html) (pip install scikit-learn)

run *python client_service.py 5000* (or any number for port) on the client device

**The data to train the model should be stored in a subfolder in _./data_ folder.** 

Once server and the clients are running on dedicated hardware, the request for running the FL task can be initiated by running the *start_fl.py* program. This can be run on any hardware. Install follwing dependencies to run this file.

1. [numpy](https://numpy.org/install/) (pip install numpy)  
2. [websockets](https://websockets.readthedocs.io/en/stable/intro/index.html#installation) (pip install websockets)
3. [matplotlib](https://matplotlib.org/stable/install/index.html)