#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/socket.h>

int main(int argc, char* argv[]) {

    if (argc != 2) {
        fprintf(stderr, "Usage: %s port\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int sv[2];

    socketpair(atoi(argv[1]), SOCK_STREAM, 0, sv);

    int status;
    pid_t pid = fork();

    if(pid == -1) {
        exit(1);
    }
    else if(pid == 0) {
        if(listen(sv[0], 50) == -1)
            perror("listen");

        

    }
    else {
        waitpid(pid, &status, 0);
    }




}