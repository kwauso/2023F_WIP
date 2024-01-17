#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{
 int sock;
 struct sockaddr_in addr;
 in_addr_t ipaddr;

 sock = socket(AF_INET, SOCK_DGRAM, 0);

 addr.sin_family = AF_INET;
 addr.sin_port = htons(12345);
 addr.sin_addr.s_addr = inet_addr("224.0.0.1");

 ipaddr = inet_addr("127.0.0.1");
 if (setsockopt(sock,
		IPPROTO_IP,
		IP_MULTICAST_IF,
		(char *)&ipaddr, sizeof(ipaddr)) != 0) {
	perror("setsockopt");
	return 1;
 }

 sendto(sock, "HELLO, World!", 13, 0, (struct sockaddr *)&addr, sizeof(addr));

 close(sock);

 return 0;
}
