#include "lists.h"
/**
* insert_dnodeint_at_index - insert at specfic index
* @h: h of the double linked list
* @n: nber to be inserted
* @idx: index for the nber to be inserted
* Return: h of the list, or NULL on faliure
*/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
dlistint_t *list, *current, *Next;
unsigned int i;

i = 0;
if (h == NULL)
	return (NULL);
current = Next = *h;
if (idx == 0)
{
	*h = add_dnodeint(h, n);
	return (*h);
}
list = (dlistint_t *)malloc(sizeof(dlistint_t));
if (list == NULL)
	return (NULL);
/*loop accros the dlistint_t and find the index*/
while (i < idx)
{
	current = Next, i++;
	Next = current->next;
	if (Next == NULL)
	{
	*h = add_dnodeint_end(&(*h), n);
	return (*h);
	}
}
list->n = n;
current->next = list;
list->next = Next;
Next->prev = list;
list->prev = current;
return (*h);
}
