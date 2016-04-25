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

    def test_0020_advertised_id_with_major_50206_minor_57048(self):
        self.beacon_data["major"] = "50206"
        self.beacon_data["minor"] = "57048"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//xB7e2A==")

    def test_0030_advertised_id_with_major_64931_minor_51855(self):
        self.beacon_data["major"] = "64931"
        self.beacon_data["minor"] = "51855"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf///aPKjw==")

    def test_0040_advertised_id_with_major_1600_minor_5825(self):
        self.beacon_data["major"] = "1600"
        self.beacon_data["minor"] = "5825"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t////ZAFsE=")

    def test_0050_advertised_id_with_major_1600_minor_58256(self):
        self.beacon_data["major"] = "1600"
        self.beacon_data["minor"] = "58256"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t////ZA45A=")

    def test_0050_advertised_id_with_major_1600_minor_582567(self):
        self.beacon_data["major"] = "1600"
        self.beacon_data["minor"] = "582567"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf///2QI46c=")

    def test_0060_advertised_id_with_major_1600_minor_5(self):
        self.beacon_data["major"] = "1600"
        self.beacon_data["minor"] = "5"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//////ZAU=")
