#include "lists.h"
/**
* add_dnodeint_end - add node at the end of d_list
* @head: head of the double linked list
* @n: number to be inserted
* Return: inserted node address, or NUll
*/
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
dlistint_t *current, *Next, *list;
current = Next = *head;
list = NULL;

list = (dlistint_t *)malloc(sizeof(dlistint_t));
if (list == NULL)
	return (NULL);
list->n = n;
/*handle empty head*/
if (*head == NULL)
{
	list->prev = NULL;
	list->next = NULL;
	*head = list;
	return (*head);
}
/*go to the end of the node*/
while (Next)
{
	current = Next;
	Next = Next->next;
}
	current->next = list;
	list->prev = current;
	list->next = NULL;
	return (*head);
}
