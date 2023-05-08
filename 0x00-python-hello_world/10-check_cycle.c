#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * find_listint_loop - free node
 * @list: list of node
 * Return: node
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
slow = list;
return (1);
}
}
return (0);
}