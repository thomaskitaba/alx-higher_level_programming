#include "lists.h"
/**
* print_dlistint - print valus of a double linked list
* @h: head of the double linked list
* Return: number of nodes
*/
size_t print_dlistint (const dlistint_t *h)
{
const dlistint_t *list;
size_t i;

list = h;
i = 0;
while (list)
{
	i++;
	printf("%d", list->n);
	list = list->next;
}
return (i);
}
