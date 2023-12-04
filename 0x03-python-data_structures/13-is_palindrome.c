#include "lists.h"

/**
 * reverseList - reverse list
 * @head: pointer to pointer of first node of listint_t list
 * Return: reversed list
 */
listint_t *reverseList(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: if success is_palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = *head;
	listint_t *rare = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (front != NULL && front->next != NULL)
	{
		front = front->next->next;
		rare = rare->next;
	}
	listint_t *reversedSecondHalf = reverseList(&rare);
	listint_t *firstHalf = *head;

	while (reversedSecondHalf != NULL)
	{
		if (firstHalf->n != reversedSecondHalf->n)
			return (0);
		firstHalf = firstHalf->next;
		reversedSecondHalf = reversedSecondHalf->next;
	}
	return (1);
}
