class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    new_head = head.next
    prev = None

    while head and head.next:
        temp = head.next.next
        head.next.next = head
        if prev:
            prev.next = head.next
        head.next = temp
        prev = head
        head = temp

    return new_head

def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

# Приклад використання:
# Створення списку [1, 2, 3, 4]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Original List:")
print_list(head)

new_head = swap_pairs(head)
print("\nList after swapping pairs:")
print_list(new_head)