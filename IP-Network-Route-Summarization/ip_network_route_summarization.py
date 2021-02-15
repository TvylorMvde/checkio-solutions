def checkio(addresses):
    addresses_in_binary = convert_addresses_to_binary(addresses)
    common_b = find_common_bits(addresses_in_binary)
    return generate_new_address(common_b)


def convert_addresses_to_binary(addresses):
    addresses_in_binary = []
    for address in addresses:
        binary = ['{:08b}'.format(int(x)) for x in address.split(".")]
        if len(binary) == 4:
            addresses_in_binary.append("".join(binary))
    return addresses_in_binary


def find_common_bits(addresses):
    addresses = sorted(addresses)
    result = ""
    for i in range(len(addresses[0])):
        if addresses[0][i] == addresses[-1][i]:
            result += addresses[0][i]
        else:
            break
    return result


def generate_new_address(common_b): 
    address = common_b + "".join([str(0) for i in range(32 - len(common_b))])
    new_ip = [str(int(address[i:i + 8], 2)) for i in range(0, len(address), 8)]
    return ".".join(new_ip) + "/" + str(len(common_b))
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"

