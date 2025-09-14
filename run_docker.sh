mkdir -p my_solutions
chmod 777 my_solutions #xD
docker run --rm -it -v "$(pwd)/my_solutions:/home/student/my_solutions" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined binexp_workshop:latest
