#include "lists.h"
/**
* reverse_linked_list - reverse a list
* @list:  head of linked list
* Return: head of reversed list
*/

listint_t *reverse_linked_list(listint_t **list)
{
listint_t *previous, *Next, *current;
current = *list;
previous = Next = NULL;
while (current)
{
	Next = current->next;
	current->next = previous;
	previous = current;
	current = Next;
}
*list = previous;
return (*list);
}
/**
* is_palindrome - check if palindrome
* @head:   head of orignal list
* Return: 0 if palinderome, 1 if not palinderome
*/
int is_palindrome(listint_t **head)
{
listint_t *reversed_list, *current;
current = *head;
if (*head == NULL || (*head)->next == NULL)
	return (1);
/*while (p)
{
q = q->next;
p = p->next->next;
if (p == NULL)
	reversed_list = reverse_linked_list(&(q->next->next));
}*/
reversed_list = reverse_linked_list(head);
while (!reversed_list->next)
{
	if (reversed_list->n != current->n)
		return (0);
	reversed_list = reversed_list->next;
	current = current->next;
}
return (1);
}
