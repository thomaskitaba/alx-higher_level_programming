#include "lists.h"
/**
* get_dnodeint_at_index - get node at index
* @head: head of the double linked list
* @index: index of node to be searched
* Return: pointer to the inserted node
*/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
dlistint_t *current;
int i;
current = head;
i = 0;
if (head == NULL)
	return (NULL);
while (current)
{
if (i == (int)index)
{
	return (current);
}
current = current->next;
i++;
}
return (NULL);
}
