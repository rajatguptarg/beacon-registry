from binascii import unhexlify


class Beacon(object):
    """
    Beacon Details
    """

    def __init__(self, form):
        self.beacon_name = form.get('name')
        self.beacon_type = form.get('type')
        self.status = form.get('status')
        self.description = form.get('description')
        self.indoorlevel_name = form.get('indoorlevel_name')
        self.expected_stability = form.get('expected_stability')
        self.position = form.get('position')
        self.place_id = form.get('place_id')
        self.msg = str(form.get('msg')).strip()
        self.namespace = form.get('namespace')

    def registration_request_body(self):
        """
        Return the request body in json format
        """
        advertise_id = self.advertised_id()
        body = {
            "advertisedId": {
                "type": "EDDYSTONE",
                "id": advertise_id
            },
            "status": self.status,
            "placeId": self.place_id,
            "indoorLevel": {
                "name": self.indoorlevel_name,
            },
            "expectedStability": self.expected_stability,
            "description": self.description,
            "properties": self.properties,
        }
        return body

    def update_request_body(self, form):
        """
        Return request body to update beacon
        """
        body = {
            "beaconName": form.get('beaconName'),
            "description": form.get('description'),
            "advertisedId": form.get('advertisedId'),
            "status": form.get('status'),
            "expectedStability": form.get('expectedStability'),
            "properties": form.get('properties'),
        }
        return body

    def attachment_request_body(self):
        """
        Return the request body in json format
        """
        body = {
            "namespacedType": self.namespace,
            "data": (self.msg).encode('base64', 'strict').strip()
        }
        return body

    def long_to_bytes(self, value, endianness='big'):
        """
        Convert hexadecimal into byte array
        """
        width = value.bit_length()
        width += 8 - ((width % 8) or 8)
        fmt = '%%0%dx' % (width // 4)
        s = unhexlify(fmt % value)

        if endianness == 'little':
            s = s[::-1]

        return s

    def advertised_id(self):
        """
        Return advertised id
        """
        pass

    @property
    def properties(self):
        """
        Return properties
        """
        return dict()

    def __repr__(self):
        if self.beacon_name:
            return 'Beacon Name: ' + str(self.beacon_name)
        else:
            return 'Advertised Id: ' + str(self.advertised_id())
