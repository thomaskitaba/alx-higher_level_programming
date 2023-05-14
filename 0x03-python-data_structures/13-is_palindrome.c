#include "lists.h"
/**
* reverse_linked_list - reverse a list
* @head:  head of linked list
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
listint_t *reversed_list, *current, *temp, *list_backup;
int i, size;
size = i = 0;
current = temp = *head;

if (*head == NULL || (*head)->next == NULL)
	return (1);

while (temp)
{
	size++;
	temp = temp->next;
}
temp = *head;
for (i = 0; i < size / 2 - 1; i++)
{
	temp = temp->next;
}
if (size % 2 == 0 && temp->n != temp->next->n)
	return (0);
if (size % 2 != 0)
	temp = temp->next->next;
else
	temp = temp->next;

reversed_list = reverse_linked_list(&temp);
temp = reversed_list;
while (reversed_list)
{
	if (reversed_list->n != current->n)
		return (0);
	reversed_list = reversed_list->next;
	current = current->next;
}
reverse_linked_list(&temp);
return (1);
}
