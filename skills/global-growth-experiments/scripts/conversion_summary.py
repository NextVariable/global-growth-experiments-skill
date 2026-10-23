#!/usr/bin/env python3
"""Describe two binary-count groups; do not decide experimental winners.

Wilson score intervals, 95%, z=1.959963984540054. Independent Bernoulli
observations are assumed within each group. Separate intervals are not a
confidence interval or significance test for the difference.
"""

import argparse
import json
import math

Z95 = 1.959963984540054


def group_summary(successes, total):
    if type(successes) is not int or type(total) is not int:
        raise ValueError("successes and total must be integers")
    if total <= 0 or successes < 0 or successes > total:
        raise ValueError("require total > 0 and 0 <= successes <= total")
    if total > 10**12:
        raise ValueError("total exceeds the supported count range (10^12)")
    rate = successes / total
    z2 = Z95**2
    denominator = 1 + z2 / total
    center = (rate + z2 / (2 * total)) / denominator
    half = Z95 * math.sqrt(rate * (1 - rate) / total + z2 / (4 * total**2)) / denominator
    return {
        "successes": successes,
        "total": total,
        "rate": rate,
        "wilson_95": [max(0.0, center - half), min(1.0, center + half)],
    }


def summarize(control_successes, control_total, variant_successes, variant_total):
    control = group_summary(control_successes, control_total)
    variant = group_summary(variant_successes, variant_total)
    delta = variant["rate"] - control["rate"]
    return {
        "control": control,
        "variant": variant,
        "difference_percentage_points": 100 * delta,
        "relative_change_percent": 100 * delta / control["rate"] if control["rate"] else None,
        "interpretation": "Descriptive only. No causal claim or winner decision. Separate group intervals are not a test of the difference.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", nargs=2, type=int, metavar=("SUCCESSES", "TOTAL"), required=True)
    parser.add_argument("--variant", nargs=2, type=int, metavar=("SUCCESSES", "TOTAL"), required=True)
    args = parser.parse_args()
    try:
        result = summarize(*args.control, *args.variant)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
