"""Exact supplementary verification of examples from the family in paper.pdf.

Requires only Python 3's standard library. The paper proves the assertions
for every nonnegative integer r; these finite checks supplement that proof.
"""
import json
from math import prod


def product(exponents):
    coefficients = [1]
    for exponent in exponents:
        result = coefficients + [0] * exponent
        for i, value in enumerate(coefficients):
            result[i + exponent] -= value
        coefficients = result
    return coefficients


def verify_family_member(r):
    assert isinstance(r, int) and r >= 0
    m = 30 * r + 28
    first_exponent = 10 * m - 3
    numerator_exponents = list(range(first_exponent, first_exponent + 4))
    denominator_exponents = [10, 2 * m, (10 * m - 1) // 3, 5 * m - 1]
    assert (10 * m - 1) % 3 == 0
    assert len(set(denominator_exponents)) == 4
    n, N = first_exponent - 1, first_exponent + 3
    assert all(1 <= w <= n for w in denominator_exponents)
    expected_degree = 890 * r + 816
    assert sum(numerator_exponents) - sum(denominator_exponents) == expected_degree
    valuations = {
        d: sum(a % d == 0 for a in numerator_exponents)
        - sum(b % d == 0 for b in denominator_exponents)
        for d in range(1, N + 1)
    }
    assert min(valuations.values()) >= 0
    numerator = product(numerator_exponents)
    denominator = product(denominator_exponents)

    # Formal reciprocal of the denominator, through the numerator degree.
    quotient = [1] + [0] * (len(numerator) - 1)
    for weight in denominator_exponents:
        for degree in range(weight, len(quotient)):
            quotient[degree] += quotient[degree - weight]
    assert quotient[first_exponent] == 0
    for exponent in numerator_exponents:
        for degree in range(len(quotient) - 1, exponent - 1, -1):
            quotient[degree] -= quotient[degree - exponent]
    assert all(value == 0 for value in quotient[expected_degree + 1:])
    quotient = quotient[:expected_degree + 1]

    # Full multiplication checks all coefficients, not just the negative term.
    reconstructed = [0] * (len(quotient) + len(denominator) - 1)
    for j, b in enumerate(denominator):
        if not b:
            continue
        for i, a in enumerate(quotient):
            reconstructed[i + j] += a * b
    assert reconstructed == numerator
    assert quotient[first_exponent] == -1 and quotient[-1] == 1
    assert all(value >= 0 for value in quotient[:first_exponent])
    assert quotient == quotient[::-1]
    negatives = {i: value for i, value in enumerate(quotient) if value < 0}
    assert sum(quotient) * prod(denominator_exponents) == prod(numerator_exponents)

    # Verify the original positive sequence in Stanton's statement.
    exponents = [1 + (i in denominator_exponents) for i in range(1, n + 1)]
    assert sum(exponents) == N and min(exponents) == 1
    for d, valuation in valuations.items():
        assert N // d - sum(exponents[d - 1::d]) == valuation
    result = {
        'r': r, 'm': m, 'n': n, 'N': N, 'degree': expected_degree,
        'first_negative_exponent': first_exponent, 'coefficient': -1,
        'negative_coefficient_count': len(negatives), 'Q_at_1': sum(quotient),
        'all_cyclotomic_exponents_nonnegative': True,
        'complete_multiply_back': True,
        'original_Stanton_parameters_verified': True,
    }
    if r == 0:
        assert negatives == {277: -1, 287: -1, 297: -1, 519: -1, 529: -1, 539: -1}
        assert sum(quotient) == 831
        result['negative_coefficients'] = negatives
        result['cyclotomic_factors'] = {d: e for d, e in valuations.items() if e}
    return result


def main():
    examples = [verify_family_member(r) for r in (0, 1, 2, 3, 10, 100)]
    print(json.dumps({
        'status': 'PASS',
        'scope': 'Finite exact checks; see the paper for the proof for all r >= 0.',
        'examples': examples,
    }, indent=2))


if __name__ == '__main__':
    main()
