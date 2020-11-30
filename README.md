# xdp_ebpf
Small test over article [Primer: How XDP and eBPF Speed Network Traffic via the Linux Kernel](https://thenewstack.io/primer-how-xdp-and-ebpf-speed-network-traffic-via-the-linux-kernel/) by [Jack Wallen](https://github.com/jlwallen).

It was checked with WSL2.

Unforeseen things found during tests:
1. The python pip module was not installed. Had to install it:
```sudo apt-get install -y python3-pip```
2. The command ```uname -r``` in WSL2 return value is not suitable to install linux-tools and linux-headers. Guessed it: ```sudo apt-get install linux-headers-5.4.0-54-generic -y``` and ```sudo apt-get install linux-tools-virtual -y```. Also, created a symbolic link (```sudo ln -s 5.4.0-54-generic 4.19.128-microsoft-standard```) in directory "/lib/modules". ("4.19.128-microsoft-standard" is the output of command ```uname -r```).
3. The debugfs needs to be mounted (https://github.com/iovisor/bcc/issues/1878#issuecomment-403284169): ```sudo mount -t debugfs debugfs /sys/kernel/debug```.
4. For some reason I don't know why, the source code in the [article](https://thenewstack.io/primer-how-xdp-and-ebpf-speed-network-traffic-via-the-linux-kernel/) shows ill-formated in my browser.
