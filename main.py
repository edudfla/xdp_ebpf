#!/usr/bin/env python3

#
# sudo apt-get install linux-tools-virtual -y
# sudo apt-get install linux-headers-5.4.0-54-generic -y
#
# FileNotFoundError: [Errno 2] No such file or directory: '/sys/kernel/debug/tracing/trace_pipe'
# https://github.com/iovisor/bcc/issues/1878#issuecomment-403284169
# sudo mount -t debugfs debugfs /sys/kernel/debug
#
from bcc import BPF
import time

device = "lo"
b = BPF(src_file = "filter.c")
fn = b.load_func("updfilter", BPF.XDP)
b.attach_xdp(device, fn, 0)
try:
    b.trace_print()
except KeyboardInterrupt:
    pass

b.remove_xdp(device, 0)
