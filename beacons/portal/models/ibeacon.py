import base64
from beacons import Beacon


class IBeacon(Beacon):
    """
    iBeacon protocol
    """

    def advertised_id(self):
        """
        Convert uuid, major, minor into advertised id
        """
        namespace = '0x' + self.uuid[:8] + self.uuid[-12:]
        major, minor = map(int, (self.major, self.minor))
        temp_instance = self._append_hex(major, minor)
        instance = self._add_padding(temp_instance)
        beacon_id = self._append_hex(int(namespace, 16), instance)
        return base64.b64encode(self.long_to_bytes(beacon_id))

    def _add_padding(self, instance):
        """
        Append padding of desired size
        """
        bit_length = (len(hex(instance)) - 2) * 4
        desired_padding_size = self.desired_instance_bits - bit_length
        padding = (2 ** desired_padding_size) - 1
        return self._append_hex(padding, instance)

    def _append_hex(self, a, b):
        """
        Append hex number a in front of b
        """
        sizeof_b = 0

        # Count the number of bits in b
        while((b >> sizeof_b) > 0):
            sizeof_b += 1

        # make number of bits perfectly divisible by 4
        sizeof_b += 4 - ((sizeof_b % 4) or 4)

        return (a << sizeof_b) | b

    @property
    def properties(self):
        return {
            "uuid": str(self.uuid),
            "major": str(self.major),
            "minor": str(self.minor)
        }

    def __init__(self, form):
        super(self.__class__, self).__init__(form)
        self.uuid = form.get('uuid')
        self.major = form.get('major')
        self.minor = form.get('minor')
        self.padding = 'f'
        self.desired_instance_bits = 48
