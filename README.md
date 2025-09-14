# binexp_workshop
Linux binexp fundamentals workshop made for those new to the binexp but not necessary new to the field. Understanding of C code and being comfortable with computers and terminal are required ;]

This has been initially planned as in-person workshop lasting one day, hence lots of simplifications on slides.

# getting there
1. clone this repo:
```
git clone https://github.com/mblzk/binexp_workshop
``` 
2. build the Docker image
```
sudo docker build . -t binexp_workshop:latest
```
3. run the container with
```
sudo run_docker.sh
```
4. your work is available through `./my_solutions` folder. It's advisable to copy files you are working with here as containers are ephemereal (you WILL lose everything on exit).
5. have fun and send me any improvements ideas

# known issues
- Addressess hardcoded in the solutions tend to differ between machines. Hopefully using docker fixes it but if my solutions crash at your machine, you'll need to obtain the return addressess yourself. Good luck!
- Not all labs are finished yet. There are mentions of labs 6 and 7 in slides which are actually not there. That's intended and I am working on it.

# TODO
1. Add ROP labs
2. Add ASLR labs
3. Prepare content on RELRO and GOT overwrites
4. Make some content about linux's heap exploitation
5. Add some final challenges with all mitigations enabled and additional logic
6. Add some linux-specific stuff (e.g. env vars)
