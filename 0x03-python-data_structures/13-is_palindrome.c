#include "lists.h"

int is_palindrome(listint_t **head)
{

listint_t *reversed_list, *current;
current = *head;
int palindrom = 0;
reversed_list = reverse_linked_list(*head);
while (!reversed_list->next)
{
    if (reversed_list->n != current->n)
        palindrom = 1;
    reversed_list = reversed_list->next;
    current = current->next;
}
if (palindrom == 0)
    return (0);
else
    return (1);
}