# About
TODO

# Services
TODO

## Docker Manager
### About 
This is a simple service to provide endpoints for managing the host docker instance.

### Enable
```bash
cd docker_manager
chmod +x setup.sh
sudo ./setup.sh
```

# Setup

## Prerequisits
- Dock and Docker-compose setup and ready
- Porta specified in ```docker-compose.yaml```
## Customize
- Modify ```.env.example``` and rename to ```.env```
- Modify ```basicauth/usersfile.example``` and rename to ```basicauth/usersfile```

## Start
- Run ```docker compose up -d```
