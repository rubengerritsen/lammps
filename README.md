# Tutorial Setup

## Setting up Docker
For this tutorial we will use the containerized version of VOTCA. It is provided as a docker container.

To install docker

```bash
sudo apt install docker.io
```

Note that this is no longer the recommended way to install Docker, but it is the quickest, for the up to date install instructions see [Docker's website](https://docs.docker.com/engine/install/).

## Getting the Docker image
```bash
docker pull votca/votca
```

## Setting up Jupyter
For the tutorial we will use a jupyter notebook. To start the docker container

```bash
sudo docker run -it -p 8888:8888 votca/votca /bin/bash
```

* `-it` Allocate a pseudo-tty and keep STDIN open even if not attached
* `-p` pass the 8888 port of the docker container to the 8888 port of the host, needed to use jupyter in your browser.

Next we need to install `jupyter` in the docker container

```bash
pip3 install jupyter
```

## Starting the tutorial
Navigate to the tutorial

```bash
cd xtp-tutorials/LAMMPS/Thiophene
```

From that directory we run jupyter. We need to pass some special options to make it work with the docker container and the host browser

```bash
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

Now navigate to [http://localhost:8888/tree](http://localhost:8888/tree) in your browser and open the `QMMM_LAMMPS.ipynb`