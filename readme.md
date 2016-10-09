# OSDNA

## Run

```bash                        
./run.sh
```

## Build
  
```bash
meteor build --architecture=os.linux.x86_64 ./
```
  
## Testing - Build with Docker 
  
Testing on staging

```bash
docker run -d \
    -e ROOT_URL=http://testing-server-example.com \
    -e MONGO_URL=mongodb://testing-server-example.com:27017/osdna \
    -v /home/ofir/osdna:/bundle \
    -p 80:80 \
    kadirahq/meteord:base
```

Testing on local

```bash
docker run \
   --net=host \
   -e ROOT_URL=http://localhost \
   -e MONGO_URL=mongodb://localhost:27017/osdna \
   -v /home/eyal_work/projects/cisco/output:/bundle \
   kadirahq/meteord:base
```

