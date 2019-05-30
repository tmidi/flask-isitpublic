from __future__ import print_function
import socket
import re
import ipaddress


def is_public(ip):
    return ipaddress.ip_address(ip).is_global


def is_valid_ipv4_address(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(ip)
        except socket.error:
            return {'status': 'danger',
                    'type': 'IPv4',
                    'message': 'is not a valid IPv4 address'}
        return ip.count('.') == 3
    except socket.error:  # not a valid address
        return {'status': 'danger',
                'type': 'IPv4',
                'message': 'is not a valid IPv4 address'}
    if is_public(ip):
        return {'status': 'success',
                'type': 'IPv4',
                'message': 'is a valid IPv4 public address'}
    else:
        return {'status': 'warning',
                'type': 'IPv4',
                'message': 'is a valid IPv4 private address'}


def is_valid_ipv6_address(ip):
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:  # not a valid address
        return {'status': 'danger',
                'type': 'IPv6',
                'message': 'is not a valid IPv6 address'}
    if is_public(ip):
        return {'status': 'success',
                'type': 'IPv6',
                'message': 'is a valid IPv6 public address'}
    else:
        return {'status': 'warning',
                'type': 'IPv6',
                'message': 'is a valid IPv6 private address'}


def netmask(cidr):
    # Regex to represent valid CIDR notation
    # source: gist.github.com/mattselph/9a160e876a62f9b505768f99a39473d4

    valid_ip = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$"

    # verify that the user entered a valid CIDR range
    if not re.match(valid_ip, cidr):
        return {'status': 'danger',
                'type': 'CIDR',
                'message': 'We could not validate the address you entred.'}

    net_bits = int(cidr[cidr.find('/') + 1:])
    num_host_bits = 32 - net_bits
    addr_bits = list(('1' * int(net_bits)).zfill(32))
    addr_bits.reverse()
    host_bits = "".join(addr_bits)
    num_hosts = 2**num_host_bits

    mask_vals = [128, 64, 32, 16, 8, 4, 2, 1]

    # how many full octets do we have
    full_octets = int(net_bits / 8)
    netmask = '255.' * full_octets
    remaining_bits = net_bits - (full_octets * 8)

    if remaining_bits > 0:
        mask = sum(mask_vals[:remaining_bits])
        netmask = netmask + str(mask) + '.'

    netmask = netmask + '0.' * abs((4 - (len(netmask.split('.')) - 1)))

    # chop off the trailing decimal
    netmask = netmask[:-1]

    # return JSON with all this
    d = {'status': 'warning',
         'type': 'CIDR',
         'message': 'valid private CIDR',
         'info': {
             'CIDR': cidr,
             'Netmask': netmask,
             'Netmask Binary': host_bits,
             'Number of hosts': num_hosts,
             'Network Bits': net_bits,
             'Host Bits': num_host_bits,
         },
         }
    if is_public(cidr.split('/')[0]):
        update = {'status': 'success', 'message': 'valid public CIDR'}
        d.update(update)
        return d
    else:
        return d
