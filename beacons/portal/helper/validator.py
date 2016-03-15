class Validator(object):
    """
    Validates the request data
    """

    @staticmethod
    def valid(beacon_info):
        """
        Returns whether Info is Valid or Not
        """
        if beacon_info.get('uuid') is None or \
                beacon_info.get('major') is None or \
                beacon_info.get('minor') is None:
            return False

        if len(beacon_info.get('uuid')) == 36 and \
                not len(beacon_info.get('major')) == 0 and \
                not len(beacon_info.get('minor')) == 0:
            return True

        return False
