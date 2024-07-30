# BK Skip

BK Skip is a tool to skip the anoying Burger King survey located at [minhabkexperiencia.com](http://minhabkexperiencia.com/).

## Installation on CasaOS
To self host this tool on CasaOS, you need to build the docker image on your machine:
```bash
# Clone the repository
git clone https://github.com/JCionx/bk-skip

# Build the docker image
docker build -t bk-skip .
```

Now transfer the image to your CasaOS server and load the image there:
```bash
docker load < bk-skip.tar
```

After that, go to the CasaOS UI, click the **+** and then **Install a customized app**, then click on the **Import** icon at the top, and choose the compose.yaml file of this repo.