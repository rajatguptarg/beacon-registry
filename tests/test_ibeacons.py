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

    def test_0020_advertised_id_with_major_1468_minor_44776(self):
        self.beacon_data["major"] = "1468"
        self.beacon_data["minor"] = "44776"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9byu6A==")

    def test_0030_advertised_id_with_major_21425_minor_1020(self):
        self.beacon_data["major"] = "21425"
        self.beacon_data["minor"] = "1020"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9TsT/A==")

    def test_0040_advertised_id_with_major_1060_minor_46978(self):
        self.beacon_data["major"] = "1060"
        self.beacon_data["minor"] = "46978"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9CS3gg==")

    def test_0050_advertised_id_with_major_24924_minor_1012(self):
        self.beacon_data["major"] = "24924"
        self.beacon_data["minor"] = "1012"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9hXD9A==")

    def test_0060_advertised_id_with_major_24924_minor_1289(self):
        self.beacon_data["major"] = "24924"
        self.beacon_data["minor"] = "1289"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9hXFCQ==")

    def test_0070_advertised_id_with_major_21425_minor_1425(self):
        self.beacon_data["major"] = "21425"
        self.beacon_data["minor"] = "1425"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "C5QH8wJVVrV/5t//9TsVkQ==")

    def test_0080_advertised_id_with_major_26968_minor_4582(self):
        self.beacon_data["major"] = "26968"
        self.beacon_data["minor"] = "4582"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//aVgR5g==")

    def test_0090_advertised_id_with_major_15536_minor_56178(self):
        self.beacon_data["major"] = "15536"
        self.beacon_data["minor"] = "56178"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//PLDbcg==")

    def test_0100_advertised_id_with_major_21425_minor_5309(self):
        self.beacon_data["major"] = "21425"
        self.beacon_data["minor"] = "5309"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//U7EUvQ==")

    def test_0110_advertised_id_with_major_50206_minor_57048(self):
        self.beacon_data["major"] = "50206"
        self.beacon_data["minor"] = "57048"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//xB7e2A==")

    def test_0120_advertised_id_with_major_26968_minor_4203(self):
        self.beacon_data["major"] = "26968"
        self.beacon_data["minor"] = "4203"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//aVgQaw==")

    def test_0130_advertised_id_with_major_26968_minor_4787(self):
        self.beacon_data["major"] = "26968"
        self.beacon_data["minor"] = "4787"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//aVgSsw==")

    def test_0140_advertised_id_with_major_24924_minor_4628(self):
        self.beacon_data["major"] = "24924"
        self.beacon_data["minor"] = "4628"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//YVwSFA==")

    def test_0150_advertised_id_with_major_26968_minor_5423(self):
        self.beacon_data["major"] = "26968"
        self.beacon_data["minor"] = "5423"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//aVgVLw==")

    def test_0160_advertised_id_with_major_64931_minor_51855(self):
        self.beacon_data["major"] = "64931"
        self.beacon_data["minor"] = "51855"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf///aPKjw==")

    def test_0170_advertised_id_with_major_15536_minor_13644(self):
        self.beacon_data["major"] = "15536"
        self.beacon_data["minor"] = "13644"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//PLA1TA==")

    def test_0180_advertised_id_with_major_21425_minor_4612(self):
        self.beacon_data["major"] = "21425"
        self.beacon_data["minor"] = "4612"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//U7ESBA==")

    def test_0190_advertised_id_with_major_21425_minor_5825(self):
        self.beacon_data["major"] = "21425"
        self.beacon_data["minor"] = "5825"
        beacon = IBeacon(self.beacon_data)
        self.assertEqual(beacon.advertised_id(), "uUB/MCVVa1f+bf//U7EWwQ==")
