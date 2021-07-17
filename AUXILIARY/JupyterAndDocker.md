# How to setup Docker for usage with Jupyter

## Installing Docker
For this tutorial we will use the containerized version of VOTCA. It is provided as a docker container.

To install docker

```bash
sudo apt install docker.io
```

Note that this is no longer the recommended way to install Docker, but it is the quickest, for the up to date install instructions see [Docker's website](https://docs.docker.com/engine/install/).

## Getting the Docker image
```bash
sudo docker pull votca/votca
```

## Setting up Jupyter
If you want to use a jupyter notebook inside the container we need some special options. To start the docker container

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
cd xtp-tutorials/<pathToTutorial>
```

Load the VOTCA environment variables

```bash
source VOTCARC.bash
```

and start jupyter. We need to pass some special options to make it work with the docker container and the host browser

```bash
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

Now navigate to [http://localhost:8888/tree](http://localhost:8888/tree) in your browser. Jupyter will ask you for a token, you can copy the token from one of the urls that appeared in your terminal, i.e. the part after `?token=`.

Now that we have setup jupyter correctly we can open the jupyter notebooks.