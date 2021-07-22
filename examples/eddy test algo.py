"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/10/2021

Purpose:

Details:

Description:

Notes:

IMPORTANT NOTES:

Explanation:

Reference:

"""
from python_code_recorder.code_recorder import CodeRecorder

tester = CodeRecorder()


@tester.decorator_wrapper_callable
def func(n):
    i = 1

    while i <= n - 2:
        tester.iteration_scope_start("i", i)
        j = i + 1
        while j <= n - 1:
            tester.iteration_scope_start("j", j)
            k = j + 1
            while k <= n:
                tester.iteration_scope_start("k", k)
                print("Hello Class")
                k += 1
                tester.iteration_scope_end_none()
            j += 1
            tester.iteration_scope_end_none()
        i += 1
        tester.iteration_scope_end_none()


if __name__ == '__main__':
    func(4)
    """
    n       total calls in k
    10      120
    9       84
    8       56
    7       35
    6       20
    5       10
    4       4
    3       1
    
    Calls of k for i for given n
    n = 6   
            i       j       k
            1
                    2
                            3
                            4
                            5
                            6
                    3
                            4
                            5
                            6
                    4
                            5
                            6
                    5       
                            6
            2
                    3       
                            4
                            5
                            6
                    4
                            5
                            6
                    5   
                            6
            3
                    4       
                            5
                            6
                    5
                            6
            4
                    5
                            6

    Calls of k for i for given n
    n = 6   
            i       j       k
            ------------------
            1
                    --------- 
                    2
                            3
                            4
                            5
                            6
                    --------- 
                    3
                            4
                            5
                            6
                    --------- 
                    4
                            5
                            6
                    --------- 
                    5       
                            6
            ------------------ 
            2       
                    ---------
                    3       
                            4
                            5
                            6
                    ---------
                    4
                            5
                            6
                    ---------
                    5   
                            6
            ------------------
            3       
                    ---------
                    4       
                            5
                            6
                    ---------
                    5
                            6
            ------------------
            4       
                    ---------
                    5
                            6

    Calls of k for i for given n
    n = 6   
            i       j       k
            ------------------
            1
                    --------- 
                    2
                            3
                            4
                            5
                            6
                    --------- 
                    3
                            4
                            5
                            6
                    --------- 
                    4
                            5
                            6
                    --------- 
                    5       
                            6
                            
                            k_count = 10
                            
                    j_count = 4
            ------------------ 
            2       
                    ---------
                    3       
                            4
                            5
                            6
                    ---------
                    4
                            5
                            6
                    ---------
                    5   
                            6
                            
                            k_count = 6
                    
                    j_count = 3
            ------------------
            3       
                    ---------
                    4       
                            5
                            6
                    ---------
                    5
                            6
            ------------------
            4       
                    ---------
                    5
                            6
                            
    Calls of k for i for given n
    n = 6   
            i       j       k           i_count j_count k_count
            ---------                   ---------
            1                           1
                    ---------                   ---------
                    2                           1       
                            3                           1
                            4                           2
                            5                           3
                            6                           4
                    ---------                    ---------
                    3                           2
                            4                           5
                            5                           6
                            6                           7
                    ---------                   ---------
                    4                           3
                            5                           8
                            6                           9
                    ---------                   ---------
                    5                           4
                            6                           10
            ---------                   ---------
            2                           2
                    ---------                   ---------
                    3                           5       
                            4                           11
                            5                           12
                            6                           13
                    ---------                   ---------
                    4                           6       
                            5                           14
                            6                           15
                    ---------                   ---------
                    5                           7       
                            6                           16
            ---------                   ---------
            3                           3       
                    ---------                   ---------
                    4                           8
                            5                           17
                            6                           18
                    ---------                   ---------
                    5                           9
                            6                           19
            ---------                   ---------
            4                           4
                    ---------                   ---------
                    5                           10
                            6                           20

    Calls of k for i for given n
    n = 6   
            i       j       k           i_rel   j_rel   k_rel
            ---------                   ---------
            1                           1
                    ---------                   ---------
                    2                           1       
                            3                           1
                            4                           2
                            5                           3
                            6                           4
                    ---------                    ---------
                    3                           2
                            4                           5
                            5                           6
                            6                           7
                    ---------                   ---------
                    4                           3
                            5                           8
                            6                           9
                    ---------                   ---------
                    5                           4
                            6                           10
            ---------                   ---------
            2                           2
                    ---------                   ---------
                    3                           1       
                            4                           1
                            5                           2
                            6                           3
                    ---------                   ---------
                    4                           2       
                            5                           4
                            6                           5
                    ---------                   ---------
                    5                           3       
                            6                           6
            ---------                   ---------
            3                           3       
                    ---------                   ---------
                    4                           1
                            5                           1
                            6                           2
                    ---------                   ---------
                    5                           2
                            6                           3
            ---------                   ---------
            4                           4
                    ---------                   ---------
                    5                           3
                            6                           4                
    
    

    n to i is       n - 2
    n to j is       n - i - 1
    
    k = n - j 
    
    
    j to k
    summation from a=j to n of n - a
    summation from a=j to n of n - a
    summation from a=2 to 6 of 6 - a  # Must start at 2
    
        https://www.wolframalpha.com/input/?i=summation+from+a%3D2+to+6+of+6+-+a
    
    n to j
    True: j = n - 2
    
    summation from i=1 to j of 1
    summation from i=1 to 4 of 1 = 4
        Goes through
            1
            2
            3
            4
    
    All together
    
    # Relative to j
    summation from b=1 to j of summation from a=b+1 to n of n - a       # a=b+1 because i goes (1,2,3,4)
    
    # Relative to n
    summation from b=1 to (n-2) of summation from a=b+1 to n of n - a   # a=b+1 because i goes (1,2,3,4)
    
    # Relative to n using standard convention 
    summation from i=1 to (n-2) of summation from j=i+1 to n of n - j   # a=b+1 because i goes (1,2,3,4)
        
        https://www.wolframalpha.com/input/?i=sum+sum+n-j%2C+j%3Di%2B1+to+n%2C+i%3D1+to+n-2
        https://www.wolframalpha.com/input/?i=sum+sum+n-j%2C+j%3Di%2B1+to+n%2C+i%3D1+to+n-2%2C+where+n+%3D+6
    
    # Relative to n using standard convention, but i=0
    summation from i=0 to (n-3) of summation from j=i+2 to n of n - j   # a=b+2 because i goes (0,1,2,3)
    
    # Relative to n using standard convention
    n = 6
    summation from i=1 to (n-2) 
                                i
                                1
                                2
                                3
                                4
    
                                of summation from j=i+1 to n of n - j
                                                                    
                                                                    j
                                                                    2
                                                                    3
                                                                    4
                                                                    5
                                                                    #6  # 6 result in the value of 0 so you can ignore
                                                                    
    """

    tester.print()
