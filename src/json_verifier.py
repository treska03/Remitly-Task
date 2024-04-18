import json
from typing import Any, Dict

def verify_aws_json(js_obj : Dict[str, Any]) -> bool:
    """
    ```js_obj``` - json object containing AWS::IAM::Role Policy data.

    Example input data:
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html#aws-properties-iam-role-policy--examples

    Returns False if an input JSON Resource field contains a single asterisk.
    Otherwise True. In case of invalidly formatted input, also returns True.
    If input is not a valid JSON, raises ValueError.
    """
    try:
        resource = js_obj["PolicyDocument"]["Statement"][0]["Resource"]
    except (KeyError, IndexError, TypeError):
        return True
    except Exception as e:
        raise e
    return resource.count("*") != 1

def read_json_file(path : str) -> Dict[str, Any]:
    """
    @params:
    """
    with open(path, "r") as f:
        return json.load(f)