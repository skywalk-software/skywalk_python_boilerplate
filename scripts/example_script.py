from skywalk_example import load_config, example_function


def main():
    config = load_config()
    print(f"API Key: {config['API_KEY']}")

    result = example_function(5, 7)
    print(f"5 + 7 = {result}")


if __name__ == "__main__":
    main()
