#include "lists.h"
/**
* dlistint_len - return length of double linke list
* @h: head of double linked list
* Return: length of node
*/
size_t dlistint_len(const dlistint_t *h)
{
const dlistint_t *list;
size_t i;

list = h;
i = 0;
while (list)
{
	i++;
	list = list->next;
}
return (i);
}
