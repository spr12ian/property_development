from d_developments import developments
from cls_helper_sys import SysHelper

sys_helper = SysHelper()

def print_developments(stream=sys_helper.stdout) -> None:
    for key, development in sorted(developments.items()):
        print(f"=== Development: {key} ===", file=stream)
        print(development.details(), file=stream)
        print("=" * 40, file=stream)
        print(file=stream)


if __name__ == "__main__":
    print_developments()
