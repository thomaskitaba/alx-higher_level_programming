#include "lists.h"
/**
* free_dlistint - free a double linked list
* @head: head of the double linked list
* Return: Nothing
*/
void free_dlistint(dlistint_t *head)
{
dlistint_t *current, *Next;
current = Next = head;

if (head == NULL)
	return;

while (Next)
{
	current = Next;
	Next = Next->next;
	free(current);
}
}