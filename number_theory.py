from typing import List
import math
import time
from local_logger import log, LogLevel

def get_first_divisor_or_prime(N):
    """
    Returns the first odd divisor 'i' if N is composite, or N itself if prime.
    Assumes N is odd.
    """
    if N % 2 == 0:
        # Should not happen as we iterate only odd numbers
        return 2
    for i in range(3, int(math.sqrt(N)) + 1 ,2):
        if N % i == 0:
            return i
    return N # N is prime

def generate_shosho_list_final(limit: int) -> List[int]:
    """
    Sequentially generates the flattened list based on the derived rules:
    - Prime p: Count is (p - 1) / 2.
    - Composite c: Count is (first_prime_divisor(c) - 1) / 2.
    """
    final_list: List[int] = [2]
    
    # We iterate through odd numbers starting from 3 up to the limit
    for num in range(3, limit + 1, 2):
        # A will be either 'num' (if prime) or the first odd divisor (if composite)
        A = get_first_divisor_or_prime(num) 
        repeat_count = 0
        if num == A: 
            # 1. PRIME RULE: A is the number itself. Count = (num - 1) / 2
            repeat_count = (num - 1) // 2
        else:
            # 2. COMPOSITE RULE: A is the first odd divisor. Count = (A - 1) / 2
            # int((A/2) - 0.5) is mathematically equivalent to (A - 1) // 2
            repeat_count = (A - 1) // 2
            
        final_list.extend([num] * repeat_count)
            
    return final_list

# --- Original ShoSho Algorithm for Comparison ---

def ShoSho(limit):
    """Generates the list of (number, count) tuples."""
    """Generate base primes up to limit using Sieve of Eratosthenes."""
    L = [(2,1)]
    for i in range(3,limit,2) :
        k=len([x for x in L if x[0]==i])
        for j in L:
            k=k+1
            if i%j[0] == 0:
                break
            
            if L[-1][0] == i:
                L[-1] = (i,k)
            else: 
                L.append((i,k))
    print(L)
    return L 

def expand(L):
    """Flattens the list of (number, count) tuples."""
    M = []
    for i in L:
        for j in range(i[1]):
            M.append(i[0])
    return M

# --- Execution ---

LIMIT = 40
start_time = time.time()
final_result_list = generate_shosho_list_final(LIMIT)
end_time = time.time()

# Check against your expected output:
expected_list = expand(ShoSho(LIMIT))

result = ShoSho(LIMIT)
log(f" All Numbers = {len(result)}",LogLevel.CRITICAL)
log(result)
A = [x for x in result if (x[1] > 1 and x[0] == 2*x[1]+1 ) or x[0]  in [2,3]]
log(f" Primes Counts = {len(A)}" , LogLevel.CRITICAL)
#log(A)
B = [x[0] for x in result if (x[1] > 1 and x[0] == 2*x[1]+1) or x[0]  in [2,3] ]
log(f" Primes = {len(B)}", LogLevel.CRITICAL)
#log(B)
C= [x[0] for x in result if x[0] != 2*x[1]+1 and x[0] not in [2,3] ] 
log(f" Composite = {len(C)} ", LogLevel.CRITICAL)
#log(C)
log(f"Primes Percentage ={round((len(B)/len(result))*100,2)}%" , LogLevel.CRITICAL)

print("\n--- Comparison ---")
print(f"Simplified Generator List Length: {len(final_result_list)}")
print(f"Original Algorithm List Length: {len(expected_list)}")
print(f"Time for Simplified Generator: {end_time - start_time:.4f} seconds")

# print(final_result_list)
# print(expected_list)

if final_result_list == expected_list:
    print("\n✅ SUCCESS: The simplified sequential generator now exactly matches the original algorithm's output!")
else:
    print("\n❌ MISMATCH: The generated lists DO NOT match.")
    # Debugging helper
    min_len = min(len(final_result_list), len(expected_list))
    for i in range(min_len):
        if final_result_list[i] != expected_list[i]:
            print(f"Deviation at index {i}: Simplified={final_result_list[i]}, Expected={expected_list[i]}")
            break
    if len(final_result_list) != len(expected_list):
        print(f"List lengths differ: Simplified={len(final_result_list)}, Expected={len(expected_list)}")