#include "lists.h"

listint_t *reverse_linked_list(listint_t *list)
{
listint_t *previous, *Next, *current;
current = list;
previous = Next = NULL;
// set Next node
while (current)
{
  Next = current->next;
  // make the reverse
  current->next = previous;
  // adjust for next iteration
  previous = current;
  current = Next;
}
list = previous;
return (list);
}
