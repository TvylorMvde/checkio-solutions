class RouteSummarization:

    def __init__(self, addresses: list):
        self.addresses = addresses

    def get_addresses_in_binary(self):
        self.addresses_binary = []
        for address in self.addresses:
            binary = ['{:08b}'.format(int(x)) for x in address.split(".")]
            if len(binary) == 4:
                self.addresses_binary.append("".join(binary))
        return self.addresses_binary

    def get_common_bits(self):
        addresses_binary = self.get_addresses_in_binary()
        addresses = sorted(addresses_binary)
        result = ""
        for i in range(len(addresses[0])):
            if addresses[0][i] == addresses[-1][i]:
                result += addresses[0][i]
            else:
                break
        return result

    def generate_summary_route(self):
        common_b = self.get_common_bits()
        ip_binary = common_b + "".join([str(0) for i in range(32 - len(common_b))])
        ip_dec = [str(int(ip_binary[i:i + 8], 2)) for i in range(0, len(ip_binary), 8)]
        return ".".join(ip_dec) + "/" + str(len(common_b))

        
if __name__ == '__main__':

    route1 = RouteSummarization(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"])
    route2 = RouteSummarization(["172.16.12.0", "172.16.13.0", "172.155.43.9"])
    route3 = RouteSummarization(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"])

    assert (route1.generate_summary_route() == "172.16.12.0/22"), "First Test"
    assert (route2.generate_summary_route() == "172.0.0.0/8"), "Second Test"
    assert (route3.generate_summary_route() == "128.0.0.0/2"), "Third Test"






    

    

