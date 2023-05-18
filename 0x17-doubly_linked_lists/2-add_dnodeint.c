#include "lists.h"
/**
* add_dnodeint - add node at the begning
* @head: head of the double linked list
* @n: number to be inserted to the list
* Return: head of the node, or Null
*/
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
dlistint_t *current, *list;
current = *head;
list = NULL;

list = (dlistint_t *)malloc(sizeof(dlistint_t));
list->n = n;
if (!list)
	return (NULL);
if (!*head)
{
	list->prev = NULL;
	list->next = NULL;
}
else
{
list->prev = NULL;
list->next = current;
current->prev = list;
}
*head = list;
return (*head);
}
