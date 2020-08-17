from configparser import ConfigParser


class Option:
    def write_pycharm(self, config_parser: ConfigParser, section: str):
        raise NotImplementedError

    def read_pycharm(self, config_parser: ConfigParser, section: str):
        pass


class KeyValueOption(Option):
    pass