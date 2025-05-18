from d_sdlt_rates import sdlt_rates
from cls_helper_sys import SysHelper

sys_helper = SysHelper()

def print_sdlt_rates(stream=sys_helper.stdout) -> None:
    for key, sdlt_rate in sorted(sdlt_rates.items()):
        print(f"=== SDLT Rates: {key} ===", file=stream)
        print(sdlt_rate.details(), file=stream)
        print("=" * 40, file=stream)
        print(file=stream)

    print(
        "Note: SDLT rates are subject to change. Always check the latest government guidelines.",
        file=stream,
    )
    print(
        "https://www.gov.uk/stamp-duty-land-tax/residential-property-rates", file=stream
    )


if __name__ == "__main__":
    print_sdlt_rates()
