import toml
import importlib
import argparse
import os

class CLITool:
    def __init__(self):
        toml_path = os.path.join(os.path.dirname(__file__), "options.toml")
        with open(toml_path, 'r') as file:
            self.options = toml.load(file)

    def execute(self, feature, args):
        if feature not in self.options:
            print(f"Feature '{feature}' not found in options.toml")
            return

        feature_data = self.options[feature]
        function_location = feature_data["function_location"]
        input_values = feature_data["input_values"]

        module_name, func_name = function_location.rsplit(".", 1)
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)

        parser = argparse.ArgumentParser()
        for arg in input_values:
            parser.add_argument(f"--{arg}", required=True)
        parsed_args = vars(parser.parse_args(args))

        func(**parsed_args)
