#include "lists.h"
/**
* reverse_linked_list - reverse a list
* @list:  head of linked list
* Return: head of reversed list
*/

listint_t *reverse_linked_list(listint_t **head)
{
listint_t *previous, *Next, *current;
current = *head;
previous = Next = NULL;
while (current)
{
	Next = current->next;
	current->next = previous;
	previous = current;
	current = Next;
}
*head = previous;
return (*head);
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
int i, size;
if (*head == NULL || (*head)->next == NULL)
	return (1);

size = i = 0;
temp = *head;
while (!temp)
{
    size++;
    temp = temp->next;
}
temp = *head;
for (i = 0; i < size / 2; i++)
{
    temp = temp->next;
}
if (size % 2 == 0 && temp->n != temp->next->n)
    return (0);

temp = temp->next->next;

reversed_list = reverse_linked_list(&temp);
list_copy = reversed_list;
temp = reversed_list;
while (!reversed_list->next)
{
	if (reversed_list->n != current->n)
		return (0);
	reversed_list = reversed_list->next;
	current = current->next;
}
reverse_linked_list(&temp);
return (1);
}
