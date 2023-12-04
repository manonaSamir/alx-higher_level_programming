#include "lists.h"

/**
 * reverseList - reverse list
 * @head: pointer to pointer of first node of listint_t list
 * Return: A pointer to the head of the reversed list.
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
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
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
	reverseList(&front);
	return (1);
}
