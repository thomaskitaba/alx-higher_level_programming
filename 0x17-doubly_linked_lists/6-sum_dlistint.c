#include "lists.h"
/**
* sum_dlistint - add all node values
* @head: head of the double linked list
* Return: sum
*/
int sum_dlistint(dlistint_t *head)
{
dlistint_t *current;
int value, sum;
current = head;
sum = value = 0;

if (head == NULL)
	return (0);
while (current)
{
	value = current->n;
	sum += value;
	current = current->next;
}
return (sum);
}
