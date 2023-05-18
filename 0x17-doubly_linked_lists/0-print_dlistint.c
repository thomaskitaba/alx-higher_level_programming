#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *list;
size_t i;

list = h;
i = 0;
while(list)
{
    i++;
    printf("%d", list->n);
    list = list->next;
}
return (i);
}