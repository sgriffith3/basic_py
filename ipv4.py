#!/usr/bin/env python3
'''
IPv4 Checker

Takes an IPv4 address and verifies that it falls within appropriate IP specs
'''


def ipv4(ip_address):
    check_ip = ip_address.split('.')
    fail = False
    if len(check_ip) != 4:
        fail = True
    for i in check_ip:
        if int(i) in range(1,256):
            check_ip.pop(-1)
            break
        else:
            fail = True
    for a in check_ip:
        if int(a) in range(256):
            pass
        else:
            fail = True
            break
    if fail == True:
        print("That's not a valid IPv4 address")
