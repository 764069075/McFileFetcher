from utils.configUtils import config
import builtins


original_print = builtins.print

def custom_print(*args, **kwargs):
    new_args = (config['PRINT_PREFIX'] + " ".join(map(str, args)) + config['PRINT_SUFFIX'],)
    original_print(*new_args, **kwargs)

builtins.print = custom_print