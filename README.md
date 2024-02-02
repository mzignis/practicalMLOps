# practicalMLOps

## Setup environment

### Install and activate venv
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install requirements
```bash
make install
```

## ssh-key agent
```bash
eval "$(ssh-agent -s)" 
ssh-add ~/.ssh/id_rsa_priv
```

## ToDo:
- [x] Use AWS Code Build
- [x] Dockerize the app
- [ ] Use AWS Elastic Container Registry (ECR)