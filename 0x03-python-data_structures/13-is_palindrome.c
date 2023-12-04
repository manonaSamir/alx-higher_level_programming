#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *front = *head;
	listint_t *rare = *head;

	/*Find the middle of the linked list*/
	while (front != NULL && front->next != NULL)
	{
		front = front->next->next;
		rare = rare->next;
	}

	/*Reverse the second half of the linked list*/
	listint_t *reversedSecondHalf = reverseList(rare);

	/* Compare the first half and reversed second half*/
	listint_t *firstHalf = *head;
	while (reversedSecondHalf != NULL)
	{
		if (firstHalf->n != reversedSecondHalf->n)
		{
			return 0; /*Not a palindrome*/
		}
		firstHalf = firstHalf->next;
		reversedSecondHalf = reversedSecondHalf->next;
	}

	return (1);
}

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
