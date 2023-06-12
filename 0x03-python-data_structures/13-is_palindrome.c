#include "lists.h"

/**
 * is_palindrome - is_palindrome
 * head: head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t* slow;
	listint_t* fast;
	listint_t* prev;
	listint_t* next;

	if (*head == NULL || (*head)->next == NULL) 
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	prev = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
