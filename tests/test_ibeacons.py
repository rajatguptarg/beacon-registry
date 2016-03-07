import unittest
from beacons.portal.models import IBeacon


class TestIBeacon(unittest.TestCase):
    """
    Test Suites for IBeacons
    """
    def setUp(self):
        """
        IBeacons Setup for tests
        """
        self.beacon_data = {
            "uuid": "B9407F30-F5F8-466E-AFF9-25556B57FE6D",
            "major": "64931",
            "minor": "59274"
        }

    def test_000_test_assertion(self):
        """
        Just to test tests
        """
        self.assertEqual(200, 200)

    def test_0010_advertised_id_with_major_64931_minor_59274(self):
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf///aPnig==")

    def test_0010_advertised_id_with_major_1468_minor_44776(self):
        self.beacon_data["major"] = "1468"
        self.beacon_data["minor"] = "44776"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9byu6A==")
