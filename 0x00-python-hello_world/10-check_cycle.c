#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check for a cycle
 * @list: list of node
 * Return: 1 if cycle exists, 0 if no cycle
 */

int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

if (list == NULL)
return (0);
slow = fast = list;
while (slow != NULL && fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
{
return (1);
}
}
return (0);
}