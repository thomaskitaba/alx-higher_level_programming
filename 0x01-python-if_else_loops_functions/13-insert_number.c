#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * insert_node - free node
 * @str: string passed
 * @head: node head recived
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
int j;
listint_t *Next, *current, *new;
current = *head;

if (!*head)
return (NULL);
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
j = 0;
new->n = number;
while(current)
{
Next = current->next;
if (number < current->n && j == 0)
{
  new->next = *head;
  *head = new; /*check latter*/
  return (*head);
}
if (Next == NULL && number >= current->n)
{
  new->next = NULL;
  current->next = new;
  break;
}
if (number >= current->n && number < Next->n)
{
  current->next = new;
  new->next = Next;
  break;
}
j++;
current = Next;
}
return (*head);
}