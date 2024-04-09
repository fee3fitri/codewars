'''
The tower of Hanoi is a famous puzzle where we have three rods and N disks. 
The objective of the puzzle is to move the entire stack to another rod. 
You are given the number of discs N. Initially, these discs are in the rod 1. 
You need to print all the steps of discs movement so that all the discs reach the 3rd rod. 
Also, you need to find the total moves.


Note: 
The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. 
Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc.

EXAMPLE: 
For Input (N = 2) 
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3 
'''

def toh(N, fromm, to, aux):
  count = 0
  
  def helper(N, fromm, to, aux):
    nonlocal count
    
    if N == 1:
      count += 1
      print(f"move disk {str(N)} from rod {str(fromm)} to rod {str(to)}")
      return
      
    helper(N - 1, fromm, aux, to)
    print(f"move disk {str(N)} from rod {str(fromm)} to rod {str(to)}")
    count += 1
    helper(N - 1, aux, to, fromm)
    
  helper(N, fromm, to, aux)
  return count

def toh_tail_recursive(N, source, destination, auxiliary):
    """Tail-recursive solution to the Tower of Hanoi problem."""
    count = 0
    def helper(N, source, destination, auxiliary):
        nonlocal count
        if N >= 1:  
            helper(N-1, source, auxiliary, destination)
            print(f"Move disk {N} from rod {source} to rod {destination}")
            count += 1
            helper(N-1, auxiliary, destination, source)  

    helper(N, source, destination, auxiliary)
    return count
  
  
def toh_memoized(N, source, destination, auxiliary):
    memo = {}
    count = 0
    def toh_util(N, source, destination, auxiliary):
        nonlocal count
        if N == 1:
            print(f"Move disk 1 from rod {source} to rod {destination}")
            count += 1
            return

        key = (N, source, destination)
        if key not in memo:
            toh_util(N - 1, source, auxiliary, destination)
            print(f"Move disk {N} from rod {source} to rod {destination}")
            count += 1
            toh_util(N - 1, auxiliary, destination, source)
            memo[key] = None  # We only need to memoize that this calculation has been done
        
    toh_util(N, source, destination, auxiliary)
    return count

# Example usage:
print(toh_tail_recursive(3, 1, 3, 2))
print(toh_memoized(3, 1, 3, 2))
print(toh(3, 1, 3, 2))
