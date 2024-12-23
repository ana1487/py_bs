def collatz_chain_length(n, memo):
    """Calculate the Collatz chain length of n using memoization."""
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 1

    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1

    length = 1 + collatz_chain_length(next_n, memo)
    memo[n] = length
    return length


def longest_collatz_chain(limit):
    """Find the starting number under `limit` that produces the longest Collatz chain."""
    longest_chain = 0
    starting_number = 0
    memo = {}

    for i in range(1, limit):
        current_chain = collatz_chain_length(i, memo)
        if current_chain > longest_chain:
            longest_chain = current_chain
            starting_number = i

    return starting_number, longest_chain


if __name__ == "__main__":
    limit = 1_000_000
    starting_number, longest_chain = longest_collatz_chain(limit)
    print(f"The starting number under {limit} that produces the longest chain is {starting_number}.")
    print(f"The length of this chain is {longest_chain}.")
