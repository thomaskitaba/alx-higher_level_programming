#include "lists.h"
/**
*
*
*/

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
/**
*
*
*/
int is_palindrome(listint_t **head)
{

listint_t *reversed_list, *current;
current = *head;
int palindrom = 1;
reversed_list = reverse_linked_list(*head);
while (!reversed_list->next)
{
    if (reversed_list->n != current->n)
        palindrom = 0;
    reversed_list = reversed_list->next;
    current = current->next;
}
if (palindrom == 0)
    return (0);
else
    return (1);
}