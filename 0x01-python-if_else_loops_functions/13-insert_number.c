#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - add_node
 * @head: head
 * @number: number
 * Return: head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p;
	listint_t *current;

	p = malloc(sizeof(listint_t));
	if (p == NULL)
	{
		return (NULL);
	}
	p->n = number;
	p->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
	p->next = *head;
	*head = p;
	return (p);
	}
	current = *head;
	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}
	p->next = current->next;
	current->next = p;
	return (p);
}
