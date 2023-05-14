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
listint_t *reversed_list, *current, *temp;
current = *head;
if (*head == NULL || (*head)->next == NULL)
	return (1);
reversed_list = reverse_linked_list(head);
temp = reversed_list;
while (!temp->next)
{
	if (temp->n != current->n)
		return (0);
	temp = temp->next;
	current = current->next;
}
*head = reverse_linked_list(&reversed_list);
return (1);
}
