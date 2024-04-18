from multiprocessing import Value
import unittest
from remitly.src.json_verifier import verify_aws_json, read_json_file

class TestVerifyAWSJson(unittest.TestCase):

    def test_json_throws_on_incorrect_json(self):
        self.assertRaises(ValueError, read_json_file, "tests/resources/not_json.json")

    def test_valid_only_asterisk(self):
        js_obj = read_json_file("tests/resources/test_json_valid_1.json")
        self.assertFalse(verify_aws_json(js_obj))

    def test_valid(self):
        js_obj = read_json_file("tests/resources/test_json_valid_2.json")
        self.assertFalse(verify_aws_json(js_obj))
    
    def test_invalid_no_asterisk(self):
        js_obj = read_json_file("tests/resources/test_json_invalid_1.json")
        self.assertTrue(verify_aws_json(js_obj))
    
    def test_invalid_multiple_asterisk(self):
        js_obj = read_json_file("tests/resources/test_json_invalid_2.json")
        self.assertTrue(verify_aws_json(js_obj))
    

    def test_invalid_json_missing_key(self):
        js_obj = {
            "PolicyDocument": {
                "Statement": [
                    {
                        # Missing "Resource" key
                    }
                ]
            }
        }
        self.assertTrue(verify_aws_json(js_obj))

    def test_invalid_json_empty_list(self):
        js_obj = {
            "PolicyDocument": {
                "Statement": []
            }
        }
        self.assertTrue(verify_aws_json(js_obj))

    def test_invalid_json_empty_dict(self):
        js_obj = {}
        self.assertTrue(verify_aws_json(js_obj))
    

if __name__ == '__main__':
    unittest.main()