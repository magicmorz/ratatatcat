import yaml


if __name__ == '__main__':
    with open("config.yaml", "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)