import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("this is testing env")
            print(f"testing ip {env['test']}")
        elif "dev" in env:
            print("this is dev env")
            print(f"testing ip {env['dev']}")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))