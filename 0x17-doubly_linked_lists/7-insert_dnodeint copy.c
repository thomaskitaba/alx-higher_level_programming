#include "lists.h"
/**
* insert_dnodeint_at_index - insert at specfic index
* @h: head of the double linked list
* @n: number to be inserted
* @idx: index for the number to be inserted
* Return: head of the list, or NULL on faliure
*/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
dlistint_t *current, *list;
unsigned int i;
current = *h;
list = NULL;

i = 0;
if (idx == 0)
    add_dnodeint_end(h, n);
if (h == NULL)
    return (NULL);
list = (dlistint_t *)malloc(sizeof(dlistint_t));
if (list == NULL)
    return (NULL);
list->n = n;
while (current)
{
    /*Next = Next->next;*/
    if (i == idx)
    {
        list->prev = current->prev;
        list->next = current->prev->next;
        current->prev = list;
        return (*h);
    }
    current = current->next;
    i++;
}
add_dnodeint_end(h, n);
return (NULL);
/*we can handle edge case here if we wont to insert at the
end if index is beyond range*/
}