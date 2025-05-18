from d_dwellings import dwellings
from cls_helper_sys import SysHelper

sys_helper = SysHelper()


def print_properties(stream=sys_helper.stdout) -> None:
    for key, dwelling in sorted(dwellings.items()):
        print(f"=== Dwelling: {key} ===", file=stream)
        print(dwelling.details(), file=stream)
        print("=" * 40, file=stream)
        print(file=stream)


if __name__ == "__main__":
    print_properties()
