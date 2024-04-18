from src.json_verifier import verify_aws_json, read_json_file

def main():
    # read_json_file(path)
    result = verify_aws_json("")

    print(result)
    
    return result

if __name__ == "__main__":
    main()