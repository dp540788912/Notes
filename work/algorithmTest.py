
# """path in array
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def solution(target, arr, visited, x, y):
#     if not target:
#         return True
    
#     if x < 0 or x >= len(arr) or \
#             y < 0 or y >= len(arr[0]) or \
#                 visited[x][y] == True:
#                 return False
#     if target[0] != arr[x][y]:
#         return False
#     visited[x][y] = True

#     for i in range(0,4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]
#         if solution(target[1:], arr, visited, next_x, next_y):
#             return True
#     visited[x][y] = False
#     return False
    


# if __name__ == "__main__":
#     arr = [list('abtg'), list('cfcs'), list('jdeh')]
#     visited = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
#     target = 'tcfdeh'
#     for k1, v1 in enumerate(arr):
#         for k2, v2 in enumerate(v1):
#             if solution(target, arr, visited, k1, k2):
#                 print("find one!!!!!!!!!!!, index is {}{}".format(k1, k2))
# """


# """permutation
# def recursive_add(ans_arr, selection, cur, visited: set, limit):
#     if len(cur) == limit:
#         ans_arr.append(cur)
#         return
#     for ch in selection:
#         if ch not in visited:
#             visited.add(ch)
#             recursive_add(ans_arr, selection, cur + ch, visited, limit)
#             visited.remove(ch)


# if __name__ == "__main__":
#     ans = []
#     select = "13689"
#     for i in range(1, len(select)+ 1):
#         recursive_add(ans, select, "", set(), i)
#     print(ans)

# """

# """
# class Node:
#     def __init__(self, v):
#         self.val = v
#         self.next = None
    
#     def print(self):
#         print(self.val)
#         itr = self.next
#         while itr:
#             print(itr.val)
#             itr = itr.next


# def recursive(root, last):
#     if root.next is None:
#         root.next = last
#         return root
    
#     ans = recursive(root.next, root)
#     root.next = last
#     return ans
    

# if __name__ == "__main__":
#     root = Node(0)
#     head = root
#     for i in range(10):
#         tmp = root
#         root.next = Node(i)
#         root = root.next
#     new = recursive(head, None)
#     new.print()
#     # head.print()
# """


# # """
# class Node:
#     def __init__(self, v):
#         self.val = v
#         self.next = None
    
#     def print(self):
#         print(self.val)
#         itr = self.next
#         while itr:
#             print(itr.val)
#             itr = itr.next
# def merge(n1, n2):
#     head = Node(-1)
#     cur = head
#     while n1 and n2:
#         if n1.val <= n2.val:
#             cur.next = n1
#             n1 = n1.next
#         else:
#             cur.next = n2
#             n2 = n2.next
#         cur = cur.next
    
#     if n1:
#         cur.next = n1
#     if n2:
#         cur.next = n2
    
#     return head.next


# if __name__ == "__main__":
#     head1 = Node(0)
#     head2 = Node(0)

#     cur1 = head1
#     cur2 = head2
#     for i in range(1,10,2):
#         cur1.next = Node(i)
#         cur1 = cur1.next
#         cur2.next = Node(i+1)
#         cur2 = cur2.next
    
#     new_head = merge(head1, head2)
#     new_head.print()

import sys 

while True:
    s = sys.stdin.readline().strip().split(' ')
    print(s)

